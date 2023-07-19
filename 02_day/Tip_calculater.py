print("Welcome to the Tip calculator!")

bill = float(input("What was the Total Bill: $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
people = int(input("How many people are spliting this bill: "))

bill_with_tip = tip / 100 * bill + bill 


final_bill = bill_with_tip / people
your_bill = "{:.2f}".format(final_bill)        # round(final_bill, 2)

print(f"Each person should pay: ${your_bill}")
