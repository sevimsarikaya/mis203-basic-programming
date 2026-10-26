"""
Difference between print and return:
- print(): Displays the output on the console screen. 
  It does not return or save any value, so it cannot be used in further calculations.
- return: Sends the calculated result back from the function to the program. 
  This value can be saved in a variable and used in other calculations.
"""
#Functions for calculating subtotal, discount rate, shipping fee, and final total
def calc_subtotal(price, quantity):
    return price * quantity

def calc_discount_rate(subtotal):
    if subtotal >= 200:
        return 0.10
    else:
        return 0.0

def calc_shipping_fee(subtotal):
    if subtotal >= 150:
        return 0
    else:
        return 25

def calc_final_total(subtotal, discount_rate, shipping_fee):
    discount_amount = subtotal * discount_rate
    return (subtotal - discount_amount) + shipping_fee

# Assert checks
assert calc_subtotal(10, 5) == 50 # Subtotal calculation
assert calc_discount_rate(200) == 0.10 # Threshold boundary check for discount (At/Above boundary: 200 TL -> 10% discount)
assert calc_discount_rate(199) == 0.0 # Threshold boundary check for discount (Below boundary: 199 TL -> 0% discount)
assert calc_shipping_fee(150) == 0 #Threshold boundary check for shipping (At/Above boundary: 150 TL -> 0 TL fee)
assert calc_shipping_fee(149) == 25 #Threshold boundary check for shipping (Below boundary: 149 TL -> 25 TL fee)

#3.SAMPLE ORDERS

# Order 1 ( Small order - subtotal < 200 )
order1_price = 40
order1_quantity = 2

order1_subtotal = calc_subtotal(order1_price, order1_quantity)
order1_discount_rate = calc_discount_rate(order1_subtotal)
order1_shipping_fee = calc_shipping_fee(order1_subtotal)
order1_final_total = calc_final_total(order1_subtotal, order1_discount_rate, order1_shipping_fee)

print("--- ORDER 1 ---")
print(f"Subtotal: {order1_subtotal} TL")
print(f"Discount Rate: {order1_discount_rate * 100}%")
print(f"Shipping Fee: {order1_shipping_fee} TL")
print(f"Final Total: {order1_final_total} TL\n")

# Order 2 ( Large order - subtotal >= 200 )
order2_price = 100
order2_quantity = 3

order2_subtotal = calc_subtotal(order2_price, order2_quantity)
order2_discount_rate = calc_discount_rate(order2_subtotal)
order2_shipping_fee = calc_shipping_fee(order2_subtotal)
order2_final_total = calc_final_total(order2_subtotal, order2_discount_rate, order2_shipping_fee)

print("--- ORDER 2 ---")
print(f"Subtotal: {order2_subtotal} TL")
print(f"Discount Rate: {order2_discount_rate * 100}%")
print(f"Shipping Fee: {order2_shipping_fee} TL")
print(f"Final Total: {order2_final_total} TL")