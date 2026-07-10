# This program converts temperature between Celsius, Fahrenheit, and Kelvin.
# The user is prompted to enter a temperature value and the unit of that temperature (C for Celsius, F for Fahrenheit, or K for Kelvin). The program then performs the necessary calculations to convert the temperature to the other two units and displays the results. If the user enters a temperature below absolute zero (-273.15°C), the program will notify them that this is not possible and exit.
# The program also checks for valid unit input and will exit if the user enters an invalid unit. The results are rounded to two decimal places for clarity.
Temperature = float(input("Enter the temperature: "))
if Temperature < -273.15:
    print("Temperature cannot be below absolute zero (-273.15°C).")
    print("Please enter a valid temperature.")
    exit()
unit = input("Enter the unit of temperature (C or F or K): ")
if unit == "C" or unit == "c":
    temperature_in_f = (Temperature * 9/5) + 32
    temperature_in_k = Temperature + 273.15
    print(f"Your temperature in Fahrenheit is: {round(temperature_in_f, 2)} F")
    print(f"Your temperature in Kelvin is: {round(temperature_in_k, 2)} K")
elif unit == "F" or unit == "f":
    temperature_in_c = (Temperature - 32) * 5/9
    temperature_in_k = (Temperature - 32) * 5/9 + 273.15
    print(f"Your temperature in Celsius is: {round(temperature_in_c, 2)} C")
    print(f"Your temperature in Kelvin is: {round(temperature_in_k, 2)} K")
elif unit == "K" or unit == "k":
    temperature_in_c = Temperature - 273.15
    temperature_in_f = (Temperature - 273.15) * 9/5 + 32
    print(f"Your temperature in Celsius is: {round(temperature_in_c, 2)} C")
    print(f"Your temperature in Fahrenheit is: {round(temperature_in_f, 2)} F")
else:
    print("Invalid unit. Please enter 'C', 'F', or 'K'.")
    exit()