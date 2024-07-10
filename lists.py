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
