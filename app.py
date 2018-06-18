from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return "The Future is now."


# =================#
#  Demographic API #
# =================#

#Add endpoints for DB queries of interest.
