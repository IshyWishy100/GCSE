#Task 1 - Unit Converter
unit = input("Enter unit for value: mm, cm, m or km  ")
convert_unit = input("Enter unit to convert to: mm, cm, m or km  ")
value = float(input("Enter value: "))

if unit == "mm":
    if convert_unit == "cm":
        print(value/10)
    elif convert_unit == "m":
        print(value/1000)
    elif convert_unit == "km":
        print(value/1000000)
    else:
        print("Please enter a valid unit")
elif unit == "cm":
    if convert_unit == "mm":
        print(value*10)
    elif convert_unit == "m":
        print(value/100)
    elif convert_unit == "km":
        print(value/100000)
    else:
        print("Please enter a valid unit")
elif unit == "m":
    if convert_unit == "mm":
        print(value/1000)
    elif convert_unit == "cm":
        print(value/100)
    elif convert_unit == "km":
        print(value*1000)
    else:
        print("Please enter a valid unit")
elif unit == "km":
    if convert_unit == "mm":
        print(value*1000000)
    elif convert_unit == "cm":
        print(value*100000)
    elif convert_unit == "m":
        print(value*1000)
    else:
        print("Please enter a valid unit")


#Task 2 - Year Addition
year = input("Enter a year")
total = 0
for i in range(len(year)):
    total += int(year[i])
print(total)


#Task 3 - Tiler's Mate
floor_w = float(input("Enter floor width: "))
floor_l = float(input("Enter floor length: "))
tile_w = float(input("Enter tile width: "))
tile_l = float(input("Enter tile length: "))
tile_cost = float(input("Enter tile cost: "))

floor_a = floor_w * floor_l
tile_a = tile_w * tile_l

tile_num = floor_a / tile_a

cost = tile_num * tile_cost

print(f"Total cost: {round(cost, 2)}")


#Task 4 - FizzBuzz
num = int(input("Enter number"))
for i in range(1, num+1):
    if i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
