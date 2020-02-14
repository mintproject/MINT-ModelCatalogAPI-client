# modelcatalog.ModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_model_index_get**](ModelApi.md#custom_model_index_get) | **GET** /custom/model/index | Get a Model
[**custom_model_intervention_get**](ModelApi.md#custom_model_intervention_get) | **GET** /custom/model/intervention | Get a Model
[**custom_model_region_get**](ModelApi.md#custom_model_region_get) | **GET** /custom/model/region | Get a Model
[**models_get**](ModelApi.md#models_get) | **GET** /models | List all Model entities
[**models_id_delete**](ModelApi.md#models_id_delete) | **DELETE** /models/{id} | Delete a Model
[**models_id_get**](ModelApi.md#models_id_get) | **GET** /models/{id} | Get a Model
[**models_id_put**](ModelApi.md#models_id_put) | **PUT** /models/{id} | Update a Model
[**models_post**](ModelApi.md#models_post) | **POST** /models | Create a Model


# **custom_model_index_get**
> list[Model] custom_model_index_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | Label of NumericalIndex
custom_query_name = 'custom_model_index' # str | Name of the custom query (optional) (default to 'custom_model_index')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_index_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Label of NumericalIndex | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_index&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_model_intervention_get**
> list[Model] custom_model_intervention_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | Label of intervation
custom_query_name = 'custom_model_intervetion' # str | Name of the custom query (optional) (default to 'custom_model_intervetion')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_intervention_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_intervention_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Label of intervation | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_intervetion&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_model_region_get**
> list[Model] custom_model_region_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | region to search
custom_query_name = 'custom_model_region' # str | Name of the custom query (optional) (default to 'custom_model_region')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_region_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| region to search | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_region&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_get**
> list[Model] models_get(username=username, label=label)

List all Model entities

Gets a list of all Model entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Model entities
    api_response = api_instance.models_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_id_delete**
> models_id_delete(id, user)

Delete a Model

Delete an existing Model

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Model
    api_instance.models_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_delete: %s\n" % e)
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

# **models_id_get**
> Model models_id_get(id, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.models_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_id_put**
> Model models_id_put(id, user, model=model)

Update a Model

Updates an existing Model

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
model = modelcatalog.Model() # Model | An old Modelto be updated (optional)

try:
    # Update a Model
    api_response = api_instance.models_id_put(id, user, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **model** | [**Model**](Model.md)| An old Modelto be updated | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_post**
> Model models_post(user, model=model)

Create a Model

Create a new instance of a Model

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model = modelcatalog.Model() # Model | A new Modelto be created (optional)

try:
    # Create a Model
    api_response = api_instance.models_post(user, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model** | [**Model**](Model.md)| A new Modelto be created | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)
