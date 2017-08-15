import urllib.request
import json


nn_lat = 56.296504
nn_lng = 43.936059
access_token = "R4VILTNRVMGGE5RLFYTMKV22IA04JEQIL0MELVKXNT1VZSEI"
api_url = "https://api.foursquare.com/v2/"

def requestWithAccessToken(request, params):
	request = api_url + request + "?oauth_token=" + access_token + "&" + params + "&v=20170810&m=foursquare"
	print(request)
	response = urllib.request.urlopen(request).read()
	return json.loads(response.decode('utf8'))

venues = []

delta_x = -0.3
delta_y = -0.3
for i in range(20):
	for j in range(20):
		venuesJson = requestWithAccessToken("venues/search", "ll=" + str(nn_lat + delta_x) + "," + str(nn_lng + delta_y) + "&intent=checkin&radius=10000")
		venues = venues + venuesJson["response"]["venues"] 
		delta_y = delta_y + 0.05
	delta_x = delta_x + 0.05

with open("venues.json", "w+") as out:
	json.dump(venues, out)