from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from Handlers import handler as h

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return "The Future is now."


# =================#
#  Demographic API #
# =================#

#Add endpoints for DB queries of interest.

#Filters records by a specified race
api.add_resource(RaceHandler, '/filter/race/<string:aRace>') 

#Filters records by a specified Age range
api.add_resource(, '/filter/age?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified population (quantity of people in an area)
api.add_resource(, '/filter/population?start=<int:minVal>&end=<int:maxVal>)

#Filters records by a specified Income range
api.add_resource(, '/filter/income?start=<float:minVal>&end=<float:maxVal>')

#Filters records by a specified Race and age range
api.add_resource(, '/filter/race/<string:aRace>/age?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified Race and population range
api.add_resource(, '/filter/race/<string:aRace>/population?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified Race and income range
api.add_resource(, '/filter/race/<string:aRace>/income?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified Race and population range
api.add_resource(, '/filter/race/<string:aRace>/population?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified age and population range
api.add_resource(, '/filter/age?start=<int:minVal>&end=<int:maxVal>/population?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified age and income range
api.add_resource(, '/filter/age?start=<int:minVal>&end=<int:maxVal>/income?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified population and income range
api.add_resource(, '/filter/population?start=<int:minVal>&end=<int:maxVal>/income?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified age and population range
api.add_resource(, '/filter/race/<string:aRace>/age?start=<int:minVal>&end=<int:maxVal>/population?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified age, population, and income range
api.add_resource(, '/filter/age?start=<int:minVal>&end=<int:maxVal>/population?start=<int:minVal>&end=<int:maxVal>/income?start=<int:minVal>&end=<int:maxVal>')

#Filters records by a specified age, population, and income range
api.add_resource(, '/filter/race/<string:aRace>/age?start=<int:minVal>&end=<int:maxVal>/population?start=<int:minVal>&end=<int:maxVal>/income?start=<int:minVal>&end=<int:maxVal>')