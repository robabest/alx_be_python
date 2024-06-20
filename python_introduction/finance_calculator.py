monthlyincome = int(input("Enter your monthly income:"))
monthlyexpense = int(input("Enter your total monthly expenses: "))
monthlysaving = monthlyincome - monthlyexpense
projectedsaving = monthlysaving * 12 + (monthlysaving * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",projectedsaving) 
