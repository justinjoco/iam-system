# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CreateUserBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, first_name: str=None, last_name: str=None, email: str=None, roles: List[str]=None):  # noqa: E501
        """CreateUserBody - a model defined in Swagger

        :param username: The username of this CreateUserBody.  # noqa: E501
        :type username: str
        :param first_name: The first_name of this CreateUserBody.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this CreateUserBody.  # noqa: E501
        :type last_name: str
        :param email: The email of this CreateUserBody.  # noqa: E501
        :type email: str
        :param roles: The roles of this CreateUserBody.  # noqa: E501
        :type roles: List[str]
        """
        self.swagger_types = {
            'username': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'roles': List[str]
        }

        self.attribute_map = {
            'username': 'username',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'roles': 'roles'
        }
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._roles = roles

    @classmethod
    def from_dict(cls, dikt) -> 'CreateUserBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateUserBody of this CreateUserBody.  # noqa: E501
        :rtype: CreateUserBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this CreateUserBody.


        :return: The username of this CreateUserBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this CreateUserBody.


        :param username: The username of this CreateUserBody.
        :type username: str
        """

        self._username = username

    @property
    def first_name(self) -> str:
        """Gets the first_name of this CreateUserBody.


        :return: The first_name of this CreateUserBody.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this CreateUserBody.


        :param first_name: The first_name of this CreateUserBody.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this CreateUserBody.


        :return: The last_name of this CreateUserBody.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this CreateUserBody.


        :param last_name: The last_name of this CreateUserBody.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this CreateUserBody.


        :return: The email of this CreateUserBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this CreateUserBody.


        :param email: The email of this CreateUserBody.
        :type email: str
        """

        self._email = email

    @property
    def roles(self) -> List[str]:
        """Gets the roles of this CreateUserBody.


        :return: The roles of this CreateUserBody.
        :rtype: List[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List[str]):
        """Sets the roles of this CreateUserBody.


        :param roles: The roles of this CreateUserBody.
        :type roles: List[str]
        """

        self._roles = roles
