import connexion
import six

from swagger_server.models.create_role_body import CreateRoleBody  # noqa: E501
from swagger_server.models.resource_write_success_response import ResourceWriteSuccessResponse  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server import util


def create_role(body=None):  # noqa: E501
    """Create role

     # noqa: E501

    :param body: Created role object
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = CreateRoleBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_role_by_id(role_id):  # noqa: E501
    """Get role by id

     # noqa: E501

    :param role_id: role id
    :type role_id: 

    :rtype: Role
    """
    return 'do some magic!'


def get_role_by_name(role_name):  # noqa: E501
    """Get role by name

     # noqa: E501

    :param role_name: role name
    :type role_name: str

    :rtype: Role
    """
    return 'do some magic!'


def get_roles():  # noqa: E501
    """Get roles

     # noqa: E501


    :rtype: List[Role]
    """
    return 'do some magic!'
