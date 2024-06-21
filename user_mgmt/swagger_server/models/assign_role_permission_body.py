# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssignRolePermissionBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self,
                 permission_id: str=None,
                 role_id: str=None):  # noqa: E501
        """AssignRolePermissionBody - a model defined in Swagger

        :param permission_id: The permission_id of this AssignRolePermissionBody.  # noqa: E501
        :type permission_id: str
        :param role_id: The role_id of this AssignRolePermissionBody.  # noqa: E501
        :type role_id: str
        """
        self.swagger_types = {'permission_id': str, 'role_id': str}

        self.attribute_map = {
            'permission_id': 'permissionId',
            'role_id': 'roleId'
        }
        self._permission_id = permission_id
        self._role_id = role_id

    @classmethod
    def from_dict(cls, dikt) -> 'AssignRolePermissionBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssignRolePermissionBody of this AssignRolePermissionBody.  # noqa: E501
        :rtype: AssignRolePermissionBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def permission_id(self) -> str:
        """Gets the permission_id of this AssignRolePermissionBody.


        :return: The permission_id of this AssignRolePermissionBody.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id: str):
        """Sets the permission_id of this AssignRolePermissionBody.


        :param permission_id: The permission_id of this AssignRolePermissionBody.
        :type permission_id: str
        """

        self._permission_id = permission_id

    @property
    def role_id(self) -> str:
        """Gets the role_id of this AssignRolePermissionBody.


        :return: The role_id of this AssignRolePermissionBody.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: str):
        """Sets the role_id of this AssignRolePermissionBody.


        :param role_id: The role_id of this AssignRolePermissionBody.
        :type role_id: str
        """

        self._role_id = role_id