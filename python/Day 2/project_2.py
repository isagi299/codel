# tip calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percent /=100
percent+=1
people = int(input("How many people to split the bill? "))
per_p = (bill/people) * percent
final_bill = "{:.2f}".format(per_p)
print(f"Each person should pay: ${final_bill}")

