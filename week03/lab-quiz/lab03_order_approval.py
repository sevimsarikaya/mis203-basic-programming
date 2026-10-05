# INPUTS 
order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member = input("Is customer a member? (yes/no): ").lower() == "yes"

# CHECK STOCK & QUANTITY 
if requested_quantity <= 0 or requested_quantity > available_stock:
    print("\nStatus: REJECTED")
    print("Reason: Invalid quantity or insufficient stock.")

# APPROVED ORDER & DISCOUNT 
else:
    print("\nStatus: APPROVED")
    print("Reason: Quantity and stock are valid.")
    
    # Apply 10% discount if member and amount >= 500
    if is_member and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Discount: 10% applied.")
    else:
        final_price = order_amount
        print("Discount: No discount.")
        
    print(f"Final Price: {final_price:.2f} TRY")