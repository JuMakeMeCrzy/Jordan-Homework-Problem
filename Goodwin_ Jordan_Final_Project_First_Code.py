def calculate_budget():
    # Step 1: Get income from the user
    income_sources = input("Enter your income sources separated by spaces: ").split()
    income_list = [float(i) for i in income_sources]  # Convert strings to floats
    total_income = sum(income_list)
    
    # Step 2: Get expenses from the user
    expense_sources = input("Enter your expenses separated by spaces: ").split()
    expense_list = [float(e) for e in expense_sources]  # Convert strings to floats
    total_expenses = sum(expense_list)
    
    # Step 3: Calculate remaining balance
    remaining_balance = total_income - total_expenses
    
    # Step 4: Display the results
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}")
