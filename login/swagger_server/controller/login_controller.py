import connexion
import six

from swagger_server.models.login_credentials import LoginCredentials  # noqa: E501
from swagger_server import util
from swagger_server.service.login_service import login_service


def register_get():  # noqa: E501
    """Get user account creation page

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def submit_login_credentials(body,
                             client_id=None,
                             code_challenge=None,
                             code_challenge_method=None,
                             redirect_uri=None,
                             state=None):  # noqa: E501
    """Post login creds

     # noqa: E501

    :param body: User login credentials
    :type body: dict | bytes
    :param client_id: client app id
    :type client_id: str
    :param code_challenge: This is to be saved for later code verification
    :type code_challenge: str
    :param code_challenge_method: code challenge method for pkce
    :type code_challenge_method: str
    :param redirect_uri: client app redirect uri
    :type redirect_uri: str
    :param state: An opaque value the client adds to the initial request that is included when redirecting back to the client. This value must be used by the client to prevent CSRF attacks.
    :type state: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoginCredentials.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
