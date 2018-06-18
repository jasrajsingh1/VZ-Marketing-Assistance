import csv
from uszipcode import ZipcodeSearchEngine

results = []
search = ZipcodeSearchEngine()
with open("ROW_Billboards_data.csv") as csvfile:
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
                