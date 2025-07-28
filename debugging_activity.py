# nelson woerk

# code snippet 1
x = 10
y = 2 # can't divide by 0
result = x / y
print('Result: ', result)

# code snippet 2
number = [1 ,2 ,3 ,4 ,5]
for i in range(len(number)):
    print(number[i]) # remove - 1

# code snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area #missing colon

radius = 5
print(calculate_area(radius))

# code snippet 4
def is_even(number):
   if number % 2 == 0:
       return True
   else: #missing colon
       return False
 
print(is_even(4))
print(is_even(7))

# code snippet 5
for i in range (5): #missing colon error
    print(i)
   
   
 # code snippet 6
def greet(name):
    return "hello, " + name # missing + sign

# code snippet 7
numbers = [1, 2, 3, 5]
sum = 0
for numbers in numbers:
    sum += numbers #IndetationError
    print("sum of numbers: ", sum)

# code snippet 8
def factorial(n): # correct, no error
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

# code snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # always evaluate to true
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# code snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "can't devide by zero!"
    else:
        result = x + y
        return result
num1 = 10
num2 = 0 # can't dived by zero
print(divide_numbers(num1, num2))

#that alot of work lol