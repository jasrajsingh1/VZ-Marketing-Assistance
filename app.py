from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
# import sys
# sys.path.insert(0,'/Users/tarraon/Documents/VZ-Marketing-Assistance/Handlers')
from Handlers import handler as h
# import handler as h

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return "The Future is now."


# =================#
#  Demographic API #
# =================#

#Add endpoints for DB queries of interest.
api.add_resource(h.AllInfoHandler, '/NoFilter') 

# # Filters records by a specified race
# # done
api.add_resource(h.RaceHandler, '/filter/race/<string:aRace>') 

# # Filters records by a specified Age range
# # done
api.add_resource(h.AgeHandler, '/filter/age_start=<int:minVal>&end=<int:maxVal>')

# # Filters records by a specified population (quantity of people in an area)
# # done
api.add_resource(h.PopulationHandler, '/filter/population_start=<int:minVal>&end=<int:maxVal>')

# # Filters records by a specified Income range
# # done
api.add_resource(h.IncomeHandler, '/filter/income_start=<float:minVal>&end=<float:maxVal>')

# #Filters records by a specified Race and age range
# # done
api.add_resource(h.RaceAgeHandler, '/filter/race/<string:aRace>/age_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified Race and population range
# # done
api.add_resource(h.RacePopHandler, '/filter/race/<string:aRace>/population_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified Race and income range
# # done
api.add_resource(h.RaceIncomeHandler, '/filter/race/<string:aRace>/income_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified age and population range
# # done
api.add_resource(h.AgePopHandler, '/filter/age_start=<int:minVal>&end=<int:maxVal>/population_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified age and income range
# # done
api.add_resource(h.AgeIncomeHandler, '/filter/age_start=<int:minVal>&end=<int:maxVal>/income_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified population and income range
# # done
api.add_resource(h.PopulationIncomeHandler, '/filter/population_start=<int:minVal>&end=<int:maxVal>/income_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified age and population range
# # done
api.add_resource(h.AgePopulationHandler, '/filter/race/<string:aRace>/age_start=<int:minVal>&end=<int:maxVal>/population_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified age, population, and income range
# # done
api.add_resource(h.AgePopulationIncomeHandler, '/filter/age_start=<int:minVal>&end=<int:maxVal>/population_start=<int:minVal>&end=<int:maxVal>/income_start=<int:minVal>&end=<int:maxVal>')

# #Filters records by a specified race, age, population, and income range
# #done
api.add_resource(h.RaceAgePopulationIncomeHandler, '/filter/race/<string:aRace>/age_start=<int:minVal>&end=<int:maxVal>/population_start=<int:minVal>&end=<int:maxVal>/income_start=<int:minVal>&end=<int:maxVal>')

if(__name__=='__main__'):
    app.run(debug = True, port = 8000)