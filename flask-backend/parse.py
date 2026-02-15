import requests, feedparser
import xml.etree.ElementTree as ET

def getRss(url):
    response = requests.get(url, timeout=5) # Takes a long time 
    response.raise_for_status()  # raises error if download failed
    return response

def getXml(xmlString):
    root = ET.fromstring(xmlString)
    return root

def getJson(root):
    return {"content": None}
