# opendota_client.HeroesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroes_get**](HeroesApi.md#heroes_get) | **GET** /heroes | GET /heroes
[**heroes_hero_id_durations_get**](HeroesApi.md#heroes_hero_id_durations_get) | **GET** /heroes/{hero_id}/durations | GET /heroes/{hero_id}/durations
[**heroes_hero_id_item_popularity_get**](HeroesApi.md#heroes_hero_id_item_popularity_get) | **GET** /heroes/{hero_id}/itemPopularity | GET /heroes/{hero_id}/itemPopularity
[**heroes_hero_id_matches_get**](HeroesApi.md#heroes_hero_id_matches_get) | **GET** /heroes/{hero_id}/matches | GET /heroes/{hero_id}/matches
[**heroes_hero_id_matchups_get**](HeroesApi.md#heroes_hero_id_matchups_get) | **GET** /heroes/{hero_id}/matchups | GET /heroes/{hero_id}/matchups
[**heroes_hero_id_players_get**](HeroesApi.md#heroes_hero_id_players_get) | **GET** /heroes/{hero_id}/players | GET /heroes/{hero_id}/players


# **heroes_get**
> list[InlineResponse20023] heroes_get()

GET /heroes

Get hero data

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()

try:
    # GET /heroes
    api_response = api_instance.heroes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_durations_get**
> list[InlineResponse20026] heroes_hero_id_durations_get(hero_id)

GET /heroes/{hero_id}/durations

Get hero performance over a range of match durations

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()
hero_id = 56 # int | Hero ID

try:
    # GET /heroes/{hero_id}/durations
    api_response = api_instance.heroes_hero_id_durations_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_durations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID | 

### Return type

[**list[InlineResponse20026]**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_item_popularity_get**
> InlineResponse20027 heroes_hero_id_item_popularity_get(hero_id)

GET /heroes/{hero_id}/itemPopularity

Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()
hero_id = 56 # int | Hero ID

try:
    # GET /heroes/{hero_id}/itemPopularity
    api_response = api_instance.heroes_hero_id_item_popularity_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_item_popularity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_matches_get**
> list[InlineResponse20015] heroes_hero_id_matches_get(hero_id)

GET /heroes/{hero_id}/matches

Get recent matches with a hero

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()
hero_id = 56 # int | Hero ID

try:
    # GET /heroes/{hero_id}/matches
    api_response = api_instance.heroes_hero_id_matches_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID | 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_matchups_get**
> list[InlineResponse20025] heroes_hero_id_matchups_get(hero_id)

GET /heroes/{hero_id}/matchups

Get results against other heroes for a hero

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()
hero_id = 56 # int | Hero ID

try:
    # GET /heroes/{hero_id}/matchups
    api_response = api_instance.heroes_hero_id_matchups_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_matchups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID | 

### Return type

[**list[InlineResponse20025]**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_players_get**
> list[list[object]] heroes_hero_id_players_get(hero_id)

GET /heroes/{hero_id}/players

Get players who have played this hero

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.HeroesApi()
hero_id = 56 # int | Hero ID

try:
    # GET /heroes/{hero_id}/players
    api_response = api_instance.heroes_hero_id_players_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_players_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID | 

### Return type

**list[list[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

