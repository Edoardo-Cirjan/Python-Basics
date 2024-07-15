#variables - holds information that changes overtime: numbers, text 
wallet = 70 

print(wallet) 

wallet = 16 
 
print(wallet)


# Ints and floats
# Ints = integer
day = 12

temp = -3

# floats =  decimal place connected to them
weight = 190.422  # => FLOAT - can be positive or negative like integer

print(temp * 3)


bananas = 8544
apples = 774

shirt = "5"

workplace = "Anchor Plaza\'s the place 'of' work"

movie = "National Treasure\'s the 'best' movie"

print(movie)


# Using variables in strings
white = "bear"
orange = "fox"
grey = "seal"
where = "in the wild"

print(f"I went hunting and found 3 animals with 3 different colors: {white}, {orange} and {grey}. I found them {where}")


# Boolean with CAPS - either True OR False
# Holds value when used with IF Statement
light_is_on = False

if light_is_on:
    print ("The light is on")


bottle_is_empty = True

if bottle_is_empty:
    print("I drank the water")
print("asdasd")


i_need_more_cigs = False

if i_need_more_cigs:
    print("Out of cigs!")


# Comparison AND Else
weight = 100
light_is_on = (weight < 80)

if light_is_on:
    print("The light is on!")
else:
    print("We're in the dark!")


weight = 81

if weight <= 101:
    print("You're under weight :)")
else:
    print("Good to go :)")


age = 13
if age >= 18:
    print("You're an adult!:)")
else:
    print("You're a child! :)")




