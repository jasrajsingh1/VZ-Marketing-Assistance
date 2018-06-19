import urllib2, json

def api_search():
    url = 'https://api.census.gov/data/2015/acs5?get=B07010_001E&for=zip+code+tabulation+area:20878'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    print data

if __name__ == '__main__':
    api_search()