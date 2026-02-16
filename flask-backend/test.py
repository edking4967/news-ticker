import json, feedparser
from flask import Flask
from parse import getRss, getXml, getJson
import xml.etree.ElementTree as ET

r = getRss("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
feed = feedparser.parse(r.content)
