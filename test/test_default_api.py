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
from mint_client.api.default_api import DefaultApi  # noqa: E501
from mint_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_login_get(self):
        """Test case for user_login_get

        """
        pass


if __name__ == '__main__':
    unittest.main()