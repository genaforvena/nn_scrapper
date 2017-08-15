import urllib.request
import json

access_token = "265791501.a4af066.f45a9f44719a4b2cb2d137118524e32b"
api_url = "https://api.instagram.com/v1"
nn_lat = 56.296504
nn_lng = 43.936059

def request(endpoint, req_params = ""):
    req = api_url + endpoint + "?access_token=" + access_token + "&" + req_params
    print(req)
    raw_response = urllib.request.urlopen(req).read()
    return json.loads(raw_response.decode('utf8'))

locations = request("/locations/search", "lat=" + str(nn_lat) + "&lng=" + str(nn_lng))["data"]

print(locations)

for location in locations:
    location_id = location["id"]
    location_media = request("/locations/" + str(location_id) + "/media/recent")
    print(location_media)

