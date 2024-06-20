# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:56:16 2023

@author: Mario
"""

from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/users/*": {"origins": "*"}})
CORS(
    app,
    resources={
        r"/users/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type"],
        }
    },
)


def Page_Not_Found(error):
    return "<h1>Page Not Found</h1>", 404



@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "static"))
    )

@app.route('/css/<path:filename>')
def custom_css(filename):
    return send_from_directory('static/css', filename, mimetype='text/css')


#print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static')))


@app.route("/")
def index():
    domain = request.host_url+"css/swagger-ui.css"
    print(domain)
    return render_template("index.html", domain=domain)


if __name__ == "__main__":
    app.register_error_handler(404, Page_Not_Found)
    app.run(debug=True, host="0.0.0.0")
else:
    application = app
