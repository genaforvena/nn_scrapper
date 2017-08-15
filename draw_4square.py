import gmplot
import json
import collections
from operator import attrgetter

nn_lat = 56.296504
nn_lng = 43.936059
apikey = "AIzaSyAEHGhDzMntd_QXMYR_ZbrOSq7iHMW3d94"

with open('venues.json', 'r') as f:
    data = json.load(f)

Venue = collections.namedtuple('Venue', 'name lat lng checkins')

venues = list(set([Venue(name = x['name'], lat = x['location']['lat'], lng = x['location']['lng'], checkins = x['stats']['checkinsCount']) for x in data]))

sortedVenues = sorted(venues, key=attrgetter('checkins'), reverse = True)

print(sortedVenues[:100])

gmap = gmplot.GoogleMapPlotter(nn_lat, nn_lng, 13)

for venue in sortedVenues:
    gmap.circle(venue.lat, venue.lng, radius = venue.checkins * 0.01, color = "#660066")

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

# replace("map.html", '<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false"></script>', '<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false&key=' + apikey + '"></script>')

