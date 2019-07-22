# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about     Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: mosorio@isi.edu
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mint_client.api_client import ApiClient
from mint_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ModelversionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_model_version(self, model_version, **kwargs):  # noqa: E501
        """Create a ModelVersion  # noqa: E501

        Creates a new instance of a `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_model_version(model_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelVersion model_version: A new `ModelVersion` to be created. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_model_version_with_http_info(model_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_model_version_with_http_info(model_version, **kwargs)  # noqa: E501
            return data

    def create_model_version_with_http_info(self, model_version, **kwargs):  # noqa: E501
        """Create a ModelVersion  # noqa: E501

        Creates a new instance of a `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_model_version_with_http_info(model_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelVersion model_version: A new `ModelVersion` to be created. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['model_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_model_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_version' is set
        if ('model_version' not in local_var_params or
                local_var_params['model_version'] is None):
            raise ApiValueError("Missing the required parameter `model_version` when calling `create_model_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model_version' in local_var_params:
            body_params = local_var_params['model_version']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/modelversions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_model_version(self, id, **kwargs):  # noqa: E501
        """Delete a ModelVersion  # noqa: E501

        Deletes an existing `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_model_version(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_model_version_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_model_version_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_model_version_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a ModelVersion  # noqa: E501

        Deletes an existing `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_model_version_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_model_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `delete_model_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/modelversion/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_model_version(self, id, **kwargs):  # noqa: E501
        """Get a ModelVersion  # noqa: E501

        Gets the details of a single instance of a `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model_version(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: ModelVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_model_version_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_model_version_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_model_version_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a ModelVersion  # noqa: E501

        Gets the details of a single instance of a `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model_version_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: ModelVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_model_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `get_model_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/modelversion/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_model_versions(self, **kwargs):  # noqa: E501
        """List All ModelVersions  # noqa: E501

        Gets a list of all `ModelVersion` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model_versions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: list[ModelVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_model_versions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_model_versions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_model_versions_with_http_info(self, **kwargs):  # noqa: E501
        """List All ModelVersions  # noqa: E501

        Gets a list of all `ModelVersion` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model_versions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: list[ModelVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_model_versions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/modelversions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelVersion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_model_version(self, id, model_version, **kwargs):  # noqa: E501
        """Update a ModelVersion  # noqa: E501

        Updates an existing `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model_version(id, model_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param ModelVersion model_version: Updated `ModelVersion` information. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_model_version_with_http_info(id, model_version, **kwargs)  # noqa: E501
        else:
            (data) = self.update_model_version_with_http_info(id, model_version, **kwargs)  # noqa: E501
            return data

    def update_model_version_with_http_info(self, id, model_version, **kwargs):  # noqa: E501
        """Update a ModelVersion  # noqa: E501

        Updates an existing `ModelVersion`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model_version_with_http_info(id, model_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique identifier for a `ModelVersion`. (required)
        :param ModelVersion model_version: Updated `ModelVersion` information. (required)
        :param str username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'model_version', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_model_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `update_model_version`")  # noqa: E501
        # verify the required parameter 'model_version' is set
        if ('model_version' not in local_var_params or
                local_var_params['model_version'] is None):
            raise ApiValueError("Missing the required parameter `model_version` when calling `update_model_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model_version' in local_var_params:
            body_params = local_var_params['model_version']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/modelversion/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
