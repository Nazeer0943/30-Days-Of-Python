# this is about variables, data types, bulit-in functions and type conversion
# Exercises: Level 1
# Day 2: 30 Days of python programming
first_name = "Nazir" # string
last_name = "Sani" # string
full_name = first_name + " " + last_name # string concatenation
country = "Nigeria" # string
city =  "Katsina" # string
age =  26 # int
year = 2026 # int
is_married  = True # bool
is_true  = True # bool
is_light_on = False # bool
abba, ismail, musa = 1, 2, 3

# Exercises: Level 2
print(type(first_name)) # str
print(type(last_name)) # str
print(type(full_name)) # str
print(type(country)) # str
print(type(city)) # str
print(type(age)) # int
print(type(year)) # int
print(type(is_married)) # bool
print(type(is_true)) # bool
print(type(is_light_on)) # bool

print(len(first_name)) # 5
print(len(first_name) == (len(last_name))) # False
print(len(full_name)) # 10
numb_1 = 5
numb_2 = 4
total = numb_1 + numb_2
diff = numb_1 - numb_2
product = numb_1 * numb_2
division = numb_1 / numb_2
remainder = numb_2 % numb_1
exp = numb_1**numb_2
floor_division = numb_1 // numb_2
"""The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area."""
radius = 30
pi = 3.142
area_of_circle = pi * radius ** 2
circum_of_circle = 2*pi*radius
print(area_of_circle) # 2827.8
print(circum_of_circle) # 188.52
new_rad = float(input("Enter the radius of the circle: "))
area_of_circle = pi * new_rad ** 2
print(area_of_circle)

"""Use the built-in input function to get first name, last name, country and age from a 
user and store the value to their corresponding variable names"""
first_nm = input("Enter you first name: ")
last_nm = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print(f"The user's name is {first_nm}, {last_nm}. He is from {country} and he is just {age} years old.")
