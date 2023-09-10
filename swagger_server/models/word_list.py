# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

import util
from models.base_model_ import Model


class WordList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, words: List[str]=None):  # noqa: E501
        """WordList - a model defined in Swagger

        :param words: The words of this WordList.  # noqa: E501
        :type words: List[str]
        """
        self.swagger_types = {
            'words': List[str]
        }

        self.attribute_map = {
            'words': 'words'
        }
        self._words = words

    @classmethod
    def from_dict(cls, dikt) -> 'WordList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The word_list of this WordList.  # noqa: E501
        :rtype: WordList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def words(self) -> List[str]:
        """Gets the words of this WordList.

        array or words  # noqa: E501

        :return: The words of this WordList.
        :rtype: List[str]
        """
        return self._words

    @words.setter
    def words(self, words: List[str]):
        """Sets the words of this WordList.

        array or words  # noqa: E501

        :param words: The words of this WordList.
        :type words: List[str]
        """

        self._words = words