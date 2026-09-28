#1.inputs for Item 1
item1_name = input("Enter Item 1 Name:")
item1_qty = int(input("Enter Item 1 Quatity:")
item1_price = float(input("Enter Item 1Unit Price:"))
#2. inputs for Item 2
item2_name = input(Enter Item 2 Name:")
item2_qty = int(input("Enter Item 1 Quatity:"))
item2_price = Float(input("Enter Item 2 Quatity:"))
#3.Inputs for delivery and tax
delivery_fee = float(input("Enter Delivery Fee:"))
tax_rate = float(input("Enter Tax Rate (%):"))
#4.Calculations
item1_subtotal = item1_qty * item1_price
item2_subtotal = item2_qty * item2_price
items_subtotal = item1_subtotal + item2_subtotal

tax_amount = items_subtotal * (tax_rate / 100)
final_total = items_subtotal + tax_amount + delivery_fee

#5.output display
print(" PURCHASE QUOTE ")
print(f"{item1_name} ({item1_qty} x {item1_price:.2f}) : {item1_subtotal:.2f} TRY")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f}) : {item2_subtotal:.2f} TRY")

print(f"Items Subtotal : {items_subtotal:.2f} TRY")
print(f"Tax ({tax_rate:.0f}%") :{tax_amount:.2f} TRY")
print(f"Delivery Fee : {delivery_fee:.2f} TRY")
print(f"FINAL TOTAL : {final_total:.2f} TRY")
               
