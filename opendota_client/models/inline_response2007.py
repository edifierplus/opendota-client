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


class InlineResponse2007(object):
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
        'account_id': 'int',
        'last_played': 'int',
        'win': 'int',
        'games': 'int',
        'with_win': 'int',
        'with_games': 'int',
        'against_win': 'int',
        'against_games': 'int',
        'with_gpm_sum': 'int',
        'with_xpm_sum': 'int',
        'personaname': 'str',
        'name': 'str',
        'is_contributor': 'bool',
        'last_login': 'str',
        'avatar': 'str',
        'avatarfull': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'last_played': 'last_played',
        'win': 'win',
        'games': 'games',
        'with_win': 'with_win',
        'with_games': 'with_games',
        'against_win': 'against_win',
        'against_games': 'against_games',
        'with_gpm_sum': 'with_gpm_sum',
        'with_xpm_sum': 'with_xpm_sum',
        'personaname': 'personaname',
        'name': 'name',
        'is_contributor': 'is_contributor',
        'last_login': 'last_login',
        'avatar': 'avatar',
        'avatarfull': 'avatarfull'
    }

    def __init__(self, account_id=None, last_played=None, win=None, games=None, with_win=None, with_games=None, against_win=None, against_games=None, with_gpm_sum=None, with_xpm_sum=None, personaname=None, name=None, is_contributor=None, last_login=None, avatar=None, avatarfull=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._last_played = None
        self._win = None
        self._games = None
        self._with_win = None
        self._with_games = None
        self._against_win = None
        self._against_games = None
        self._with_gpm_sum = None
        self._with_xpm_sum = None
        self._personaname = None
        self._name = None
        self._is_contributor = None
        self._last_login = None
        self._avatar = None
        self._avatarfull = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if last_played is not None:
            self.last_played = last_played
        if win is not None:
            self.win = win
        if games is not None:
            self.games = games
        if with_win is not None:
            self.with_win = with_win
        if with_games is not None:
            self.with_games = with_games
        if against_win is not None:
            self.against_win = against_win
        if against_games is not None:
            self.against_games = against_games
        if with_gpm_sum is not None:
            self.with_gpm_sum = with_gpm_sum
        if with_xpm_sum is not None:
            self.with_xpm_sum = with_xpm_sum
        if personaname is not None:
            self.personaname = personaname
        if name is not None:
            self.name = name
        if is_contributor is not None:
            self.is_contributor = is_contributor
        if last_login is not None:
            self.last_login = last_login
        if avatar is not None:
            self.avatar = avatar
        if avatarfull is not None:
            self.avatarfull = avatarfull

    @property
    def account_id(self):
        """Gets the account_id of this InlineResponse2007.  # noqa: E501

        account_id  # noqa: E501

        :return: The account_id of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InlineResponse2007.

        account_id  # noqa: E501

        :param account_id: The account_id of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def last_played(self):
        """Gets the last_played of this InlineResponse2007.  # noqa: E501

        last_played  # noqa: E501

        :return: The last_played of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._last_played

    @last_played.setter
    def last_played(self, last_played):
        """Sets the last_played of this InlineResponse2007.

        last_played  # noqa: E501

        :param last_played: The last_played of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._last_played = last_played

    @property
    def win(self):
        """Gets the win of this InlineResponse2007.  # noqa: E501

        win  # noqa: E501

        :return: The win of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._win

    @win.setter
    def win(self, win):
        """Sets the win of this InlineResponse2007.

        win  # noqa: E501

        :param win: The win of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._win = win

    @property
    def games(self):
        """Gets the games of this InlineResponse2007.  # noqa: E501

        games  # noqa: E501

        :return: The games of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this InlineResponse2007.

        games  # noqa: E501

        :param games: The games of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._games = games

    @property
    def with_win(self):
        """Gets the with_win of this InlineResponse2007.  # noqa: E501

        with_win  # noqa: E501

        :return: The with_win of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._with_win

    @with_win.setter
    def with_win(self, with_win):
        """Sets the with_win of this InlineResponse2007.

        with_win  # noqa: E501

        :param with_win: The with_win of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._with_win = with_win

    @property
    def with_games(self):
        """Gets the with_games of this InlineResponse2007.  # noqa: E501

        with_games  # noqa: E501

        :return: The with_games of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._with_games

    @with_games.setter
    def with_games(self, with_games):
        """Sets the with_games of this InlineResponse2007.

        with_games  # noqa: E501

        :param with_games: The with_games of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._with_games = with_games

    @property
    def against_win(self):
        """Gets the against_win of this InlineResponse2007.  # noqa: E501

        against_win  # noqa: E501

        :return: The against_win of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._against_win

    @against_win.setter
    def against_win(self, against_win):
        """Sets the against_win of this InlineResponse2007.

        against_win  # noqa: E501

        :param against_win: The against_win of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._against_win = against_win

    @property
    def against_games(self):
        """Gets the against_games of this InlineResponse2007.  # noqa: E501

        against_games  # noqa: E501

        :return: The against_games of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._against_games

    @against_games.setter
    def against_games(self, against_games):
        """Sets the against_games of this InlineResponse2007.

        against_games  # noqa: E501

        :param against_games: The against_games of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._against_games = against_games

    @property
    def with_gpm_sum(self):
        """Gets the with_gpm_sum of this InlineResponse2007.  # noqa: E501

        with_gpm_sum  # noqa: E501

        :return: The with_gpm_sum of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._with_gpm_sum

    @with_gpm_sum.setter
    def with_gpm_sum(self, with_gpm_sum):
        """Sets the with_gpm_sum of this InlineResponse2007.

        with_gpm_sum  # noqa: E501

        :param with_gpm_sum: The with_gpm_sum of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._with_gpm_sum = with_gpm_sum

    @property
    def with_xpm_sum(self):
        """Gets the with_xpm_sum of this InlineResponse2007.  # noqa: E501

        with_xpm_sum  # noqa: E501

        :return: The with_xpm_sum of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._with_xpm_sum

    @with_xpm_sum.setter
    def with_xpm_sum(self, with_xpm_sum):
        """Sets the with_xpm_sum of this InlineResponse2007.

        with_xpm_sum  # noqa: E501

        :param with_xpm_sum: The with_xpm_sum of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._with_xpm_sum = with_xpm_sum

    @property
    def personaname(self):
        """Gets the personaname of this InlineResponse2007.  # noqa: E501

        personaname  # noqa: E501

        :return: The personaname of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """Sets the personaname of this InlineResponse2007.

        personaname  # noqa: E501

        :param personaname: The personaname of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._personaname = personaname

    @property
    def name(self):
        """Gets the name of this InlineResponse2007.  # noqa: E501

        name  # noqa: E501

        :return: The name of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2007.

        name  # noqa: E501

        :param name: The name of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_contributor(self):
        """Gets the is_contributor of this InlineResponse2007.  # noqa: E501

        is_contributor  # noqa: E501

        :return: The is_contributor of this InlineResponse2007.  # noqa: E501
        :rtype: bool
        """
        return self._is_contributor

    @is_contributor.setter
    def is_contributor(self, is_contributor):
        """Sets the is_contributor of this InlineResponse2007.

        is_contributor  # noqa: E501

        :param is_contributor: The is_contributor of this InlineResponse2007.  # noqa: E501
        :type: bool
        """

        self._is_contributor = is_contributor

    @property
    def last_login(self):
        """Gets the last_login of this InlineResponse2007.  # noqa: E501

        last_login  # noqa: E501

        :return: The last_login of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this InlineResponse2007.

        last_login  # noqa: E501

        :param last_login: The last_login of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._last_login = last_login

    @property
    def avatar(self):
        """Gets the avatar of this InlineResponse2007.  # noqa: E501

        avatar  # noqa: E501

        :return: The avatar of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this InlineResponse2007.

        avatar  # noqa: E501

        :param avatar: The avatar of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def avatarfull(self):
        """Gets the avatarfull of this InlineResponse2007.  # noqa: E501

        avatarfull  # noqa: E501

        :return: The avatarfull of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._avatarfull

    @avatarfull.setter
    def avatarfull(self, avatarfull):
        """Sets the avatarfull of this InlineResponse2007.

        avatarfull  # noqa: E501

        :param avatarfull: The avatarfull of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._avatarfull = avatarfull

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
