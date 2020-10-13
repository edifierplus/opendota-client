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


class PlayersaccountIdmatchesHeroes(object):
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
        'player_slot': 'PlayersaccountIdmatchesHeroesPlayerSlot'
    }

    attribute_map = {
        'player_slot': 'player_slot'
    }

    def __init__(self, player_slot=None):  # noqa: E501
        """PlayersaccountIdmatchesHeroes - a model defined in Swagger"""  # noqa: E501

        self._player_slot = None
        self.discriminator = None

        if player_slot is not None:
            self.player_slot = player_slot

    @property
    def player_slot(self):
        """Gets the player_slot of this PlayersaccountIdmatchesHeroes.  # noqa: E501


        :return: The player_slot of this PlayersaccountIdmatchesHeroes.  # noqa: E501
        :rtype: PlayersaccountIdmatchesHeroesPlayerSlot
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """Sets the player_slot of this PlayersaccountIdmatchesHeroes.


        :param player_slot: The player_slot of this PlayersaccountIdmatchesHeroes.  # noqa: E501
        :type: PlayersaccountIdmatchesHeroesPlayerSlot
        """

        self._player_slot = player_slot

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
        if issubclass(PlayersaccountIdmatchesHeroes, dict):
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
        if not isinstance(other, PlayersaccountIdmatchesHeroes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other