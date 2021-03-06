import csv, urllib2, json, time
import psycopg2, datetime
from itertools import chain
from uszipcode import ZipcodeSearchEngine

## MAKE MODIFICATIONS!!!
db = psycopg2.connect(dbname='marketingDBPSQL', user='burda9l')

cursor = db.cursor()

results = []
search = ZipcodeSearchEngine()

zipIncome = {}
with open('/Users/burda9l/Documents/VZ-Marketing-Assistance/Income Data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|') # change contents to floats
    for row in reader: # each row is a list 
        if row[1] != "-":
            zipIncome[row[0].zfill(5)] = row[1]

with open('/Users/burda9l/Documents/VZ-Marketing-Assistance/ROW_Billboards_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|') # change contents to floats
    for row in reader: # each row is a list 
        results.append(row)

line_num = 1
for arr in results:
        lat_lon_str = arr[0]
        objId = arr[1]
        town = arr[3]
        addr = arr[4]

        if lat_lon_str:
            lon = float(lat_lon_str.split(" ")[1].split("(")[1])
            lat = float(lat_lon_str.split(" ")[2].split(")")[0])
            zipcode = search.by_coordinate(lat,lon)[0].Zipcode
            
            ## Race API Call
            ## Black
            burl = 'https://api.census.gov/data/2015/acs5?get=B01001B_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            bdata = json.load(urllib2.urlopen(burl))
            bdata = list(chain.from_iterable(bdata))
            bdata = float(''.join(bdata[2]))

            ## White
            wurl = 'https://api.census.gov/data/2015/acs5?get=B01001H_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            wdata = json.load(urllib2.urlopen(wurl))
            wdata = list(chain.from_iterable(wdata))
            wdata = float(''.join(wdata[2]))

            ## Hispanic
            hurl = 'https://api.census.gov/data/2015/acs5?get=B01001I_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            hdata = json.load(urllib2.urlopen(hurl))
            hdata = list(chain.from_iterable(hdata))
            hdata = float(''.join(hdata[2]))

            ## Asian
            aurl = 'https://api.census.gov/data/2015/acs5?get=B01001D_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            adata = json.load(urllib2.urlopen(aurl))
            adata = list(chain.from_iterable(adata))
            adata = float(''.join(adata[2]))

            overallData = int(max([bdata,wdata,hdata,adata]))

            if overallData == bdata:
                race = "Black"
            elif overallData == wdata:
                race = "White"
            elif overallData == hdata:
                race = "Hispanic"
            elif overallData == adata:
                race = "Asian"
            else:
                race = "N/A"


            ## Median Age
            maurl = 'https://api.census.gov/data/2015/acs5?get=B01002_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            mdata = json.load(urllib2.urlopen(maurl))
            mdata = list(chain.from_iterable(mdata))
            mdata = str(float(''.join(mdata[2])))
            
            ## Count
            curl = 'https://api.census.gov/data/2015/acs5?get=B01001_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            cdata = json.load(urllib2.urlopen(curl))
            cdata = list(chain.from_iterable(cdata))
            cdata = str(float(''.join(cdata[2])))

            if zipcode not in zipIncome:
                income = 0
            else:
                income = float(zipIncome[zipcode])
            
            lat = str(lat)
            lon = str(lon)
            income = str(income)
            overallData = str(overallData)

            if cdata > 1000:
                insertStatement = "INSERT INTO information VALUES("+objId+","+"'"+town+"'"+","+"'"+addr+"'"+","+"'"+zipcode+"'"+","+mdata+","+income+","+"'"+race+"'"+","+cdata+","+"'"+lon+"'"+","+"'"+lat+"'"+");"
                print insertStatement
                cursor.execute(insertStatement)
                db.commit()
            else:
                print("This is too small. Skipping...")
db.close()

        
