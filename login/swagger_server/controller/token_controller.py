import connexion
import six

from swagger_server.models.token_response import TokenResponse  # noqa: E501
from swagger_server import util
from swagger_server.service.token_service import token_service


def generate_token(grant_type, client_id, client_secret, scope, redirect_uri,
                   code, code_verifier, refresh_token):  # noqa: E501
    """Get access token

     # noqa: E501

    :param grant_type: 
    :type grant_type: str
    :param client_id: 
    :type client_id: str
    :param client_secret: 
    :type client_secret: str
    :param scope: 
    :type scope: str
    :param redirect_uri: 
    :type redirect_uri: str
    :param code: 
    :type code: str
    :param code_verifier: 
    :type code_verifier: str
    :param refresh_token: 
    :type refresh_token: str

    :rtype: TokenResponse
    """
    return 'do some magic!'
