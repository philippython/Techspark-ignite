# type hinting
def square_number(number:int):
    """This function calculates the square of a number"""
    square = number ** 2
    print(square)

square_number(5)

# print vs return

def mins_to_hrs(minutes:int):
    hours = minutes / 60
    return hours

hrs = mins_to_hrs(135)

def compare(x:int, y:int): 
    if x > y:
        return x
    elif y > x :
        return y
    
highest = compare(43, 12)
print(highest)

def login(username:str, password:str):

    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        if username == "admin":
            return "Password is incorrect"
        else:
            return "username is incorrect"
   
        

response = login("admin", "1234")
print(response)

def calculator(num1:int, num2:int):
    addition = num1 + num2
    subtraction = num1 - num2
    division = num1 / num2
    return addition, subtraction, division

add, _, _ = calculator(23, 11)
print(add)
