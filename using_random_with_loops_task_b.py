import random, string

num_pass = int(input("Enter how many passwords you would like to generate.\n> "))

print("Generated passwords:")
for i in range(num_pass):
  password = ""
  for j in range(10):
    char = random.choice(string.ascii_letters + string.digits)
    password += char
  print(password)
