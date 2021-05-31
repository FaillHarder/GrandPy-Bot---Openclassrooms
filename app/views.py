from . import app
import config
from .grandpybot.grandpy import Grandpy


from flask import render_template, request, jsonify


@app.route("/")
def home():
    api_key = config.HERE_API_KEY
    return render_template("index.html", api_key=api_key)


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["user_input"]
    response = Grandpy().get_response(user_text)
    return jsonify(response)
