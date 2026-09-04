#Task 1
print("----- Task 1 -----")
cars = []
brand = input("Enter car brand")
cars.append(brand)
brand = input("Enter car brand")
cars.append(brand)
brand = input("Enter car brand")
cars.append(brand)
print(cars)

#Task 2
print("----- Task 2 -----")
cars = []
sentry = True
while sentry == True:
    user = input("Input a car brand or press x to exit").lower()
    if user == "x":
        print("Exiting...")
        sentry = False
    else:
        cars.append(user)
print(f"In the list is {cars}")

#Task 3
print("----- Task 3 -----")
names = []
name1 = input("Enter name 1")
names.append(name1)
name2 = input("Enter name 2")
names.append(name2)
name3 = input("Enter name 3")
names.append(name3)
confirm = input("Add another person? Y/N").lower()
if confirm == "y":
    while True:
        name = input("Enter name")
        names.append(name)
        confirm = input("Add another person? Y/N").lower()
        if confirm == "n":
            break
        else:
            continue
print(f"You have invited {len(names)} to the party.")

#Task 4
print("----- Task 4 -----")
programmes = [
    "Thanger Strings"
    "Beaking Brad"
    "Thame of Grones"
    "Kujustu Jaisen"
    "Tattack on Itan"
    ]
show = input("Enter another show")
position = int(input("Enter index"))

programmes[0].append(show)
print(programmes)
