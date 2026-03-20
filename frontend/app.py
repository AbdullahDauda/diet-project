import json
import os

from flask import Flask, Response, send_from_directory

app = Flask(__name__, static_folder="dashboard", static_url_path="")

@app.get("/config.js")
def config():
    backend_url = os.getenv("BACKEND_URL", "")
    body = f"window.BACKEND_URL = {json.dumps(backend_url)};\\n"
    return Response(body, mimetype="application/javascript")


@app.get("/")
def index():
    return send_from_directory("dashboard", "index.html")


@app.get("/<path:path>")
def static_files(path: str):
    return send_from_directory("dashboard", path)
