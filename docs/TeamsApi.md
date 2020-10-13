# opendota_client.TeamsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_get**](TeamsApi.md#teams_get) | **GET** /teams | GET /teams
[**teams_team_id_get**](TeamsApi.md#teams_team_id_get) | **GET** /teams/{team_id} | GET /teams/{team_id}
[**teams_team_id_heroes_get**](TeamsApi.md#teams_team_id_heroes_get) | **GET** /teams/{team_id}/heroes | GET /teams/{team_id}/heroes
[**teams_team_id_matches_get**](TeamsApi.md#teams_team_id_matches_get) | **GET** /teams/{team_id}/matches | GET /teams/{team_id}/matches
[**teams_team_id_players_get**](TeamsApi.md#teams_team_id_players_get) | **GET** /teams/{team_id}/players | GET /teams/{team_id}/players


# **teams_get**
> list[InlineResponse20029] teams_get()

GET /teams

Get team data

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.TeamsApi()

try:
    # GET /teams
    api_response = api_instance.teams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20029]**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_team_id_get**
> InlineResponse20029 teams_team_id_get(team_id)

GET /teams/{team_id}

Get data for a team

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.TeamsApi()
team_id = 56 # int | Team ID

try:
    # GET /teams/{team_id}
    api_response = api_instance.teams_team_id_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_team_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_team_id_heroes_get**
> InlineResponse20031 teams_team_id_heroes_get(team_id)

GET /teams/{team_id}/heroes

Get heroes for a team

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.TeamsApi()
team_id = 56 # int | Team ID

try:
    # GET /teams/{team_id}/heroes
    api_response = api_instance.teams_team_id_heroes_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_team_id_heroes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_team_id_matches_get**
> InlineResponse20015 teams_team_id_matches_get(team_id)

GET /teams/{team_id}/matches

Get matches for a team

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.TeamsApi()
team_id = 56 # int | Team ID

try:
    # GET /teams/{team_id}/matches
    api_response = api_instance.teams_team_id_matches_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_team_id_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_team_id_players_get**
> InlineResponse20030 teams_team_id_players_get(team_id)

GET /teams/{team_id}/players

Get players who have played for a team

### Example
```python
from __future__ import print_function
import time
import opendota_client
from opendota_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendota_client.TeamsApi()
team_id = 56 # int | Team ID

try:
    # GET /teams/{team_id}/players
    api_response = api_instance.teams_team_id_players_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_team_id_players_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

