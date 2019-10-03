# mint_client.ImageApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_get**](ImageApi.md#images_get) | **GET** /images | List all Image entities
[**images_id_delete**](ImageApi.md#images_id_delete) | **DELETE** /images/{id} | Delete a Image
[**images_id_get**](ImageApi.md#images_id_get) | **GET** /images/{id} | Get a Image
[**images_id_put**](ImageApi.md#images_id_put) | **PUT** /images/{id} | Update a Image
[**images_post**](ImageApi.md#images_post) | **POST** /images | Create a Image


# **images_get**
> list[Image] images_get(username=username)

List all Image entities

Gets a list of all Image entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ImageApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Image entities
    api_response = api_instance.images_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_id_delete**
> images_id_delete(id, user)

Delete a Image

Delete an existing Image

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
api_instance = mint_client.ImageApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Image
    api_instance.images_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_delete: %s\n" % e)
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

# **images_id_get**
> Image images_id_get(id, username=username)

Get a Image

Gets the details of a single instance of a Image

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ImageApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Image
    api_response = api_instance.images_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_id_put**
> images_id_put(id, user, image=image)

Update a Image

Updates an existing Image

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
api_instance = mint_client.ImageApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
image = mint_client.Image() # Image | An old Imageto be updated (optional)

try:
    # Update a Image
    api_instance.images_id_put(id, user, image=image)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **image** | [**Image**](Image.md)| An old Imageto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_post**
> images_post(user, image=image)

Create a Image

Create a new instance of a Image

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
api_instance = mint_client.ImageApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
image = mint_client.Image() # Image | A new Imageto be created (optional)

try:
    # Create a Image
    api_instance.images_post(user, image=image)
except ApiException as e:
    print("Exception when calling ImageApi->images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **image** | [**Image**](Image.md)| A new Imageto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
