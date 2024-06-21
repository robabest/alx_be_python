income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
Monthly_Savings = income - expense
Projected_Savings = float(Monthly_Savings) * 12 + float(Monthly_Savings * 12 * 0.05)
print("Your monthly savings are $" + str(Monthly_Savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(int(Projected_Savings)) + "." )
