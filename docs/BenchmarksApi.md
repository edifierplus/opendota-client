# opendota_client.BenchmarksApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**benchmarks_get**](BenchmarksApi.md#benchmarks_get) | **GET** /benchmarks | GET /benchmarks


# **benchmarks_get**
> InlineResponse20022 benchmarks_get(hero_id)

GET /benchmarks

Benchmarks of average stat values for a hero

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.BenchmarksApi()
hero_id = 'hero_id_example' # str | Hero ID

try:
    # GET /benchmarks
    api_response = api_instance.benchmarks_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->benchmarks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **str**| Hero ID | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

