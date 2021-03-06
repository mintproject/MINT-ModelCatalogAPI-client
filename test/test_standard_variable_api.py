# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.standard_variable_api import StandardVariableApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestStandardVariableApi(unittest.TestCase):
    """StandardVariableApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.standard_variable_api.StandardVariableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_standardvariables_get(self):
        """Test case for standardvariables_get

        List all instances of StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_id_delete(self):
        """Test case for standardvariables_id_delete

        Delete an existing StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_id_get(self):
        """Test case for standardvariables_id_get

        Get a single StandardVariable by its id  # noqa: E501
        """
        pass

    def test_standardvariables_id_put(self):
        """Test case for standardvariables_id_put

        Update an existing StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_post(self):
        """Test case for standardvariables_post

        Create one StandardVariable  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
