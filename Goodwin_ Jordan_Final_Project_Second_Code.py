def calculate_budget_with_categories():
    # Step 1: Get income from the user
    income_sources = input("Enter your income sources separated by spaces: ").split()
    income_list = [float(i) for i in income_sources]
    total_income = sum(income_list)
    
    # Step 2: Get expenses with categories
    expenses = {}
    while True:
        category = input("Enter expense category (or 'done' to finish): ")
        if category == 'done':
            break
        amount = float(input(f"Enter the amount for {category}: "))
        expenses[category] = amount

    total_expenses = sum(expenses.values())
    
    # Step 3: Calculate remaining balance
    remaining_balance = total_income - total_expenses
    
    # Step 4: Display the results
    print("\nTotal Income: ${total_income:.2f}")
    print("Total Expenses: ${total_expenses:.2f}")
    print("Remaining Balance: ${remaining_balance:.2f}")
    
    print("\nExpense Breakdown:")
    for category, amount in expenses.items():
        print("{category}: ${amount:.2f}")
