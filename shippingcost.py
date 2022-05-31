print('Shipping Calculator')
print('')

shipping_cost = 0
total_cost = 0

cont = 'y'

while cont == 'y' or cont == 'Y':
    items_cost = float(input('Cost of items ordered: '))
    if items_cost <= 0:
        print('You must enter a positive number. Please try again.')
        continue
    elif items_cost < 30:
        shipping_cost = 5.95
    elif items_cost >= 30 and items_cost <= 49.99:
        shipping_cost = 7.95
    elif items_cost >= 50 and items_cost <= 74.99:
        shipping_cost = 9.95
    else:
        shipping_cost = 0
    
    total_cost = shipping_cost + items_cost
    print('Shipping Cost: {:.2f}'.format(shipping_cost))
    print('Total cost: {:.2f}'.format(total_cost))
    cont = input('Continue? (y/n): ')

print('Bye!')
