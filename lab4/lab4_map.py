from functools import reduce
import csv 

with open("titanic.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))
women_passengers = list(map(lambda x: x[4] == 'female', dataset))
print(women_passengers.count(True))
