"""
Write a program to find and display the largest number 
of a list without using built-in function max(). 
"""

num_list = input("Enter a list of number\n:> ").strip().split(' ')

max = int(num_list[0])
for num in range(1, len(num_list)):
    if max < int(num_list[num]) :
        max = int(num_list[num])

print(max)
 
