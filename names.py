import csv
import random
  
def get_random_last():
    filename = open('pop_last_name.csv', 'r')
    file = csv.DictReader(filename)
    last_names = []
    
    for col in file:
        last_names.append(col['Last Names'])

    print(last_names)

def get_random_first():
    male_list = []
    female_list =[]

    filename = open('pop_name_usa.csv', 'r')
    file = csv.DictReader(filename)
    for col in file:
        male_list.append(col['Male'])
        female_list.append(col['Female'])
    
    return random.choice(male_list), random.choice(female_list)

get_random_first()