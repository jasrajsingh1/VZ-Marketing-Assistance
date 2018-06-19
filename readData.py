import csv, urllib2, json, time
import pymysql
from itertools import chain
from uszipcode import ZipcodeSearchEngine

pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect(host="localhost",user="burda9l",passwd="grandtheft23",db="marketingDB")
init = db.cursor()

results = []
search = ZipcodeSearchEngine()
with open('/Users/burda9l/Documents/VZ-Marketing-Assistance/ROW_Billboard_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|') # change contents to floats
    for row in reader: # each row is a list 
        results.append(row)

line_num = 1
for arr in results:
        lat_lon_str = arr[0]
      #  objId = arr[1]
    # town = arr[3]
       # addr = arr[4]

        if lat_lon_str:
            lon = float(lat_lon_str.split(" ")[1].split("(")[1])
            lat = float(lat_lon_str.split(" ")[2].split(")")[0])
            zipcode = search.by_coordinate(lat,lon)[0].Zipcode

            ## Race API Call
            ## Black
            burl = 'https://api.census.gov/data/2015/acs5?get=B01001B_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            bdata = json.load(urllib2.urlopen(burl))
            bdata = list(chain.from_iterable(bdata))
            bdata = int(''.join(bdata[2]))

            ## White
            wurl = 'https://api.census.gov/data/2015/acs5?get=B01001H_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            wdata = json.load(urllib2.urlopen(wdata))
            wdata = list(chain.from_iterable(wdata))
            wdata = int(''.join(wdata[2]))

            ## Hispanic
            hurl = 'https://api.census.gov/data/2015/acs5?get=B01001I_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            hdata = json.load(urllib2.urlopen(hdata))
            hdata = list(chain.from_iterable(hdata))
            hdata = int(''.join(hdata[2]))

            ## Asian
            aurl = 'https://api.census.gov/data/2015/acs5?get=B01001D_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            adata = json.load(urllib2.urlopen(aurl))
            adata = list(chain.from_iterable(adata))
            adata = int(''.join(adata[2]))

            ## Median Age
            maurl = 'https://api.census.gov/data/2015/acs5?get=B01002_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            mdata = json.load(urllib2.urlopen(maurl))
            mdata = list(chain.from_iterable(mdata))
            mdata = int(''.join(mdata[2]))
            
            ## Count
            curl = 'https://api.census.gov/data/2015/acs5?get=B01001_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            cdata = json.load(urllib2.urlopen(curl))
            cdata = list(chain.from_iterable(cdata))
            cdata = int(''.join(cdata[2]))


