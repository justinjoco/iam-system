import connexion
import six

from swagger_server.models.change_password_body import ChangePasswordBody  # noqa: E501
from swagger_server.models.create_user_body import CreateUserBody  # noqa: E501
from swagger_server.models.resource_write_success_response import ResourceWriteSuccessResponse  # noqa: E501
from swagger_server.models.update_user_body import UpdateUserBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def change_user_password(user_id, body=None):  # noqa: E501
    """Change password of user given userId

     # noqa: E501

    :param user_id: The id that needs to be fetched
    :type user_id: 
    :param body: Change password body
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = ChangePasswordBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(body=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: Create user object
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = CreateUserBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_by_id(user_id):  # noqa: E501
    """Soft delete a user

     # noqa: E501

    :param user_id: The id that needs to be fetched
    :type user_id: 

    :rtype: ResourceWriteSuccessResponse
    """
    return 'do some magic!'


def get_user_by_id(user_id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param user_id: The id that needs to be fetched
    :type user_id: 

    :rtype: User
    """
    return 'do some magic!'


def get_users():  # noqa: E501
    """Get users

     # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def update_user_by_id(user_id, body=None):  # noqa: E501
    """Update info of user

     # noqa: E501

    :param user_id: The id that needs to be fetched
    :type user_id: 
    :param body: Update user body
    :type body: dict | bytes

    :rtype: ResourceWriteSuccessResponse
    """
    if connexion.request.is_json:
        body = UpdateUserBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
