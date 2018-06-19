from flask import jsonify, request
from DAO.dao import InfoDAO
from flask_restful import Resource, reqparse

def mapToDict(row):
    mappedResult = {}
    mappedResult['']=row[0]

    return mappedResult

class RaceHandler(Resource):
    def get(self,aRace):
        dao = InfoDAO()
        aFilter = dao.filterByRace(aRace)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(RaceFilter= resultList)

class AgeHandler(Resource):
    def get(self,minVal,maxVal):
        dao = InfoDAO()
        aFilter = dao.filterByAge(minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgeFilter= resultList)
