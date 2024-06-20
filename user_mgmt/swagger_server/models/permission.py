# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Permission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, action: str=None, resource: str=None, roles: List[str]=None):  # noqa: E501
        """Permission - a model defined in Swagger

        :param action: The action of this Permission.  # noqa: E501
        :type action: str
        :param resource: The resource of this Permission.  # noqa: E501
        :type resource: str
        :param roles: The roles of this Permission.  # noqa: E501
        :type roles: List[str]
        """
        self.swagger_types = {
            'action': str,
            'resource': str,
            'roles': List[str]
        }

        self.attribute_map = {
            'action': 'action',
            'resource': 'resource',
            'roles': 'roles'
        }
        self._action = action
        self._resource = resource
        self._roles = roles

    @classmethod
    def from_dict(cls, dikt) -> 'Permission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Permission of this Permission.  # noqa: E501
        :rtype: Permission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self) -> str:
        """Gets the action of this Permission.


        :return: The action of this Permission.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this Permission.


        :param action: The action of this Permission.
        :type action: str
        """

        self._action = action

    @property
    def resource(self) -> str:
        """Gets the resource of this Permission.


        :return: The resource of this Permission.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str):
        """Sets the resource of this Permission.


        :param resource: The resource of this Permission.
        :type resource: str
        """

        self._resource = resource

    @property
    def roles(self) -> List[str]:
        """Gets the roles of this Permission.


        :return: The roles of this Permission.
        :rtype: List[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List[str]):
        """Sets the roles of this Permission.


        :param roles: The roles of this Permission.
        :type roles: List[str]
        """

        self._roles = roles
