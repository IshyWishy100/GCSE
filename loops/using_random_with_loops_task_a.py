import time, random

usr_num = int(input("Enter a random number between 1 and 10"))
print(usr_num)

print("I am generating a number...")
time.sleep(2)

num = random.randint(1, 10)
print(f"My random number is {num}.")
