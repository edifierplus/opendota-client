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


class InlineResponse20032(object):
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
        'match_id': 'int',
        'cluster': 'int',
        'replay_salt': 'int'
    }

    attribute_map = {
        'match_id': 'match_id',
        'cluster': 'cluster',
        'replay_salt': 'replay_salt'
    }

    def __init__(self, match_id=None, cluster=None, replay_salt=None):  # noqa: E501
        """InlineResponse20032 - a model defined in Swagger"""  # noqa: E501

        self._match_id = None
        self._cluster = None
        self._replay_salt = None
        self.discriminator = None

        if match_id is not None:
            self.match_id = match_id
        if cluster is not None:
            self.cluster = cluster
        if replay_salt is not None:
            self.replay_salt = replay_salt

    @property
    def match_id(self):
        """Gets the match_id of this InlineResponse20032.  # noqa: E501

        match_id  # noqa: E501

        :return: The match_id of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this InlineResponse20032.

        match_id  # noqa: E501

        :param match_id: The match_id of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._match_id = match_id

    @property
    def cluster(self):
        """Gets the cluster of this InlineResponse20032.  # noqa: E501

        cluster  # noqa: E501

        :return: The cluster of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this InlineResponse20032.

        cluster  # noqa: E501

        :param cluster: The cluster of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._cluster = cluster

    @property
    def replay_salt(self):
        """Gets the replay_salt of this InlineResponse20032.  # noqa: E501

        replay_salt  # noqa: E501

        :return: The replay_salt of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._replay_salt

    @replay_salt.setter
    def replay_salt(self, replay_salt):
        """Sets the replay_salt of this InlineResponse20032.

        replay_salt  # noqa: E501

        :param replay_salt: The replay_salt of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._replay_salt = replay_salt

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
        if issubclass(InlineResponse20032, dict):
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
        if not isinstance(other, InlineResponse20032):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other