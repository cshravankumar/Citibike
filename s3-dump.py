import json
import urllib
import boto3
import time

url = "https://feeds.citibikenyc.com/stations/stations.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
data = json.dumps(data)
# print(data)
# some_binary_data = b'Here we have some data'
# more_binary_data = b'Here we have some more data
s3 = boto3.resource('s3')
str = str(int(time.time())) + ".json"
object = s3.Object('citibike-bucket', str)
#assert isinstance(data, object)
object.put(Body=data)