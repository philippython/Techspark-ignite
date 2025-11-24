from random import randint
# Python Magic/dunder method & Pass Keyword
# while loop

# def square_number(number):
#     """This function calculates the square of a number"""
#     square = number ** 2
#     print(square)

# print(square_number.__doc__)
# "string"
# 'string'
# docstring is a string it starts with """"""
# docstring is used for documentation
# """string"""

# def function():
#     pass

# car_state = "fine"
# reached_finished = False
# kilometres = 0

# while car_state != "crashed" and reached_finished != True:
#     print("Racing!!!")
#     kilometres += 20 
#     if kilometres > 120:
#         reached_finished = True

def count_by(start:int, stop:int, step=1):

    """prints number from start to stop, increasing by step, using a while loop"""
    current = start
    while current <= stop:
        print(current)
        current += step

# count_by(3, 9, 1)

# def compare(x:int, y:int): 
#     if x > y:
#         return x
#     elif y > x :
#         return y
#     else:
#         return x, y

# biggest = compare(7, 7)
# print(biggest[0])

# def login(username, password):
#     if (username == "admin" and password == "1234"):
#         return "Login successful"
#     else:
#         if username == "admin":
#             return "Password is incorrect"
#         else:
#             return "username is incorrect"
# 5 * 4 * 3 * 2 * 1

def factorial(n:int):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1) # Recursive call
   
factorial_ten = factorial(10)

# print(factorial(5))
correct_number = randint(0,100)
chances = ["❤️", "❤️", "❤️", "❤️", "❤️"]
print(correct_number)

def game():
    guessed_number = int(input("Guess a number between 0-100 "))

    if guessed_number > correct_number:
        print("Too high \nYou guessed wrong")
        chances.remove("❤️")
        print("".join(chances))
        if len(chances) > 0:
            game()
    elif guessed_number < correct_number:
        print("Too Low \nYou guessed wrong")
        chances.pop()
        print("".join(chances))
        if len(chances) > 0:
            game()
    else:
        print("You won!! \nYou guessed right")

# game()

# first class is a function that can be assigned to a variable 
# higher order function is a fuction that takes another function as its paramter
def discount(price, discount_percentage):
    discount_price = price - ( discount_percentage / 100 * price )
    return discount_price

def bill(price, discount_percentage, cust_name: str, discount_func):
    return f"{cust_name} final bill is ${discount_func(price, discount_percentage)}"

print(bill(450, 2, "Philip", discount))






