import connexion
import six

from swagger_server import util
from swagger_server.service.authorize_service import authorize_service


def authorize(response_type=None,
              client_id=None,
              state=None,
              redirect_uri=None,
              code_challenge_method=None,
              code_challenge=None):  # noqa: E501
    """Start authorization code flow

     # noqa: E501

    :param response_type: Indicates which OAuth 2.0 Flow you want to perform. Use code for Authorization Code Grant (with and without PKCE). Use code for Authorization Code without PKCE. Use pkce for Authorization Code with PKCE
    :type response_type: str
    :param client_id: client id of application
    :type client_id: str
    :param state: An opaque value the client adds to the initial request that is included when redirecting back to the client. This value must be used by the client to prevent CSRF attacks.
    :type state: str
    :param redirect_uri: client app redirect uri
    :type redirect_uri: str
    :param code_challenge_method: code challenge method for pkce
    :type code_challenge_method: str
    :param code_challenge: Generated challenge from the code_verifier
    :type code_challenge: str

    :rtype: None
    """
    return 'do some magic!'
