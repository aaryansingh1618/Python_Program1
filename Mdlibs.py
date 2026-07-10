# This is a simple Mad Libs game in Python that prompts the user for various words and then constructs a short story using those words.
# The program uses the input() function to get user input and the f-string formatting to insert the user's words into the story.
# The story is about a visit to a zoo, and the user is asked to provide an adjective, a noun, another adjective, a verb ending with 'ing', and a final adjective. The program then prints out the completed story using the words provided by the user.
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description): ")
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")