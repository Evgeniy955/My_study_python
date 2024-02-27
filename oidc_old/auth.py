import requests

from Rest.auth.oidc_old.oauth import PKCESecret, fetch_token, open_authorization_endpoint

client_id = "complete-anatomy"
authorization_endpoint = "https://accounts.nonprod.3d4medical.com/protocol/openid-connect/auth"
token_endpoint = "https://accounts.nonprod.3d4medical.com/protocol/openid-connect/token"
userinfo_endpoint = "https://accounts.nonprod.3d4medical.com/protocol/openid-connect/userinfo"
redirect_uri = "http://localhost:3000/"
pkce_secret = PKCESecret()


def _login():
    authorization_code = open_authorization_endpoint(
        endpoint=authorization_endpoint,
        redirect_uri=redirect_uri,
        client_id=client_id,
        pkce_secret=pkce_secret,
        scope="openid",
    )

    token_response, content_dict = fetch_token(
        client_id=client_id,
        redirect_uri=redirect_uri,
        pkce_secret=pkce_secret,
        code=authorization_code,
        token_uri=token_endpoint,
    )
    return token_response, content_dict, authorization_code


def get_info():
    token_response, content_dict, code = _login()
    if token_response.status_code == 200:
        for key, value in content_dict.items():
            print(f"{key}: {value}")
        token_info = token_response.json()
        access_token = token_info.get("access_token")
        # return access_token

        # The UserInfo endpoint contains provisions about authorized user.
        userinfo_response = requests.get(userinfo_endpoint, headers={"Authorization": f"Bearer {access_token}"})
        if userinfo_response.status_code == 200:
            userinfo = userinfo_response.json()
            print(f"User Information: \n{userinfo}")
            print(f"Authorization code: {code}")
        else:
            print(f"Error while retrieving user information: {userinfo_response.status_code}")
    else:
        print(f"Error when receiving tokens: {token_response.status_code}")


if __name__ == "__main__":
    get_info()
