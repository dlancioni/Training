# https://zetcode.com/python/faker/   

import os
import random
from faker import Faker

os.system("cls")

faker = Faker("pt_BR")

with open("c:\\temp\\data.txt", "w") as f:
    for i in range(1, 10):         
        line = ""
        line += faker.first_name() + " " + faker.last_name() + ";"                                         # Name
        line += faker.email() + ";"                                                                        # Email
        line += str(faker.date_time_between(start_date='-30y', end_date='now').strftime("%Y-%m-%d")) + ";" # Hire Date
        line += random.choice(["Analyst", "Associate", "VP"]) + ";"                                        # Job Title
        line += str(faker.random_int(5000, 10000)) + "." + str(faker.random_int(0, 99)) + ";"              # Salary
        line += "\n"
        f.write(line)

print("Done")        