# FIXME (1): Finish reading item price and quantity, then output a receipt
item_name = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quan = int(input('Enter item quantity:\n'))
total = item_price * item_quan 

print()
print('RECEIPT')
print(item_quan, item_name, '@', ('${:.2f}'.format(item_price)), '=', ('${:.2f}'.format(total)))
print('Total cost:', ('${:.2f}'.format(total)))
print()
print()
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
item_name2 = input('Enter second food item name:\n')
item_price2 = float(input('Enter item price:\n'))
item_quan2 = int(input('Enter item quantity:\n'))
item_cost = item_price2 * item_quan2
total2 = (item_price2 * item_quan2) + total

print()
print('RECEIPT')
print(item_quan, item_name, '@', ('${:.2f}'.format(item_price)), '=', ('${:.2f}'.format(total)))
print(item_quan2, item_name2, '@', ('${:.2f}'.format(item_price2)), '=', ('${:.2f}'.format(item_cost)))
print('Total cost:', ('${:.2f}'.format(total2)))
print()
# FIXME (3): Add a gratuity and total with tip to the second receipt
gratuity = 0.15 * total2
final = gratuity + total2

print('15% gratuity:', ('${:.2f}'.format(gratuity)))
print('Total with tip:', ('${:.2f}'.format(final)))