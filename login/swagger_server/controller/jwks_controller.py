import connexion
import six

from swagger_server.models.jwk import JWK  # noqa: E501
from swagger_server import util
from swagger_server.service.jwks_service import jwks_service


def get_public_jwks():  # noqa: E501
    """Json web key set

     # noqa: E501


    :rtype: List[JWK]
    """
    return 'do some magic!'
