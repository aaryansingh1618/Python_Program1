# In this program you can order something from menu then get your bill by your order and total
menu ={"Pizza": 250.00,
       "Chole Bhature": 100,
       "Chocolate" : 100,
       "Momos": 50,
       "Cold Drink": 50,
       "Chips": 50,
       "Popcorn": 100,
       "Protein Shake": 100,
       "Oat Meal": 100,
       "Pineapple Juice": 50,
       "Biryani": 100,
       "Eggs": 100}
cart = []
total = 0
print("\033[1m            MENU\033[0m")
print("-------------------------------")
for key,value in menu.items():
 print(f"{key:20}  {value: .2f}")
print("-------------------------------")
while True:
    food = input("Select an item (q to quit): ")
    if food.lower() =="q":
        break
    elif menu.get(food) is not None:
         cart.append(food)
print("---------Your Order-----------")
for food in cart:
    total += menu.get(food)
    print(food,end="   ")
print()
print(f"Total is: {total: .2f}")
#From this program i learn about dictionaries and their keys and values and how to call them and access them.