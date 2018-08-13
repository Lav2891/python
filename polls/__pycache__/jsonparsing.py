import requests
import json

def fun(t):
    getjson = json.loads(t)
    
    if "message" in getjson["status"]:
        print(getjson["status"]["message"])
    if "value" in getjson["status"]:
        print(getjson["status"]["value"])
    

def main():
    url = "http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo"
    w = requests.get(url)
    t = w.text
    #print(t)
    fun(t)
if __name__ == "__main__":
    main()