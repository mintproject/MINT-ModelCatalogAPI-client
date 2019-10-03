# mint_client.SoftwareApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwares_get**](SoftwareApi.md#softwares_get) | **GET** /softwares | List all Software entities
[**softwares_id_delete**](SoftwareApi.md#softwares_id_delete) | **DELETE** /softwares/{id} | Delete a Software
[**softwares_id_get**](SoftwareApi.md#softwares_id_get) | **GET** /softwares/{id} | Get a Software
[**softwares_id_put**](SoftwareApi.md#softwares_id_put) | **PUT** /softwares/{id} | Update a Software
[**softwares_post**](SoftwareApi.md#softwares_post) | **POST** /softwares | Create a Software


# **softwares_get**
> list[Software] softwares_get(username=username)

List all Software entities

Gets a list of all Software entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SoftwareApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Software entities
    api_response = api_instance.softwares_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Software]**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwares_id_delete**
> softwares_id_delete(id, user)

Delete a Software

Delete an existing Software

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
api_instance = mint_client.SoftwareApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Software
    api_instance.softwares_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_delete: %s\n" % e)
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

# **softwares_id_get**
> Software softwares_id_get(id, username=username)

Get a Software

Gets the details of a single instance of a Software

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SoftwareApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Software
    api_response = api_instance.softwares_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Software**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwares_id_put**
> softwares_id_put(id, user, software=software)

Update a Software

Updates an existing Software

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
api_instance = mint_client.SoftwareApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
software = mint_client.Software() # Software | An old Softwareto be updated (optional)

try:
    # Update a Software
    api_instance.softwares_id_put(id, user, software=software)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **software** | [**Software**](Software.md)| An old Softwareto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwares_post**
> softwares_post(user, software=software)

Create a Software

Create a new instance of a Software

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
api_instance = mint_client.SoftwareApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
software = mint_client.Software() # Software | A new Softwareto be created (optional)

try:
    # Create a Software
    api_instance.softwares_post(user, software=software)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software** | [**Software**](Software.md)| A new Softwareto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
