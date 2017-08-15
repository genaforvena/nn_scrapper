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

import decimal

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += jump

for i in drange(56.099482, 56.50298, 0.05):
	for j in drange(43.714302, 44.305771, 0.05):
		venuesJson = requestWithAccessToken("venues/search", "ll=" + str(i) + "," + str(j) + "&intent=checkin&radius=10000")
		venues = venues + venuesJson["response"]["venues"] 

with open("venues.json", "w+") as out:
	json.dump(venues, out)