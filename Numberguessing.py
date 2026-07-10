a = int(input("Enter a number: "))
print("Give a range of numbers to guess from: 1 to 500")
import random
number_to_guess = random.randint(1, 500)
while True:
    if a < number_to_guess:
        print("Too low! Try again.")
    elif a > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
    a = int(input("Enter a number: ")) # This code will prompt the user to enter a number and then compare it to a randomly generated number between 1 and 100. If the user's guess is too low, it will print "Too low! Try again." If the user's guess is too high, it will print "Too high! Try again." If the user's guess is correct, it will print "Congratulations! You guessed the number." The loop will continue until the user guesses the correct number.
#In this code i use binary search techinque to guess the number. The user will be prompted to enter a number and then the program will compare it to the randomly generated number. If the user's guess is too low, the program will print "Too low! Try again." If the user's guess is too high, the program will print "Too high! Try again." If the user's guess is correct, the program will print "Congratulations! You guessed the number." The loop will continue until the user guesses the correct number.