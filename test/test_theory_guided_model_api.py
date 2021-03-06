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
from modelcatalog.api.theory_guided_model_api import TheoryGuidedModelApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestTheoryGuidedModelApi(unittest.TestCase):
    """TheoryGuidedModelApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.theory_guided_model_api.TheoryGuidedModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_theory_guidedmodels_get(self):
        """Test case for theory_guidedmodels_get

        List all instances of Theory-GuidedModel  # noqa: E501
        """
        pass

    def test_theory_guidedmodels_id_delete(self):
        """Test case for theory_guidedmodels_id_delete

        Delete an existing Theory-GuidedModel  # noqa: E501
        """
        pass

    def test_theory_guidedmodels_id_get(self):
        """Test case for theory_guidedmodels_id_get

        Get a single Theory-GuidedModel by its id  # noqa: E501
        """
        pass

    def test_theory_guidedmodels_id_put(self):
        """Test case for theory_guidedmodels_id_put

        Update an existing Theory-GuidedModel  # noqa: E501
        """
        pass

    def test_theory_guidedmodels_post(self):
        """Test case for theory_guidedmodels_post

        Create one Theory-GuidedModel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
