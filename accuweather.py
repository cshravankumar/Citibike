import json
import time
import ast
from six.moves import urllib
API = 'D0E2WtXZg1W8cytlWE29Q3GAuLX3qxDF'

def get_location(api, pincode):
    url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=%s&q=%s' % (api, pincode)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', "Python client")
    resp = urllib.request.urlopen(req)
    data = resp.read().decode("utf-8")
    loaded_json = json.loads(data)
    return(loaded_json[0]['Key']) 

def get_weather(api, location_id):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', "Python client")
    resp = urllib.request.urlopen(req)
    data = resp.read().decode()
    loaded_json = json.loads(data)
    return (loaded_json[0]['RealFeelTemperature']['Imperial']['Value'],
            loaded_json[0]['RelativeHumidity'],
            loaded_json[0]['Wind']['Direction']['Degrees'],
            loaded_json[0]['Wind']['Speed']['Imperial']['Value'],
            loaded_json[0]['UVIndex'],
           loaded_json[0]['CloudCover'],
            loaded_json[0]['Pressure']['Metric']['Value'],
           loaded_json[0]['Precip1hr']['Metric']['Value'],
           loaded_json)
#timestamp = time.time()
LOCATION_ID =get_location(API, "10025")
#temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw = get_weather(API, LOCATION_ID)
#print(temperature)