item_name = input("Enter item name")
item_price = int(input("Enter item price:"))
dis_card = input("Discount card? 'True'/'False'").lower()

if dis_card == "true":
    item_price-=(item_price/100)*25
else:
    pass
print(item_name)
print(item_price)
