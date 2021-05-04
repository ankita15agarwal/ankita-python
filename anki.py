import json


class Car:
    # Create Data
    def addData(self, name, model, launch_date, colour, price):
        detail = {
            "name": name,
            "model": model,
            "launch_date": launch_date,
            "colour": colour,
            "price": price
        }

        def write_json(data, filename='ankita.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        with open('ankita.json') as json_file:
            data = json.load(json_file)
            temp = data['detail']
            a = detail
            temp.append(a)
            write_json(data)

    # Read Data
    def view_data(self):
        y = open('ankita.json').read()
        file = json.loads(y)
        i = 0
        for x in file["detail"]:
            print(x)
            name = x["name"]
            model = x["model"]
            colour = x["colour"]
            launch_date = x["launch_date"]
            price = x["price"]
            print(f"Index Number {i}")
            print("Name of the car :", name)
            print("model of the car:", model)
            print("colour of car :", colour)
            print("launch_date of car :", launch_date)
            print("price of car :", price)
            print("\n\n")
            i = i + 1

    # delete Data
    def deletedata(self, name):
        def write_json(data, filename='ankita.json'):
            with open(filename, 'r+') as file:
                json.dump(data, file, indent=4)

        with open('ankita.json', 'r+') as json_file:
            data = json.load(json_file)
            for i in data["detail"]:

                if (i["name"] == name):
                    temp = data["detail"]
                    temp.remove(i)
                    write_json(data)
                    print("Data Deleted")

# UpdateData
    def update_data(self, filename="ankita.json"):
        self.view_data()
        new_data = []
        with open(filename, "r") as f:
            temp = json.load(f)
        option = int(input("enter number which data you want to update:"))
        i = 0
        for entry in temp:
            if i == option:

                name = input('new name of car:')
                model = input('enter your new model:')
                launch_date = input('enter your new date:')
                colour = input('enter your new colour:')
                price = input('enter your new price')
                new_data.append({ 'name': name, 'model':model,'launch_date':launch_date,'colour':colour,'price':price})
                i = i + 1
            else:
                new_data.append(entry)
                i = i + 1
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)
        print("data updated successfully.")

print("""Enter Your Choice
        1. Create Data
        2. Read Data
        3. Delete Data
        4. Update Data
    """)
x = int(input("Enter number"))
str = Car()
if x == 1:

    name = input("Name of the car :")
    model = input("model of the car:")
    colour = input("colour of car :")
    launch_date = input("launch_date of car :")
    price = input("price of car :")
    str.addData(name, model, colour, launch_date, price)

elif x == 2:

    name = input("enter name")
    str.view_data()

elif x == 3:

    str.deletedata(name='Ferrari')
elif x == 4:
    obj = Car()
    str.update_data()

else:
    print("Invalid Number...")





