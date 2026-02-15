import json
from flask import Flask
from parse import getRss, getXml, getJson

app = Flask(__name__)

@app.route("/feed")
def feed():
    r = getRss("https://feeds.simplecast.com/54nAGcIl")
    root = getXml(r.content)
    return getJson(root)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# TODO: create a route like def parseXml(xmlUrl):
# return root
# (Would this be safe?) NO. cannot fetch/parse arbitrary xml.
# Safer way?# 
# TODO: go through feed and make json object to pass to react
