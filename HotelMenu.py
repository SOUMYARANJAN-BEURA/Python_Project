"""
"menu = {
    'Pizza' : 350,
    'Burger' : 120,
    'Pasta' : 90,
    'Salad' : 50,
    'Coffee' : 60
}

print("Welcome To Python Hotel")

print(" Pizza : 350 \n Burger : 120 \n Pasta : 90 \n Salad : 50 \n Coffee : 60")


order_total = 0

item1 = input("Enter the name of item you want to order = ")

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been Ordered")
else:
    print(f"Sorry, ordered item {item1} is not available in menu !!")


another_item = input("Do you want to order another item ? (Yes/No) = ")
if another_item == "Yes":
    item2 = input("Enter the name of second item = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item {item2} has been Ordered")
    else:
        print(f"Sorry, ordered item {item2} is not available in menu !!")    

print(f"Your total bill is to pay {order_total}")"


"""

menu = {
    'Pizza': 350,
    'Burger': 120,
    'Pasta': 90,
    'Salad': 50,
    'Coffee': 60
}

print("Welcome To Python Hotel")
print("Menu:")
for item, price in menu.items():
    print(f" {item} : {price}")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order (or type 'stop' to finish) = ").capitalize()

    if item.lower() == "stop":
        break  # Exit the loop when the user types 'stop'

    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been Ordered")
    else:
        print(f"Sorry, ordered item {item} is not available in the menu !!")

print(f"Your total bill to pay is {order_total}")
print("Thank you for visiting Python Hotel! 😊")
