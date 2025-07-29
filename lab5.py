# lab 5 nelson ramos gonon
# step 1
def cat_greeting(word):
    print(f'cat says {word}')
    print('cat says nothing')

cat_greeting("meow")

# step 2
def generate_superhero_power():
    name = "Johnny"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# step 3
def generate_superhero_power1():
    power = "flying"
    return power

print(generate_superhero_power1())

# step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of" + super_power + "!"
    return message

print(generate_superhero_power2("manica", " super human strength"))

# step 5
def cat_greeting_loop(greeting):
    for i in range(5):
        print(f'the cat says {greeting}')

cat_greeting_loop("meow")

# step 6

def generate_multiple_powers(powers):
    for i in powers:
     print(i)

    power_super = ["teleport", "flying", "speed", "strength"]
    generate_multiple_powers(power_super)

