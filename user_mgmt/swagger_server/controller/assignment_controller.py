import connexion
import six

from swagger_server.models.assign_context_permission_body import AssignContextPermissionBody  # noqa: E501
from swagger_server.models.assign_role_permission_body import AssignRolePermissionBody  # noqa: E501
from swagger_server.models.assign_user_role_body import AssignUserRoleBody  # noqa: E501
from swagger_server.models.resource_write_success_response import ResourceWriteSuccessResponse  # noqa: E501
from swagger_server.models.role_permission import RolePermission  # noqa: E501
from swagger_server.models.user_role import UserRole  # noqa: E501
from swagger_server import util
from swagger_server.service.assignment_service import assignment_service


def assign_context_to_permission(body):  # noqa: E501
    """assign context to permission

     # noqa: E501

    :param body: Create permission context assignment
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = AssignContextPermissionBody.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assign_permission_to_role(body):  # noqa: E501
    """assign permission to role

     # noqa: E501

    :param body: Create role permission assignment
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = AssignRolePermissionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assign_role_to_user(body):  # noqa: E501
    """assign role to user

     # noqa: E501

    :param body: Create user role assignment
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = AssignUserRoleBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_permission_context_by_id(permission_context_id):  # noqa: E501
    """delete role permission

     # noqa: E501

    :param permission_context_id: permission context id
    :type permission_context_id: 

    :rtype: ResourceWriteSuccessResponse
    """
    return 'do some magic!'


def delete_role_permission_by_id(role_permission_id):  # noqa: E501
    """delete role permission

     # noqa: E501

    :param role_permission_id: role permissionId
    :type role_permission_id: 

    :rtype: ResourceWriteSuccessResponse
    """
    return 'do some magic!'


def delete_user_role_by_id(user_role_id):  # noqa: E501
    """delete user role

     # noqa: E501

    :param user_role_id: user role id
    :type user_role_id: 

    :rtype: ResourceWriteSuccessResponse
    """
    return 'do some magic!'


def get_all_permission_contexts():  # noqa: E501
    """get permission contexts

     # noqa: E501


    :rtype: RolePermission
    """
    return 'do some magic!'


def get_permission_context_by_id(permission_context_id):  # noqa: E501
    """get permission context

     # noqa: E501

    :param permission_context_id: permission context id
    :type permission_context_id: 

    :rtype: RolePermission
    """
    return 'do some magic!'


def get_role_permission_by_id(role_permission_id):  # noqa: E501
    """get role permission

     # noqa: E501

    :param role_permission_id: role permissionId
    :type role_permission_id: 

    :rtype: RolePermission
    """
    return 'do some magic!'


def get_role_permissions():  # noqa: E501
    """get role permissions

     # noqa: E501


    :rtype: List[RolePermission]
    """
    return 'do some magic!'


def get_user_role_by_id(user_role_id):  # noqa: E501
    """get user role

     # noqa: E501

    :param user_role_id: user role Id
    :type user_role_id: 

    :rtype: UserRole
    """
    return 'do some magic!'


def get_user_roles():  # noqa: E501
    """get user roles

     # noqa: E501


    :rtype: List[UserRole]
    """
    return 'do some magic!'
