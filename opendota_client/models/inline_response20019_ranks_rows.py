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


class InlineResponse20019RanksRows(object):
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
        'bin': 'int',
        'bin_name': 'int',
        'count': 'int',
        'cumulative_sum': 'int'
    }

    attribute_map = {
        'bin': 'bin',
        'bin_name': 'bin_name',
        'count': 'count',
        'cumulative_sum': 'cumulative_sum'
    }

    def __init__(self, bin=None, bin_name=None, count=None, cumulative_sum=None):  # noqa: E501
        """InlineResponse20019RanksRows - a model defined in Swagger"""  # noqa: E501

        self._bin = None
        self._bin_name = None
        self._count = None
        self._cumulative_sum = None
        self.discriminator = None

        if bin is not None:
            self.bin = bin
        if bin_name is not None:
            self.bin_name = bin_name
        if count is not None:
            self.count = count
        if cumulative_sum is not None:
            self.cumulative_sum = cumulative_sum

    @property
    def bin(self):
        """Gets the bin of this InlineResponse20019RanksRows.  # noqa: E501

        bin  # noqa: E501

        :return: The bin of this InlineResponse20019RanksRows.  # noqa: E501
        :rtype: int
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this InlineResponse20019RanksRows.

        bin  # noqa: E501

        :param bin: The bin of this InlineResponse20019RanksRows.  # noqa: E501
        :type: int
        """

        self._bin = bin

    @property
    def bin_name(self):
        """Gets the bin_name of this InlineResponse20019RanksRows.  # noqa: E501

        bin_name  # noqa: E501

        :return: The bin_name of this InlineResponse20019RanksRows.  # noqa: E501
        :rtype: int
        """
        return self._bin_name

    @bin_name.setter
    def bin_name(self, bin_name):
        """Sets the bin_name of this InlineResponse20019RanksRows.

        bin_name  # noqa: E501

        :param bin_name: The bin_name of this InlineResponse20019RanksRows.  # noqa: E501
        :type: int
        """

        self._bin_name = bin_name

    @property
    def count(self):
        """Gets the count of this InlineResponse20019RanksRows.  # noqa: E501

        count  # noqa: E501

        :return: The count of this InlineResponse20019RanksRows.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse20019RanksRows.

        count  # noqa: E501

        :param count: The count of this InlineResponse20019RanksRows.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cumulative_sum(self):
        """Gets the cumulative_sum of this InlineResponse20019RanksRows.  # noqa: E501

        cumulative_sum  # noqa: E501

        :return: The cumulative_sum of this InlineResponse20019RanksRows.  # noqa: E501
        :rtype: int
        """
        return self._cumulative_sum

    @cumulative_sum.setter
    def cumulative_sum(self, cumulative_sum):
        """Sets the cumulative_sum of this InlineResponse20019RanksRows.

        cumulative_sum  # noqa: E501

        :param cumulative_sum: The cumulative_sum of this InlineResponse20019RanksRows.  # noqa: E501
        :type: int
        """

        self._cumulative_sum = cumulative_sum

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
        if issubclass(InlineResponse20019RanksRows, dict):
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
        if not isinstance(other, InlineResponse20019RanksRows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
