# python error handling
age_str = "8"
age_int = 8

# try...except block 
try:
    age_sum = age_str  + age_int
except Exception:
    print("You cannot add a number to a string")
else:
    print(age_sum)

print("The code has completed execution")

try:
    with open('test.txt', 'x') as new_file:
        pass 
except Exception:
    print("This file already exist")
else:
    print("test.txt has been created successfully")
    print(new_file)
finally:
    print("This is the end of the try..except block")