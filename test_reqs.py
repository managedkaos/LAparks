#!/usr/bin/python
import json
import requests

url = "https://data.lacounty.gov/resource/u2yw-tuvv.json"

querystring = {"category2":"Parks and Gardens"}

headers = { 'accept': "application/json" } 

response = requests.request("GET", url, headers=headers, params=querystring)
parks = response.json()

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
