menu = {'pizza' : 2.99, 'burger' : 3.99, 'hot dog' : 1.99, 'cheese' : 0.59, 'ice cream' : 1.49, 'churro' : 0.79, 'soda' : 0.89}

# step 2
def total_price(item1,item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum

total_price('pizza', 'burger')

# step 3
def total_difference(item1, item2):
    difference = abs(menu[item1] - menu[item2])
    return difference

total_difference('ice cream', 'hot dog')

# step 4
def inflation(item, number):
    menu[item] = menu[item] * number
    return menu

inflation('soda', 2)

# step 5
def inflation(item, number):
 menu[item] = menu[item] / number
 return menu

#step 6
def discount(item, discount):
   total_sum = menu[item] - discount
   return total_sum
