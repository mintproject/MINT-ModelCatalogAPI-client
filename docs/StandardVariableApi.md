# mint_client.StandardVariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standardvariables_get**](StandardVariableApi.md#standardvariables_get) | **GET** /standardvariables | List all StandardVariable entities
[**standardvariables_id_delete**](StandardVariableApi.md#standardvariables_id_delete) | **DELETE** /standardvariables/{id} | Delete a StandardVariable
[**standardvariables_id_get**](StandardVariableApi.md#standardvariables_id_get) | **GET** /standardvariables/{id} | Get a StandardVariable
[**standardvariables_id_put**](StandardVariableApi.md#standardvariables_id_put) | **PUT** /standardvariables/{id} | Update a StandardVariable
[**standardvariables_post**](StandardVariableApi.md#standardvariables_post) | **POST** /standardvariables | Create a StandardVariable


# **standardvariables_get**
> list[StandardVariable] standardvariables_get(username=username)

List all StandardVariable entities

Gets a list of all StandardVariable entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.StandardVariableApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all StandardVariable entities
    api_response = api_instance.standardvariables_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[StandardVariable]**](StandardVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standardvariables_id_delete**
> standardvariables_id_delete(id, user)

Delete a StandardVariable

Delete an existing StandardVariable

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.StandardVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a StandardVariable
    api_instance.standardvariables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standardvariables_id_get**
> StandardVariable standardvariables_id_get(id, username=username)

Get a StandardVariable

Gets the details of a single instance of a StandardVariable

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.StandardVariableApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a StandardVariable
    api_response = api_instance.standardvariables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**StandardVariable**](StandardVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standardvariables_id_put**
> standardvariables_id_put(id, user, standard_variable=standard_variable)

Update a StandardVariable

Updates an existing StandardVariable

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.StandardVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
standard_variable = mint_client.StandardVariable() # StandardVariable | An old StandardVariableto be updated (optional)

try:
    # Update a StandardVariable
    api_instance.standardvariables_id_put(id, user, standard_variable=standard_variable)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **standard_variable** | [**StandardVariable**](StandardVariable.md)| An old StandardVariableto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standardvariables_post**
> standardvariables_post(user, standard_variable=standard_variable)

Create a StandardVariable

Create a new instance of a StandardVariable

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.StandardVariableApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
standard_variable = mint_client.StandardVariable() # StandardVariable | A new StandardVariableto be created (optional)

try:
    # Create a StandardVariable
    api_instance.standardvariables_post(user, standard_variable=standard_variable)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **standard_variable** | [**StandardVariable**](StandardVariable.md)| A new StandardVariableto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
