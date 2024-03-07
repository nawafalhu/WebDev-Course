"""
Write a program that prompts the user to input a Celsius temperature and 
outputs the equivalent temperature in Fahrenheit
"""

Celsius = int(input("Enter a Celsius temperature\n:> "))

fah =  (Celsius * 9/5) + 32

print(f"the temperature in Fahrenheit is {fah}")
