import json, requests, feedparser
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)   # allow all origins (dev only)

@app.route("/feed")
def feed():
    url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    response = requests.get(url, timeout=5) # Takes a long time 
    response.raise_for_status()  # raises error if download failed
    feed = feedparser.parse(response.content)
    return feed

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# TODO: create a route like def parseXml(xmlUrl):
# return root
# (Would this be safe?) NO. cannot fetch/parse arbitrary xml.
# Safer way?# 
# TODO: go through feed and make json object to pass to react
