#Variables to store total sales data
tickets_sold = 0
total_revenue = 0
free_tickets = 0

# Main loop runs until the user decides to quit
while True: 
    # 1. Get customer's name
    name =input("Customer name(or q to quit):")
    if name == "q" or name == "Q":
        break #Exit the loop
   
 # 2. Get and validate age
    age = int(input("Age:"))
    if age < 0 or age > 120:
        print("Invalid age. ")
        continue #Go back to the start of the loop
    
    # 3. Get and validate day
    day = input("Day (weekday/weekend):").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day. ")
        continue #Go back to the start of the loop
   
    # 4. Get and validate student status
    student = input("Student (yes/no):").lower()
    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue #Go back to the start of the loop

    # 5. Set base ticket price
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250

    # 6. Calculate discount and category in order
    if age < 6:
        discount = 1.0 # 100% discount (Free)
        category = "Free"
    elif age >= 65:
        discount = 0.50 # 50% discount
        category = "Senior"
    elif age <= 12: #Age is between 6 and 12
        discount = 0.40 # 40% discount
        category = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30 # 30% discount
        category = "Student"
    else:
        discount = 0.0 # No discount
        category = "Standard"

    # Calculate final ticket price
    price = base_price * (1 - discount)

    # Print individual result formatted with 2 decimal places
    print(f"{name}: {price:.2f} TRY ({category})")

    # Update total stats
    tickets_sold = tickets_sold + 1
    total_revenue = total_revenue + price
    if discount == 1.0:
        free_tickets = free_tickets + 1

# Print final summary after loop ends
if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Total tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average ticket price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
