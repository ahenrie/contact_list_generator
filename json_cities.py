import csv
import random
import json

with open("zip_code_database.csv", "r") as csvfile:
    zip_list = []
    zip_dictionary = {}
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        zipcode = row[0]
        type = row[1]
        decommissioned = row[2]
        primary_city = row[3]
        acceptable_cities = row[4]
        unacceptable_cities = row[5]
        state = row[6]
        county = row[7]
        timezone = row[8]
        area_codes = row[9]
        world_region = row[10]
        country = row[11]
        latitude = row[12]
        longitude = row[13]
        irs_estimated_population = row[14]

        #create row in dictionary
        zip_dictionary[zipcode] = {
            "primary_city": primary_city,
            "county": county,
            "state": state,
            "population": irs_estimated_population
        }

    #save json to file
    with open("zip.json", "w") as jsonfile:
        json_zip = json.dump(zip_dictionary, fp=jsonfile)
