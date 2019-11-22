from mongodb import getCollection
from foursquare import getPlace,prepareData
import json

def main():
    mataderoMadrid = [40.3826978,-3.6927541]
    places = getPlace(*mataderoMadrid,"starbucks")
    db, col = getCollection("starbucks","starbucks")

if __name__ == "__main__":
    main()
