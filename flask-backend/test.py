import json
from flask import Flask
from parse import getRss, getXml, getJson
import xml.etree.ElementTree as ET

r = getRss("https://feeds.simplecast.com/54nAGcIl")
root = getXml(r.content)

e = ET.SubElement(root, "item")

print(e.tag)
print(e.attrib)

print( getJson(root))
