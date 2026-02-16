from flask import send_from_directory, Flask
import requests, feedparser

app = Flask(__name__)


@app.route("/")
def serve():
    return send_from_directory("dist", "index.html")

@app.route("/assets/<path:path>")
def serve_assets(path):
    return send_from_directory("dist/assets", path)

@app.route("/feed")
def feed():
    url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    response = requests.get(url, timeout=5) # Takes a long time
    response.raise_for_status()  # raises error if download failed
    feed = feedparser.parse(response.content)
    return feed

