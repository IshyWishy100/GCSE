#task 1 - Find The Factorial
num = int(input("Enter number: "))

total = 1

for i in range(num, 0, -1):
    total *= i

print(total)

#Task 2 - Reverse it
sentence = input("Enter a sentence to be reversed: ")

vowels = ["a", "e", "i", "o", "u"]
vowels_num = 0
cons_num = 0

for i in range(len(sentence)):
    if sentence[i] in vowels:
        vowels_num += 1
    else:
        cons_num += 1

print(sentence[::-1])
print(f"Number of consonants: {cons_num}")
print(f"Number of vowels: {vowels_num}")

#Task 3 - R@nd0m P@ssw0rd
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','£','$','%','&','*','€','#','?']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = []

length = int(input("Pick a password length: "))

for i in range(length):
    category = random.randint(1, 4)
    if category == 1:
        password.append(random.choice(letters))
    elif category == 2:
        password.append(random.choice(symbols))
    elif category == 3:
        password.append(random.choice(numbers))
    else:
        password.append(random.choice(letters).upper())

print("".join(password))
