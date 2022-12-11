import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
characters = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
print("PASSWORD GENERATOR !!")
count_of_letters = int(input("How many letters does your password required ?"))
count_of_number = int(input("How many numbers does your password required ?"))
count_of_spl = int(input("How many special characters does you password required ?"))
password_list = []
for i in range(0, count_of_letters):
    password_list.append(random.choice(letter))
for j in range(0, count_of_number):
    password_list.append(random.choice(numbers))
for k in range(0,count_of_spl):
    password_list.append(random.choice(characters))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")
