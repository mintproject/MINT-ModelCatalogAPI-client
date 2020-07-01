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
from modelcatalog.api.sample_execution_api import SampleExecutionApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestSampleExecutionApi(unittest.TestCase):
    """SampleExecutionApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.sample_execution_api.SampleExecutionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sampleexecutions_get(self):
        """Test case for sampleexecutions_get

        List all instances of SampleExecution  # noqa: E501
        """
        pass

    def test_sampleexecutions_id_delete(self):
        """Test case for sampleexecutions_id_delete

        Delete an existing SampleExecution  # noqa: E501
        """
        pass

    def test_sampleexecutions_id_get(self):
        """Test case for sampleexecutions_id_get

        Get a single SampleExecution by its id  # noqa: E501
        """
        pass

    def test_sampleexecutions_id_put(self):
        """Test case for sampleexecutions_id_put

        Update an existing SampleExecution  # noqa: E501
        """
        pass

    def test_sampleexecutions_post(self):
        """Test case for sampleexecutions_post

        Create one SampleExecution  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
