food = 'pizza'
print(food[0:3])
print(food[-3:-1])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

number_list = [1, 13910, 13, -1000 ,0 , 1969]
number_list.append(67)
number_list.insert(3, 1000)


books = {'Jeff Kinney': 'Diary of a wimpy kid', 'Dav Pilkey': 'Dog Man', 'Lincoln Peirce': 'Big Nate'}
books.pop(list(book))