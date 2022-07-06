# https://zetcode.com/python/faker/   

import os
import random
from faker import Faker

os.system("cls")

faker = Faker("pt_BR")

with open("c:\\temp\\100k1.txt", "w") as f:
    f.write("Codigo; Nome; Email; Data; Cargo; Salario\n")
    for i in range(1, 100001):
        line = ""
        line += str(i) + ";"                                                                               # Codigo
        line += faker.first_name() + " " + faker.last_name() + ";"                                         # Name
        line += faker.email() + ";"                                                                        # Email
        line += str(faker.date_time_between(start_date='-30y', end_date='now').strftime("%Y-%m-%d")) + ";" # Hire Date
        line += random.choice(["Analista", "Gerente", "Diretor"]) + ";"                                    # Job Title
        line += str(faker.random_int(5000, 10000)) + "." + str(faker.random_int(0, 99)) + ";"              # Salary
        line += "\n"
        f.write(line)

print("Done")        