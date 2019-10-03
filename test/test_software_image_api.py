# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.software_image_api import SoftwareImageApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestSoftwareImageApi(unittest.TestCase):
    """SoftwareImageApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.software_image_api.SoftwareImageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_softwareimages_get(self):
        """Test case for softwareimages_get

        List all SoftwareImage entities  # noqa: E501
        """
        pass

    def test_softwareimages_id_delete(self):
        """Test case for softwareimages_id_delete

        Delete a SoftwareImage  # noqa: E501
        """
        pass

    def test_softwareimages_id_get(self):
        """Test case for softwareimages_id_get

        Get a SoftwareImage  # noqa: E501
        """
        pass

    def test_softwareimages_id_put(self):
        """Test case for softwareimages_id_put

        Update a SoftwareImage  # noqa: E501
        """
        pass

    def test_softwareimages_post(self):
        """Test case for softwareimages_post

        Create a SoftwareImage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
