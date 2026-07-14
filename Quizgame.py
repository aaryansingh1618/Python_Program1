#This is a quiz program in which you give your answer by options and then after completion you get your score
questions =("Who is the CEO of JP Morgan: ",
            "Who is first trillionaire in the world: ",
            "Which Launguage widely used in AI/ML: ",
            "where are most tech companiesnare in india: ",
            "When Will i become a Billionaire")
options = (("A. Jamie Dimon", "B. Modi ","C. Charles Schwab","D. Chage Huges"),
           ("A. Bill Gates ", "B. Sundar Pichai","C. Sam Altman","D. Elon Musk"),
           ("A. Python","B. Java","C. R Programming ","D. Rust"),
           ("A. Banglore","B. Delhi","C. Haryana","D. Bilaspur"),
           ("A. 2027","B. 2028","C. 2030","D. 2032"))
answers= ("A","D","A","A","C")
guesses = []
score = 0
question_num = 0
for question in questions:
   print("--------------------------")
   print(question)
   for option in options[question_num]:
    print(option)
   guess = input("Enter one option out of(A,B,C,D): ").upper()
   guesses.append(guess)
   if guess == answers[question_num]:
     score +=1
     print("Correct!")
   else:
     print("Incorrect!")
     print(f"{answers[question_num]} is the correct option")
   question_num += 1
print("---------------------")
print("       RESULT")
print("---------------------")
print("Answers: ",end=" ")
for answer in answers:
 print(answer, end=" ")
print()
print("Guesses: ",end=" ")
for guess in guesses:
 print(guess, end=" ")
print()
score =int(score / len(questions) * 100)
print(f"Your score is: {score}%")