"""OAuth 2.1 authorization flow definition utilities."""
from __future__ import annotations

import base64
import hashlib
import json
import random
import string
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from typing import cast
from urllib.parse import parse_qs, urlencode, urlparse

import requests
from requests import session


class AuthorizationCodeHandler(BaseHTTPRequestHandler):
    """OAuth 2.1 authorization code flow (with PKCE) HTTP handler."""

    def __init__(
        self,
        request,
        client_address,
        server,
    ):
        # Required for type-checking the server object
        super().__init__(request, client_address, server)

    def log_message(self, *_: str) -> None:
        # Silence HTTP server logging to *stdout* and *stderr*
        pass

    def do_GET(self) -> None:
        # BUG: init method accepts a 'RedirectionServer'
        # but it remains a 'BaseServer' here!
        server = cast(RedirectionServer, self.server)

        url = urlparse(self.path)

        # Ignore request to a path different from the specified redirection
        if url.path != server.redirection_path:
            self.send_error(HTTPStatus.NOT_FOUND, message="Not found")
            return

        qs = parse_qs(url.query)

        # Validate state
        try:
            (query_state,) = qs.get("state", [])
            if query_state != server.state:
                print("bad state in OAuth redirect URI: " f"'{query_state}', expected '{server.state}'.")
        except (TypeError, ValueError):
            print("no state in OAuth redirect URI.")

        # Get code
        try:
            (server.code,) = qs.get("code", [])
        except (TypeError, ValueError):
            print("no code in OAuth redirect URI.")

        self.send_response(HTTPStatus.OK)
        self.send_header("Connection", "close")
        self.send_header("Content-type", "text/html;utf-8")
        self.end_headers()

        self.wfile.write(
            b"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OpenID Connect | Login</title>
</head>
<body>
<h1>Authenticated!</h1>
<p>You may now close this page.</p>
<p><small>OIDC Client</small></p>
</body>
</html>"""
        )


class RedirectionServer(HTTPServer):
    """OAuth 2.1 authorization code flow (with PKCE) HTTP server."""

    def __init__(
        self,
        server_address,
        handler_class,
        redirection_path,
    ):
        super().__init__(server_address, handler_class)

        self.redirection_path = redirection_path or "/"
        self.state = base64.urlsafe_b64encode(
            "".join(random.choices(string.ascii_letters + string.digits + "-._~", k=32)).encode()
        ).decode()

        self.code: str | None = None


def start_server(port):
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    print(f"Server is running on port {port}")

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    return server, server_thread


def open_authorization_endpoint(endpoint: str, client_id: str, redirect_uri: str, pkce_secret, scope: str):
    """Direct the user agent to an OAuth 2.1 authorization server."""
    my_server, my_server_thread = start_server(3000)
    random_nonce = "".join(random.choices(string.ascii_letters + string.digits + "-._~", k=32))

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": scope,
        "code_challenge": pkce_secret.challenge,
        "code_challenge_method": pkce_secret.challenge_method,
        "ui_locales": "en",
        "nonce": random_nonce,
    }

    """Start OAuth 2.1 authorization code flow (with PKCE).
         Authorization code flow is interactive, this:
         1. opens a web browser allowing a user to log in;
         2. a local HTTP server handles the redirection from the authorization server and
        accepts the authorization code (a temporary credential used to obtain tokens)."""

    session_login = session()
    data = {
        "email": "b2b_student_plus_subscr@gmail.com",
        "password": "Sepultura1@#",
        "source": "COMPLETE_ANATOMY",
        "captcha": "123",
    }
    oidc_data = session_login.get(f"{endpoint}?{urlencode(params)}")
    session_login.post(oidc_data.url, json.dumps(data), headers={"Content-Type": "application/json"})
    redirection_response = session_login.get(oidc_data.history[1].url)
    location_response = redirection_response.history[0].headers["Location"]
    authorization_code = parse_qs(urlparse(location_response).query).get("code", [None])[0]

    print("Server closed")
    my_server.shutdown()
    my_server_thread.join()

    return authorization_code


def fetch_token(client_id: str, redirect_uri: str, pkce_secret, code: str, token_uri: str):
    # Data for requesting tokens
    token_data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": None,
        "redirect_uri": redirect_uri,
        "code": code,
        "code_verifier": str(pkce_secret),
    }

    # Send a POST request to exchange the authorization code for tokens
    token_response = requests.post(token_uri, data=token_data)
    content = token_response.content
    content_dict = json.loads(content.decode("utf-8"))
    return token_response, content_dict


class PKCESecret:
    """PKCE secret."""

    def __init__(self, length: int = 128):
        self.value = "".join(random.choices(string.ascii_letters + string.digits, k=length))

    def __str__(self) -> str:
        return self.value

    def __bytes__(self) -> bytes:
        return self.value.encode()

    @property
    def challenge(self) -> bytes:
        """PKCE challenge matching the secret value."""
        return base64.urlsafe_b64encode(hashlib.sha256(bytes(self)).digest()).rstrip(b"=")

    @property
    def challenge_method(self) -> str:
        """PKCE challenge method, always 'S256' in this implementation."""
        return "S256"
