import urllib.request
import json
import gmplot

access_token = "265791501.a4af066.f45a9f44719a4b2cb2d137118524e32b"
api_url = "https://api.instagram.com/v1"
nn_lat = 56.296504
nn_lng = 43.936059
apikey = "AIzaSyAEHGhDzMntd_QXMYR_ZbrOSq7iHMW3d94"

locations_response = urllib.request.urlopen(api_url + "/locations/search?lat=" + str(nn_lat) + "&lng=" + str(nn_lng) + "&access_token=" + access_token + "&count=100").read()
locations_json = json.loads(locations_response.decode('utf8'))

locations = locations_json["data"]

lats = []
lngs = []

for items in locations:
	lats.append(items["latitude"])
	lngs.append(items["longitude"])

print(lats)

gmap = gmplot.GoogleMapPlotter(nn_lat, nn_lng, 13)
gmap.heatmap(lats, lngs)

gmap.draw("map.html")

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

replace("map.html", '<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false"></script>', '<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false&key=' + apikey + '"></script>')