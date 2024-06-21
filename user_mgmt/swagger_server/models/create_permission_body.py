# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CreatePermissionBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, resource: str=None):  # noqa: E501
        """CreatePermissionBody - a model defined in Swagger

        :param action: The action of this CreatePermissionBody.  # noqa: E501
        :type action: str
        :param resource: The resource of this CreatePermissionBody.  # noqa: E501
        :type resource: str
        """
        self.swagger_types = {'action': str, 'resource': str}

        self.attribute_map = {'action': 'action', 'resource': 'resource'}
        self._action = action
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt) -> 'CreatePermissionBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreatePermissionBody of this CreatePermissionBody.  # noqa: E501
        :rtype: CreatePermissionBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self) -> str:
        """Gets the action of this CreatePermissionBody.


        :return: The action of this CreatePermissionBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this CreatePermissionBody.


        :param action: The action of this CreatePermissionBody.
        :type action: str
        """

        self._action = action

    @property
    def resource(self) -> str:
        """Gets the resource of this CreatePermissionBody.


        :return: The resource of this CreatePermissionBody.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str):
        """Sets the resource of this CreatePermissionBody.


        :param resource: The resource of this CreatePermissionBody.
        :type resource: str
        """

        self._resource = resource