print("Welcome to the Bill Calculator!")
print("Enter the total amount of your bill: $")
total_bill = float(input())
print("Enter the tip percentage you would like to give (e.g., 15 for 15%): ")
tip_percentage = float(input())
tip_amount = (tip_percentage / 100) * total_bill
final_amount = total_bill + tip_amount
print("The total number of people sharing the bill: ")
num_people = int(input())
amount_per_person = final_amount / num_people
print(f"The total bill amount is: ${final_amount:.2f}")
print(f"The tip amount is: ${tip_amount:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")
print("Thank you for using the Bill Calculator!")   