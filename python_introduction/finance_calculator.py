monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_saving = monthly_income - monthly_expenses
projected_Savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_Savings}.")


# Enter your monthly income: 5000
# Enter your total monthly expenses: 4000
# Your monthly savings are $1000.
# Projected savings after one year, with interest, is: $12600.