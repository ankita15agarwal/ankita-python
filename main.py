
import json
a = input("Enter the name of the car : ")
data = open('details.json', )
obj = json.load(data)
for x in obj["Detail"]:
   if (x['name'] == a):
      print(x)



