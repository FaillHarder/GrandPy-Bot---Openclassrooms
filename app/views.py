from . import app
from .grandpybot.grandpy import Grandpy

from flask import render_template, request, jsonify


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["user_input"]
    response = Grandpy().get_response(user_text)
    return jsonify(response)
