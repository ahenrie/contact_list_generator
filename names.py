import csv
import random
  
def get_random_last():
    filename = open('pop_last_name.csv', 'r')
    file = csv.DictReader(filename)
    last_names = []
    
    for col in file:
        last_names.append(col['Last Names'])

    return random.choice(last_names)

def get_random_first():
    male_list = []
    female_list =[]
    i = random.randint(1, 100)

    filename = open('pop_name_usa.csv', 'r')
    file = csv.DictReader(filename)
    for col in file:
        male_list.append(col['Male'])
        female_list.append(col['Female'])
    if i % 2 == 0:
        return random.choice(male_list)
    else:
        return random.choice(female_list)
