#!/usr/bin/python
# json.load()  reads json from a file
# json.loads() reads json from a string
import json
with open('data.json') as parks_file:    
    parks = json.load(parks_file)

for i in range(0,3):
    print "---------------"
    print parks[i]['id']
    print parks[i]['name']
    print parks[i]['website']
    print parks[i]['location_1']['latitude']
    print parks[i]['location_1']['longitude']

    # the address is stored as a string and needs to 
    # be converted into json
    address = json.loads(parks[i]['location_1']['human_address'])
    print address['address']
    print address['city']
    print address['state']
    print address['zip']
