# first_name = input("What is your first name ? ")
# last_name = input("What is your last name ? ")
# city = input("Where are you located  ? ")
# full_name = first_name + " " + last_name

# # hello percy oladosu!welcome to colsheterter
# print("hello" + full_name + "!" + "welcome to" + city)
# print(f"Hello {full_name} ! Welcome to {city}")

# num1 = int(input("Enter a number "))
# num2 = int(input("Enter another number "))

# sum = num1 + num2
# difference = num1 - num2
# multiplication = num1 * num2
# divsion = num1 / num2

# print(sum, difference, multiplication, divsion)
# == != > < >= <= 

internet = "slow"

if internet == "active" :
    print("Class is going hold")   
elif internet == "slow" :
    print("Call is going to be delayed due to internet") 
else:
    print("Class is not going to hold")

# if, elif and else are the keywords used to create a conditional statement
# if is independent 
# elif is depenedent on if , you can only use elif if we already have if 
# else is dependent on if 

# ctrl + shift + ``
# cinema ticket 2usd, 5usd, 4usd, 3usd

# logical operators 
# and, or , not 
age = int(input("How old are you ? "))

if age < 18 :
    print("Cinema ticket cost 2usd")
elif age >= 18 and age <= 35:
    print("Cinema ticket cost 5usd")
elif age > 35 and age <= 50 :
    print("Cinema ticket cost 4usd")
elif age > 50:
    print("Cinema ticket cost 3usd")


