import re
from flask import render_template, url_for, request, jsonify
from . import app
from wiki_api import WikiApi
from grandpy import Grandpy

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["user_input"]
    response = Grandpy().get_response(user_text)
    return jsonify(response)