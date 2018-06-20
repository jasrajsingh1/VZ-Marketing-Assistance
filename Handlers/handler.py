from flask import jsonify, request

import sys
from DAO import dao as d
from flask_restful import Resource, reqparse

def mapToDict(row):
    mappedResult = {}
    mappedResult['objectID']=row[0]
    mappedResult['town']=row[1]
    mappedResult['streetaddress']=row[2]
    mappedResult['zipcode']=row[3]
    mappedResult['age']=row[4]
    mappedResult['amount']=float(row[5])
    mappedResult['race']=row[6]
    mappedResult['popCount']=row[7]
    mappedResult['lng']=row[8]
    mappedResult['lat']=row[9]
    return mappedResult

class AllInfoHandler(Resource):
    def get(self):
        dao = d.d.InfoDAO()
        aList = dao.noFilter()
        resultList = []
        for row in aList:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AllInformation= resultList)

class RaceHandler(Resource):
    def get(self,aRace):
        dao = d.InfoDAO()
        aFilter = dao.filterByRace(aRace)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(RaceFilter= resultList)

class AgeHandler(Resource):
    def get(self,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByAge(minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgeFilter= resultList)

class PopulationHandler(Resource):
    def get(self,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByPopulation(minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(PopulationFilter= resultList)

class IncomeHandler(Resource):
    def get(self,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByIncome(minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(IncomeFilter= resultList)

class RaceAgeHandler(Resource):
    def get(self,aRace,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByR_A(aRace,minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(RaceAgeFilter= resultList)
    
class RacePopHandler(Resource):
    def get(self,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByR_P(aRace,minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(RacePopFilter= resultList)

class RaceIncomeHandler(Resource):
    def get(self,minVal,maxVal):
        dao = d.InfoDAO()
        aFilter = dao.filterByR_I(aRace,minVal,maxVal)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(RaceIncomeFilter= resultList)

class AgePopHandler(Resource):
    def get(self,minAge,maxAge,minPop,maxPop):
        dao = d.InfoDAO()
        aFilter = dao.filterByA_Pop(minAge,maxAge,minPop,maxPop)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgePopulationFilter= resultList)

class AgeIncomeHandler(Resource):
    def get(self,minAge,maxAge,minInc,maxInc):
        dao = d.InfoDAO()
        aFilter = dao.filterByA_Income(minAge,maxAge,minPop,maxPop)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgeIncomeFilter= resultList)

class PopulationIncomeHandler(Resource):
    def get(self,minPop,maxPop,minInc,maxInc):
        dao = d.InfoDAO()
        aFilter = dao.filterByP_Income(minPop,maxPop,minInc,maxInc)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(PopulationIncomeFilter= resultList)

class AgePopulationHandler(Resource):
    def get(self,minAge,maxAge,minPop,maxPop):
        dao = d.InfoDAO()
        aFilter = dao.filterByA_Population(minAge,maxAge,minPop,maxPop)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgePopulationFilter= resultList)

class AgePopulationIncomeHandler(Resource):
    def get(self,minAge,maxAge,minPop,maxPop,minInc,maxInc):
        dao = d.InfoDAO()
        aFilter = dao.filterByA_Pop_Inc(minAge,maxAge,minPop,maxPop,minInc,maxInc)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgePopulationFilter= resultList)

class RaceAgePopulationIncomeHandler(Resource):
    def get(self,aRace,minAge,maxAge,minPop,maxPop,minInc,maxInc):
        dao = d.InfoDAO()
        aFilter = dao.filterByR_A_Pop_Inc(aRace,minAge,maxAge,minPop,maxPop,minInc,maxInc)
        resultList = []
        for row in aFilter:
            result = mapToDict(row)
            resultList.append(result)
        return jsonify(AgePopulationFilter= resultList)

