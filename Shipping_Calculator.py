item = int(input("How many items do you have? "))
ship_price = item / item * 10.95
ship_price_two = (item - 1) * 2.95
total_shipping = ship_price + ship_price_two
print("You have",item ,"items. Your total shipping comes to:", total_shipping) 
