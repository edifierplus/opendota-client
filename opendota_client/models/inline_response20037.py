# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.   # noqa: E501

    OpenAPI spec version: 18.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20037(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'table_name': 'str',
        'column_name': 'str',
        'data_type': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'column_name': 'column_name',
        'data_type': 'data_type'
    }

    def __init__(self, table_name=None, column_name=None, data_type=None):  # noqa: E501
        """InlineResponse20037 - a model defined in Swagger"""  # noqa: E501

        self._table_name = None
        self._column_name = None
        self._data_type = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        if data_type is not None:
            self.data_type = data_type

    @property
    def table_name(self):
        """Gets the table_name of this InlineResponse20037.  # noqa: E501

        table_name  # noqa: E501

        :return: The table_name of this InlineResponse20037.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this InlineResponse20037.

        table_name  # noqa: E501

        :param table_name: The table_name of this InlineResponse20037.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this InlineResponse20037.  # noqa: E501

        column_name  # noqa: E501

        :return: The column_name of this InlineResponse20037.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this InlineResponse20037.

        column_name  # noqa: E501

        :param column_name: The column_name of this InlineResponse20037.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def data_type(self):
        """Gets the data_type of this InlineResponse20037.  # noqa: E501

        data_type  # noqa: E501

        :return: The data_type of this InlineResponse20037.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this InlineResponse20037.

        data_type  # noqa: E501

        :param data_type: The data_type of this InlineResponse20037.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20037, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20037):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
