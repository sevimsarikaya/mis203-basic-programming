def main():
    print("=== Savings Goal Planner ===")

    # 1. Get and validate user inputs using while loops
    starting_balance = float(input("Enter starting balance: "))
    while starting_balance < 0:
        print("Starting balance cannot be negative!")
        starting_balance = float(input("Enter starting balance: "))

    monthly_deposit = float(input("Enter monthly deposit: "))
    while monthly_deposit <= 0:
        print("Monthly deposit must be greater than zero!")
        monthly_deposit = float(input("Enter monthly deposit: "))

    interest_rate = float(input("Enter monthly interest rate (%): "))
    while interest_rate < 0:
        print("Interest rate cannot be negative!")
        interest_rate = float(input("Enter monthly interest rate (%): "))

    savings_goal = float(input("Enter savings goal: "))
    while savings_goal <= 0:
        print("Savings goal must be greater than zero!")
        savings_goal = float(input("Enter savings goal: "))

    # 2. Check if starting balance already reaches the goal
    if starting_balance >= savings_goal:
        print("\nStarting balance already meets or exceeds the goal!")
        print(f"Final Balance: ${starting_balance:.2f}")
        print("Total Interest Earned: $0.00")
        return

    # 3. Monthly simulation setup
    balance = starting_balance
    total_interest = 0.0
    goal_reached = False
    months = 0

    print("\nMonth | Interest Earned | New Balance")
    print("-" * 38)

    # Simulate for a maximum of 60 months
    for month in range(1, 61):
        months = month
        
        # Calculate interest for the current month
        interest = balance * (interest_rate / 100)
        total_interest += interest
        
        # Update current balance with interest and monthly deposit
        balance += interest + monthly_deposit

        # Print monthly results in a clean table row
        print(f"{month:<5} | ${interest:<14.2f} | ${balance:.2f}")

        # Stop the loop early if the savings goal is reached
        if balance >= savings_goal:
            goal_reached = True
            break

    # 4. Print final results
    print("-" * 38)
    if goal_reached:
        print(f"Goal reached in {months} month(s)!")
    else:
        print("Goal was NOT reached within 60 months.")

    print(f"Final Balance: ${balance:.2f}")
    print(f"Total Interest Earned: ${total_interest:.2f}")


if __name__ == "__main__":
    main()