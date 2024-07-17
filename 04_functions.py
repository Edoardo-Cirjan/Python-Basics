# Functions:
# Create a function called meow that prints "meow meow!" and one that prints "I am a cat!"
def meow():
    print("meow meow!")
    print("I am a cat!")


# For loop the function:
for x in range(1):
    meow()


# Create a function called meow that prints "Hellow my name is Edi!" and one that prints "I am learning this!"
def hello():
    print("Hellow my name is Edi!")
    print("I am learning this!")


hello()


# Parameters:

def game(name):
    print(f"I like this game called {name}")


game("Battlefield")
game("Apex Legends")
game("Need for Speed")


# Having more than one parameter

def add_numbers(num1, num2):
    print(num1 * num2)


add_numbers(68, 98)
add_numbers(98, 77)


# Create a function called dog_info that takes in a dog's age and name and prints a sentence about the dog
def dog_info(age, name):
    print(f"Hi my name is {name} and i am {age} years old!")


dog_info(7, "Rex")


# Returning

def double(number):
    return number * 2


new_number = double(100)

print(new_number)


# Crate a function that returns a string in all caps:
def uppercase(text):
    return text.upper()


print(uppercase("good"))

names = ["really bad", "bad", "average", "above average", "good", "really good"]

for name in names:
    print(uppercase(name))

# Input
# First ask for some text, and the prompt "Enter 1 to uppercase or 2 to lowercase: "

user_text = input("Enter some text: ")

upp_or_lower = input("Enter 1 to uppercase or 2 to lowercase: ")

if upp_or_lower == "1":
    print(user_text.upper())
else:
    print(user_text.lower())
