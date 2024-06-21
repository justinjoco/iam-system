import connexion
import six

from swagger_server.models.create_permission_body import CreatePermissionBody  # noqa: E501
from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.resource_write_success_response import ResourceWriteSuccessResponse  # noqa: E501
from swagger_server import util


def create_permission(body=None):  # noqa: E501
    """Create permission

     # noqa: E501

    :param body: Create permission object
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = CreatePermissionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_permission_by_id(permission_id):  # noqa: E501
    """Get permission by id

     # noqa: E501

    :param permission_id: permission id
    :type permission_id: 

    :rtype: Permission
    """
    return 'do some magic!'


def get_users_with_permissions(action, resource, resource_id):  # noqa: E501
    """Get users with permissions to given resource with resourceId

     # noqa: E501

    :param action: permission action
    :type action: str
    :param resource: permission resource
    :type resource: str
    :param resource_id: permission resource id
    :type resource_id: 

    :rtype: List[Permission]
    """
    return 'do some magic!'
