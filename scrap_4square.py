import urllib.request
import json


nn_lat = 56.296504
nn_lng = 43.936059
access_token = "R4VILTNRVMGGE5RLFYTMKV22IA04JEQIL0MELVKXNT1VZSEI"
api_url = "https://api.foursquare.com/v2/"
apikey = "AIzaSyAEHGhDzMntd_QXMYR_ZbrOSq7iHMW3d94"

def requestWithAccessToken(request, params):
	request = api_url + request + "?oauth_token=" + access_token + "&" + params + "&v=20170810&m=foursquare"
	print(request)
	response = urllib.request.urlopen(request).read()
	return json.loads(response.decode('utf8'))

venues = []

delta = -0.1
for i in range(200):
	venuesJson = requestWithAccessToken("venues/search", "ll=" + str(nn_lat + delta) + "," + str(nn_lng) + "&intent=checkin&radius=10000")
	venues = venues + venuesJson["response"]["venues"] 
	delta = delta + 0.01

delta = -0.1
for i in range(200):
	venuesJson = requestWithAccessToken("venues/search", "ll=" + str(nn_lat ) + "," + str(nn_lng + delta) + "&intent=checkin&radius=10000")
	venues = venues + venuesJson["response"]["venues"] 
	delta = delta + 0.01

with open("venues.json", "w+") as out:
	json.dump(venues, out)