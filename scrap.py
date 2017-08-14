import urllib.request
import json

access_token = "265791501.a4af066.f45a9f44719a4b2cb2d137118524e32b"
api_url = "https://api.instagram.com/v1"

locations_response = urllib.request.urlopen(api_url + "/locations/search?lat=56.296504&lng=43.936059&access_token=" + access_token + "&count=100").read()
locations_json = json.loads(locations_response.decode('utf8'))

print(locations_json)