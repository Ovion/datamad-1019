import os
import dotenv
import requests
import config

def getPlace(lat, lng, query="coffee"):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
      client_id=os.getenv('FOURSQUARE_CLIENT_ID'),
      client_secret=os.getenv('FOURSQUARE_SECRET'),
      v='20180323',
      ll=f"{lat},{lng}",
      query=query,
      limit=10
    )
    res = requests.get(url, params=params)
    return res.json()

def prepareData(jsonResponse):
    cleanedItems = []
    errors = 0
    for group in jsonResponse["response"]["groups"]:
        for item in group['items']:
            try:
                venue = item["venue"]
                cleanedItems.append({
                    "name":venue["name"],
                    "lat":venue["location"]["lat"],
                    "lng":venue["location"]["lng"],
                    "distance":venue["location"]["distance"],
                    "coordinates":{
                        "type":"Point",
                        "coordinates":[venue["location"]["lat"],venue["location"]["lng"]]
                    }
                })
            except Exception:
                errors += 1
                
    if errors > 0:
        print(f"there are {errors} venues without enough data ")

    return cleanedItems