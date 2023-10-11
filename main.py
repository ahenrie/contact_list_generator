import random
import csv
import names

class gen_customer():
  def __init__(self, num_customers, customers = []):
    self.num_customers = num_customers
    self.customers = customers

    with open("zip_code_database.csv", "r") as csvfile:
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

    for i in range(num_customers):
        zipcodes = list(zip_dictionary.keys())
        first_name = names.get_random_first()
        last_name = names.get_random_last()
        email = first_name.lower() + random.choice(["_", "-", "."]) + last_name.lower() + random.choice(["@gmail.com", "@hotmail.com", "@aol.com", "@outlook.com"])
        street_address = "123 Main St"
        zip_code = random.choice(zipcodes)
        city = zip_dictionary[zip_code]["primary_city"]
        state = zip_dictionary[zip_code]["state"]
        customer = {
        "id": i,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        #"street_address": street_address,
        "city": city,
        "state": state,
        "zip": zip_code
        }
        customers.append(customer)
    print(self.customers)

list1 = gen_customer()

