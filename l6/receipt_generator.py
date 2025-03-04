
from datetime import datetime

# 1. Yoghurt:  N1000

now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%Y-%m-%d")
total = 0
items = []

def print_receipt():
    print("\n......Giftcares........")
    print(f"Date: {date}\nTime: {time}")
    print("..................................")
    print("s/n \tName \tAmount")
    print("..................................")

    for i, name_price in enumerate(items, start = 1):
        print (f"{i}. {name_price[0]} : N{name_price[1]}")
    
    print("...................................")
    print(f"Total : {total}")
    print(".....................................")
    print ("Thanks for your patronage 🤗")

while True :
    name =  input("\nEnter name of item [Enter 'q' to quit]: ")
    if name.lower() == 'q' :
        break
    price = int(input("Enter the price of the item: "))

    total += price
    items.append([name,price])

print_count = int(input("\nEnter print count: "))

print_receipt()