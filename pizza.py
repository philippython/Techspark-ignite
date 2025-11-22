# ✅ TASK 1 — Basic Pizza Order With Size + Toppings (Nested If)
# Write a Python program that asks the user for:
# Pizza size — S, M, or L
# Whether they want extra cheese
# Whether they want pepperoni
# Use nested conditional statements to calculate the total price based on the rules:
# Small pizza (S) → ₦2500
# Medium pizza (M) → ₦3500
# Large pizza (L) → ₦4500
# Extras:
# Pepperoni →
# ₦300 for S
# ₦500 for M or L
# Extra cheese → ₦200 for any size

# Print the final bill.

pizza_size = input("What is the pizza size you would like to order ? ")
extra_pepperoni = input("Do you want an extra pepperoni ?")
extra_chesse = input("Do you want an extra cheese ?")

bill = 0 

if pizza_size == "S" :
    bill += 2500
    if extra_pepperoni == "Y" :
        bill += 300
    else:
        bill += 0
elif pizza_size == "M":
    bill += 3500
    if extra_pepperoni == "Y" :
        bill += 500
    else:
        bill += 0
elif pizza_size == "L":
    bill += 4500
    if extra_pepperoni == "Y" :
        bill += 500
    else:
        bill += 0
else:
    print("Pizza size is not available")

if extra_chesse == "Y":
    bill += 200


print(f"Your total bill is #{bill}")

# DRY -> Do not repeat yourself