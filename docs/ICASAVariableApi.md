# mint_client.ICASAVariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**icasavariables_get**](ICASAVariableApi.md#icasavariables_get) | **GET** /icasavariables | List all ICASAVariable entities
[**icasavariables_id_delete**](ICASAVariableApi.md#icasavariables_id_delete) | **DELETE** /icasavariables/{id} | Delete a ICASAVariable
[**icasavariables_id_get**](ICASAVariableApi.md#icasavariables_id_get) | **GET** /icasavariables/{id} | Get a ICASAVariable
[**icasavariables_id_put**](ICASAVariableApi.md#icasavariables_id_put) | **PUT** /icasavariables/{id} | Update a ICASAVariable
[**icasavariables_post**](ICASAVariableApi.md#icasavariables_post) | **POST** /icasavariables | Create a ICASAVariable


# **icasavariables_get**
> list[ICASAVariable] icasavariables_get(username=username)

List all ICASAVariable entities

Gets a list of all ICASAVariable entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ICASAVariableApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all ICASAVariable entities
    api_response = api_instance.icasavariables_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ICASAVariableApi->icasavariables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[ICASAVariable]**](ICASAVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icasavariables_id_delete**
> icasavariables_id_delete(id, user)

Delete a ICASAVariable

Delete an existing ICASAVariable

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
api_instance = mint_client.ICASAVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a ICASAVariable
    api_instance.icasavariables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ICASAVariableApi->icasavariables_id_delete: %s\n" % e)
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

# **icasavariables_id_get**
> ICASAVariable icasavariables_id_get(id, username=username)

Get a ICASAVariable

Gets the details of a single instance of a ICASAVariable

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ICASAVariableApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a ICASAVariable
    api_response = api_instance.icasavariables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ICASAVariableApi->icasavariables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**ICASAVariable**](ICASAVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icasavariables_id_put**
> icasavariables_id_put(id, user, icasa_variable=icasa_variable)

Update a ICASAVariable

Updates an existing ICASAVariable

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
api_instance = mint_client.ICASAVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
icasa_variable = mint_client.ICASAVariable() # ICASAVariable | An old ICASAVariableto be updated (optional)

try:
    # Update a ICASAVariable
    api_instance.icasavariables_id_put(id, user, icasa_variable=icasa_variable)
except ApiException as e:
    print("Exception when calling ICASAVariableApi->icasavariables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **icasa_variable** | [**ICASAVariable**](ICASAVariable.md)| An old ICASAVariableto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icasavariables_post**
> icasavariables_post(user, icasa_variable=icasa_variable)

Create a ICASAVariable

Create a new instance of a ICASAVariable

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
api_instance = mint_client.ICASAVariableApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
icasa_variable = mint_client.ICASAVariable() # ICASAVariable | A new ICASAVariableto be created (optional)

try:
    # Create a ICASAVariable
    api_instance.icasavariables_post(user, icasa_variable=icasa_variable)
except ApiException as e:
    print("Exception when calling ICASAVariableApi->icasavariables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **icasa_variable** | [**ICASAVariable**](ICASAVariable.md)| A new ICASAVariableto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
