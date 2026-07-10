# Interest Calculator Program 
# This program calculates both simple and compound interest based on user input for principal, rate, and time.
class InterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def calculate_compound_interest(self, n):
        return self.principal * ((1 + (self.rate / (n * 100))) ** (n * self.time)) - self.principal
    def display_results(self):
        simple_interest = self.calculate_simple_interest()
        compound_interest = self.calculate_compound_interest(1)  # Assuming n=1 for annual compounding
        profit = compound_interest - simple_interest
        print(f"Principal: {self.principal}")
        print(f"Rate: {self.rate}%")
        print(f"Time: {self.time} years")
        print(f"Simple Interest: {simple_interest:.2f}")
        print(f"Compound Interest (annually): {compound_interest:.2f}")
        print(f"Profit from Compound Interest: {profit:.2f}")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
calculator = InterestCalculator(principal, rate, time)
calculator.display_results()