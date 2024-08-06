def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Test the functions
print(celsius_to_fahrenheit(0))  # Output: 32.0
print(fahrenheit_to_celsius(32))  # Output: 0.0


# Adding user input
def temperature_converter():
    choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()
    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid choice. Please type 'C' or 'F'.")


temperature_converter()

# Modules in Python
