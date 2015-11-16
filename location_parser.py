import os
import commands
import json
from geopy.geocoders import Nominatim

#Get all of the hourly tweet files
file_list=[]
twitter_directory="~/Desktop/tweets/"

for files in os.listdir(twitter_directory):
    if files.startswith('deflategate'):
        file_list.append(files)

#Now get addresses for all of the tweets
geolocator = Nominatim()
for item in file_list:
    filename=item
    fileopen=open(filename, "r")
    file_length=commands.getoutput(''.join("wc -l " + filename + " | awk '{print $1}'"))
    lines=fileopen.readlines()
    for n in range(0, int(file_length)):
        if lines[n] != "\n":
            json_string=lines[n]
            try:
                parsed_json=json.loads(json_string)
            except ValueError:
                continue   
            try:
                if parsed_json['coordinates']:
                    gpslocation=parsed_json['coordinates'].values()[1]
                    latitude=gpslocation[1]
                    longitude=gpslocation[0]
                    coordinates=''.join(str(latitude) + ', ' + str(longitude))
                    location = geolocator.reverse(coordinates, timeout=10)
                    try:
                        print location.address, latitude
                    except UnicodeEncodeError:
                        pass
            except (TypeError, KeyError):
                continue
        
