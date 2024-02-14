"""
Write a program to enter names of employees and their salaries 
as input and store them in a dictionary.
"""

print('Enter your name and salary')

employee = input(':> ').strip().split(" ")
emp_list = {}
while employee[0] != 'no' :
    emp_list[employee[0]] = employee[1]
    employee = input(':> ').strip().split(" ")
print(emp_list)