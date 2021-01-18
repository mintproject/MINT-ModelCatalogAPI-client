# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SampleCollection(object):
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
        'data_catalog_identifier': 'list[str]',
        'has_part': 'list[SampleResource]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'value': 'list[object]'
    }

    attribute_map = {
        'data_catalog_identifier': 'dataCatalogIdentifier',
        'has_part': 'hasPart',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, data_catalog_identifier=None, has_part=None, description=None, id=None, label=None, type=None, value=None):  # noqa: E501
        """SampleCollection - a model defined in OpenAPI"""  # noqa: E501

        self._data_catalog_identifier = None
        self._has_part = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.data_catalog_identifier = data_catalog_identifier
        self.has_part = has_part
        self.description = description
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.value = value

    @property
    def data_catalog_identifier(self):
        """Gets the data_catalog_identifier of this SampleCollection.  # noqa: E501

        An identifier for resources with metadata entries in a data catalog  # noqa: E501

        :return: The data_catalog_identifier of this SampleCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_catalog_identifier

    @data_catalog_identifier.setter
    def data_catalog_identifier(self, data_catalog_identifier):
        """Sets the data_catalog_identifier of this SampleCollection.

        An identifier for resources with metadata entries in a data catalog  # noqa: E501

        :param data_catalog_identifier: The data_catalog_identifier of this SampleCollection.  # noqa: E501
        :type: list[str]
        """

        self._data_catalog_identifier = data_catalog_identifier

    @property
    def has_part(self):
        """Gets the has_part of this SampleCollection.  # noqa: E501

        Property designed to reference the elements included in a sample collection.  # noqa: E501

        :return: The has_part of this SampleCollection.  # noqa: E501
        :rtype: list[SampleResource]
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this SampleCollection.

        Property designed to reference the elements included in a sample collection.  # noqa: E501

        :param has_part: The has_part of this SampleCollection.  # noqa: E501
        :type: list[SampleResource]
        """

        self._has_part = has_part

    @property
    def description(self):
        """Gets the description of this SampleCollection.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this SampleCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleCollection.

        small description  # noqa: E501

        :param description: The description of this SampleCollection.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this SampleCollection.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this SampleCollection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleCollection.

        identifier  # noqa: E501

        :param id: The id of this SampleCollection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SampleCollection.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this SampleCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SampleCollection.

        short description of the resource  # noqa: E501

        :param label: The label of this SampleCollection.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SampleCollection.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this SampleCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleCollection.

        type of the resource  # noqa: E501

        :param type: The type of this SampleCollection.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this SampleCollection.  # noqa: E501

        Value associated to the described entity  # noqa: E501

        :return: The value of this SampleCollection.  # noqa: E501
        :rtype: list[object]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SampleCollection.

        Value associated to the described entity  # noqa: E501

        :param value: The value of this SampleCollection.  # noqa: E501
        :type: list[object]
        """

        self._value = value

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
        if not isinstance(other, SampleCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
