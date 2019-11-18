# coding: utf-8

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.2.0/index-en.html](https://w3id.org/okn/o/sdm)  # noqa: E501

    OpenAPI spec version: v1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.subsidy_api import SubsidyApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestSubsidyApi(unittest.TestCase):
    """SubsidyApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.subsidy_api.SubsidyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_subsidys_get(self):
        """Test case for subsidys_get

        List all Subsidy entities  # noqa: E501
        """
        pass

    def test_subsidys_id_delete(self):
        """Test case for subsidys_id_delete

        Delete a Subsidy  # noqa: E501
        """
        pass

    def test_subsidys_id_get(self):
        """Test case for subsidys_id_get

        Get a Subsidy  # noqa: E501
        """
        pass

    def test_subsidys_id_put(self):
        """Test case for subsidys_id_put

        Update a Subsidy  # noqa: E501
        """
        pass

    def test_subsidys_post(self):
        """Test case for subsidys_post

        Create a Subsidy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
