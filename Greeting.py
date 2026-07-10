Time = int(input("Enter the time in hours (0-12): "))
Time2 = str(input("AM or PM : ")).upper()
if Time2 == "AM":
    if 0 <= Time <= 12:
        print("Good morning!")
    else:
        print("Invalid time entered. Please enter a value between 0 and 11.")
elif Time2 == "PM":
    if 0 <= Time < 4:
        print("Good afternoon!")
    elif 4 <= Time < 8:
        print("Good evening!")
    elif 8 <= Time < 12:
        print("Good night!")
    else:
        print("Invalid time entered. Please enter a value between 0 and 11.")
else:
    print("Invalid input for AM/PM. Please enter 'AM' or 'PM'.")