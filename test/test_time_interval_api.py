# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mint_client
from mint_client.api.time_interval_api import TimeIntervalApi  # noqa: E501
from mint_client.rest import ApiException


class TestTimeIntervalApi(unittest.TestCase):
    """TimeIntervalApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.time_interval_api.TimeIntervalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_timeintervals_get(self):
        """Test case for timeintervals_get

        List all TimeInterval entities  # noqa: E501
        """
        pass

    def test_timeintervals_id_delete(self):
        """Test case for timeintervals_id_delete

        Delete a TimeInterval  # noqa: E501
        """
        pass

    def test_timeintervals_id_get(self):
        """Test case for timeintervals_id_get

        Get a TimeInterval  # noqa: E501
        """
        pass

    def test_timeintervals_id_put(self):
        """Test case for timeintervals_id_put

        Update a TimeInterval  # noqa: E501
        """
        pass

    def test_timeintervals_post(self):
        """Test case for timeintervals_post

        Create a TimeInterval  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()