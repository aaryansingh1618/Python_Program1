import time 
# This program is a simple clock timer that displays the current time in hours, minutes, and seconds. It uses the time module to get the current local time and formats it for display. The program runs in an infinite loop, updating the time every second. The user can exit the program by pressing Ctrl+C.
# This Program Tell Two Things One is current time and other feture is timer which is used to set a timer for a specific duration. The user can input the duration in seconds,minutes,Hours and the program will count down from that duration to zero, displaying the remaining time in minutes and seconds format. When the timer reaches zero, it will print "Time's up!" to notify the user that the countdown has finished.
class ClockTimer:
    def __init__(self):
        pass

    def display_current_time(self):
        while True:
            current_time = time.strftime("%H:%M:%S")
            print("Current Time:", current_time, end="\r")
            time.sleep(1)

    def set_timer(self, duration):
        print(f"Timer set for {duration} seconds.")
        while duration:
            mins, secs = divmod(duration, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Time Remaining:", timer, end="\r")
            time.sleep(1)
            duration -= 1
        print("\nTime's up!")
clock_timer = ClockTimer()
input_choice = input("Enter '1' to display current time or '2' to set a timer: ")
if input_choice == '1':
    clock_timer.display_current_time()
elif input_choice == '2':
    duration = int(input("Enter the duration for the timer in seconds: "))
    clock_timer.set_timer(duration)
else:
    print("Invalid choice. Please enter '1' or '2'.")

