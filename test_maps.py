#!/usr/bin/python
# json.load()  reads json from a file
# json.loads() reads json from a string
import json
from flask import Flask
from flask_googlemaps import GoogleMaps
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.txt')

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = config.get('google', 'api_key')

GoogleMaps(app)

#@app.route("/")
#def mapview():

with open('data.json') as parks_file:    
    parks = json.load(parks_file)
