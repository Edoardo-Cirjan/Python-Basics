# Tuples - have specific order, items can't be changed, () used to enclose items

# Child's birth information exercise
child1_birth = ("Alex", "St. Mary Children Hospital", "New York", "United States", "06/22/2020", "08:44")
child2_birth = ("Marry", "Washington Hospital", "Fremont", "California", "United States", "08/12/2019", "04:32")

# Print the type of the variables
print(type(child2_birth))
print(type(child2_birth))

# Print the information inside the tuple
print(child1_birth)
print(child2_birth)

# Extract specific information of the first child as followed: name, hospital of birth, country and date
name = child1_birth[0]
hospital_of_birth = child1_birth[1]
country_of_birth = child1_birth[3]
date_of_birth = child1_birth[4]

# Printing the extracted information
print(f"Name: {name}")
print(f"Hospital of Birth: {hospital_of_birth}")
print(f"Country of Birth: {country_of_birth}")
print(f"Date of Birth: {date_of_birth}")
