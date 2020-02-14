# modelcatalog.RegionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regions_get**](RegionApi.md#regions_get) | **GET** /regions | List all Region entities
[**regions_id_delete**](RegionApi.md#regions_id_delete) | **DELETE** /regions/{id} | Delete a Region
[**regions_id_get**](RegionApi.md#regions_id_get) | **GET** /regions/{id} | Get a Region
[**regions_id_put**](RegionApi.md#regions_id_put) | **PUT** /regions/{id} | Update a Region
[**regions_post**](RegionApi.md#regions_post) | **POST** /regions | Create a Region


# **regions_get**
> list[Region] regions_get(username=username, label=label)

List all Region entities

Gets a list of all Region entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.RegionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Region entities
    api_response = api_instance.regions_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_id_delete**
> regions_id_delete(id, user)

Delete a Region

Delete an existing Region

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Region
    api_instance.regions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_id_get**
> Region regions_id_get(id, username=username)

Get a Region

Gets the details of a single instance of a Region

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.RegionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Region
    api_response = api_instance.regions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_id_put**
> Region regions_id_put(id, user, region=region)

Update a Region

Updates an existing Region

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
region = modelcatalog.Region() # Region | An old Regionto be updated (optional)

try:
    # Update a Region
    api_response = api_instance.regions_id_put(id, user, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **region** | [**Region**](Region.md)| An old Regionto be updated | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_post**
> Region regions_post(user, region=region)

Create a Region

Create a new instance of a Region

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
region = modelcatalog.Region() # Region | A new Regionto be created (optional)

try:
    # Create a Region
    api_response = api_instance.regions_post(user, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **region** | [**Region**](Region.md)| A new Regionto be created | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)
