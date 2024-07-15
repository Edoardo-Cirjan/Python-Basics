# Make a list of your favorite shoes and print the 5th one. Print shoe called: Bape

fav_shoes = ["Jordan", "Nike", "New Balance", "Adidas", "Bape", "Louis Vuitton"]

print(fav_shoes[4])

# Make a list of your favorite numbers and print the 7th one. Print number: 21

fav_numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print(fav_numbers[6])

# Length of a created list

fav_shoes = ["Jordan", "Nike", "New Balance", "Adidas", "Bape", "Louis Vuitton"]

print(len(fav_shoes))

# Adding shoes into the list

fav_shoes.append("Maison Margiela")

print(len(fav_shoes))

# Figure out in what location was "Maison Margiela" added

print(fav_shoes)

# Adding shoes in a precise location inside the list (between "Adidas" and "Bape")

fav_shoes.insert(4, "Puma")

print(fav_shoes)

# Removing shoes from the list ("Adidas")

del (fav_shoes[3])
print(fav_shoes)

# Remove until there is only the shoe called "New Balance" on the list

fav_shoes = ['Jordan', 'Nike', 'New Balance', 'Adidas', 'Puma', 'Bape', 'Louis Vuitton', 'Maison Margiela']
del (fav_shoes[0])
del (fav_shoes[0])
del (fav_shoes[1])
del (fav_shoes[1])
del (fav_shoes[1])
del (fav_shoes[1])
del (fav_shoes[1])

print(fav_shoes)

fav_numbers = [1, 2, 3, 4, 5, 6]
print(fav_numbers[5])

# Loops
for number in range(10):
    print("number")

fav_shoes = ["Jordan", "Nike", "New Balance", "Adidas", "Bape", "Louis Vuitton"]

# Loop 60 times and print the number of the loop times 2.
for x in fav_shoes:
    print(x)

for x in range(10):
    if x % 2 == 0:
        print(x)
    else:
        print("odd")

for number in range(60):
    print((number + 1) * 2)

# Dictionaries
cats = {"Catrice": 6, "Thomas": 9, "Benji": 2}

# Print age of the cats - You cannot access the key from a value

print(cats["Catrice"], cats["Thomas"], cats["Benji"], )

# Add an item to the dictionary

cats = {"Catrice": 6, "Thomas": 9, "Benji": 2}

cats["Michael"] = 5

print(cats)

# Remove an item from the dictionary & find the length of it

cats = {"Catrice": 6, "Thomas": 9, "Benji": 2}

cats["Michael"] = 5
del (cats["Catrice"])
len(cats)

print(cats)
print(len(cats))

# Create a dictionary with Ints for Keys and Booleans for values

dictionary = {22: True, 33: False, 44: False, 55: True, 66: False}
print(dictionary)

# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False


# Determine the sum of all even numbers
def your_code():
    new_numbers = []
    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

    for p in numbers:
        if p % 2 == 0:
            new_numbers.append(p)
        return sum(new_numbers)


your_code()


# Alternative approach

def your_code_2():
    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
    total = 0
    for number in numbers:
        remainder = number % 2

        if remainder == 0:
            total = total + number

    return total


your_code_2()
