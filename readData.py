import csv, urllib2, json, time
from uszipcode import ZipcodeSearchEngine

results = []
search = ZipcodeSearchEngine()
with open('/Users/burda9l/Documents/VZ-Marketing-Assistance/ROW_Billboard_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|') # change contents to floats
    for row in reader: # each row is a list 
        results.append(row)

ziplist = []

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

            ## White
            wurl = 'https://api.census.gov/data/2015/acs5?get=B01001H_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            wdata = json.load(urllib2.urlopen(wdata))

            ## Hispanic
            hurl = 'https://api.census.gov/data/2015/acs5?get=B01001I_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            hdata = json.load(urllib2.urlopen(hdata))

            ## Asian
            aurl = 'https://api.census.gov/data/2015/acs5?get=B01001D_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            adata = json.load(urllib2.urlopen(aurl))

            ## Median Age
            maurl = 'https://api.census.gov/data/2015/acs5?get=B01002_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            mdata = json.load(urllib2.urlopen(maurl))
            
            ## Count
            curl = 'https://api.census.gov/data/2015/acs5?get=B01001_001E&for=zip+code+tabulation+area:' + zipcode + '&key=2fd73cb25990a63e4d615c3bcbd02bbded8afd33'
            cdata = json.load(urllib2.urlopen(curl))

