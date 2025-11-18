
"""
# print function -> builtin user-defined
# it helps us to display output in our terminal
print(123)

# python datatypes
# string, float, integer, boolean

# 1.a string is a sequence of characters enquoted in single or double quotes
# '123saji!@# ' 
# "670"

# 2. an integer is any whole number
# 100 200 0 1 2 3

# 3. a float is number with floating point
# 78.90 5.3 

# ctrl + / cmd + /
# "90.34"
# this is a test comment 
# 4. boolean is just True or False 
# 'True'

# python comment and docstring
# python variables and variable naming
# a variable is a storage, it helps us to hold a value or collection of values 
location = "Lagos"
bill2 = 67.88
bill_1 = 89.08
_bill = 79 
bill = 90.76
Bill = 76

print(bill)

# variable naming rules
# 1. a variable can have any character between 0-9, a-z(A-Z), _
# 2. a variable cannot start with a number, however we can have a variable name starting with an underscore 
# 3. variable names are case-sensitive

# python type function
# type function is one of the python builtin functions 
fee = 89.00
print(type(fee))


# python type conversion/casting
# int(), float(), bool(), str()
fee_2 = int(fee)
print(fee_2)

age = 21
age_stringfy = str(age)
print(age_stringfy)

name = "87.44"
# print(int(name))

print(bool(1))

# concatenation -> joining two or more strings together 
first_name = "Philip"
last_name = "Odulaja"
total_students = 18_600
height = 5.6
age = 21
full_name = last_name + first_name
sentence = last_name + " " + first_name + " is an instructor with " + str(total_students) + " student and he is" + str(age) + " yrs old and " + str(height) + "ft tall"

# f-string -> formated string 
sentence_2 = f"{last_name} {first_name} is an instructor with {total_students} student and he is {age}yrs old and he is {height}ft tall"
# Odulaja Philip is an instructor with 18_600 student and he is 21 yrs old and 5.8ft tall
# print(sentence_2)

# print(full_name)
# print(total_students)


# python input function 
weight  = int(input("Enter your weight in kilogram "))
print(type(weight))

# docstring -> documentation string 

This is a introductory python class
hosted by Mr Ademola
We have 6 attendants
ff
f
f
f
f
f
f
f
f
f
f
f
f
f

f
"""