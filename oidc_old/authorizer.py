from Rest.auth.legasy_sso.sso_session import LegacySsoAuthorizer
from Rest.auth.oidc.oidc_session import OidcAuthorizer
from Web.definitions import AUTHORIZE


class Authorizer:
    sessions = {}  # to store sessions by credential name
    auth_methods = {
        "LEGACY_SSO": LegacySsoAuthorizer,
        "OIDC": OidcAuthorizer,
        # "neoid": NeoIdAuthorizer,
    }

    def __init__(self, auth_method):
        self.auth_method = self.auth_methods[auth_method]()

    def __getitem__(self, credential_name):
        return self.get_session(credential_name)

    def get_session(self, credential_name):
        # Create a new session if it is not exist for the target credentials
        if credential_name not in self.sessions:
            self.sessions[credential_name] = self.auth_method[credential_name]
        return self.sessions[credential_name]


authorizer = Authorizer(auth_method=AUTHORIZE)
