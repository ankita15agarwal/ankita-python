import json

a = input("Enter the name of the car : ")
f = open('details.json', )
data = json.load(f)
for i in data['CarDetails']:
    print(i)
