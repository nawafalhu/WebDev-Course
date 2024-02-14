"""
Write a program that prompts the user to input a number and prints its multiplication table
"""

user_num = int(input("Enter a number\n:> "))

for i in range(1, 11):
    result = i * user_num
    print(f"{user_num} * {i} = {result}")