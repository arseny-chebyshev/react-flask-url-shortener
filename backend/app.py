import json
from lib2to3.pgen2.parse import ParseError
from urllib.parse import urlparse
from flask import Flask, request, jsonify, redirect, abort
from flask_cors import CORS
from utils import URLShortener
from models import URL
from db import Client

app = Flask(__name__)
CORS(app)

db_client = Client(db='flask-db')

@app.route("/<string:short_url>")
def redirect_to_long_url(short_url):
    with db_client:
        url = URL.objects.filter(short_url=short_url).first()
        if not url:
            return abort(404)
    return redirect(url.long_url)

@app.route("/url", methods=["OPTIONS", "POST"])
def create_url():
    if request.method == "POST":
        shortener = URLShortener()
        try:
            data = json.loads(request.data)
            url = shortener.validate_url(str(data['target_url']))
            with db_client:
                document = URL.objects.filter(long_url=url).first()
                if document:
                    short_url = document.short_url
                else:
                    short_url = shortener.create_short_alias()
                    document = URL(long_url=url, short_url=short_url)
                    document.save()
            response = jsonify({"url": f"http://localhost:5000/{short_url}",
                                "target_url": url})
            
        except ParseError:
            response = jsonify({"url": "URL не является валидным"})
        except KeyError:
            response = jsonify({"error": "URL не был предоставлен"})
    else:
        response = jsonify({"nothing": "happened"})
    
    return response
