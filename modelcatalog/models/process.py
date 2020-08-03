# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Process(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'influences': 'list[Process]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'influences': 'influences',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, influences=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """Process - a model defined in OpenAPI"""  # noqa: E501

        self._influences = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.influences = influences
        self.description = description
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def influences(self):
        """Gets the influences of this Process.  # noqa: E501

        Property that captures if a physical process influences another process  # noqa: E501

        :return: The influences of this Process.  # noqa: E501
        :rtype: list[Process]
        """
        return self._influences

    @influences.setter
    def influences(self, influences):
        """Sets the influences of this Process.

        Property that captures if a physical process influences another process  # noqa: E501

        :param influences: The influences of this Process.  # noqa: E501
        :type: list[Process]
        """

        self._influences = influences

    @property
    def description(self):
        """Gets the description of this Process.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Process.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Process.

        small description  # noqa: E501

        :param description: The description of this Process.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Process.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Process.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Process.

        identifier  # noqa: E501

        :param id: The id of this Process.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Process.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Process.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Process.

        short description of the resource  # noqa: E501

        :param label: The label of this Process.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Process.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Process.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Process.

        type of the resource  # noqa: E501

        :param type: The type of this Process.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Process):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
