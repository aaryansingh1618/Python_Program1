#This is a cart game in which you enter some food name and their prices and you get waht you add in the last and total price
foods = []
prices = []
total = 0
while True:
    food = (input("Enter your food to buy(q to quit)"))
    if food.lower() == "q":
     break
    else: 
     price = float(input(f"Enter the Price of {food}: $"))
     foods.append(food)
     prices.append(price)
print("-----Your Cart-----")
for food in foods:
 print(food,end= "")
 print()
for price in prices:
 total += price
print(f"Your Total is: {total}$")
    