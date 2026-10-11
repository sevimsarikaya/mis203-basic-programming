import math
import random

print("=== COFFEE & MUSIC MATCH ===")

# Customer details
user_name = input("Enter your name: ")
print("Select your coffee:")
print("1 - Espresso (100 TRY) [Strong & Energetic]")
print("2 - Latte (180 TRY) [Smooth & Relaxing]")
print("3 - Filter Coffee (100 TRY) [Focus & Study]")
print("4 - Caramel Macchiato (200 TRY) [Sweet & Trendy]")

# Get user choice
choice = input("Select (1-4): ")

# While loop: Repeats if the choice is not between 1 and 4
while choice != "1" and choice != "2" and choice != "3" and choice != "4":
    print("Invalid choice! Please select a number between 1 and 4.")
    choice = input("Select (1-4): ")

# Get coffee quantity
quantity_input = input("How many cups? ")
quantity = int(quantity_input)

# Set coffee details based on choice
if choice == "1":
    coffee_name = "Espresso"
    unit_price = 100.0
    song_list = ["Dua Lipa - Training Session", "Bariş Manço - Kara Sevda"]
elif choice == "2":
    coffee_name = "Latte"
    unit_price = 180.0
    song_list = ["Coldplay - Yellow", "Yuzyuzeyken Konusuruz - Sandal"]
elif choice == "3":
    coffee_name = "Filter Coffee"
    unit_price = 100.0
    song_list = ["Imagine Dragons - Believer", "Pinhani - Dunyadan Uzak"]
elif choice == "4":
    coffee_name = "Caramel Macchiato"
    unit_price = 200.0
    song_list = ["Mabel Matiz - A Canim", "Harry Styles - Watermelon Sugar"]

# Calculate price using math library
subtotal = quantity * unit_price
final_total = math.ceil(subtotal)

# Pick a random song from the list
suggested_song = random.choice(song_list)

# Set a special note based on quantity and choice
if choice == "3" and quantity >= 2:
    note = "High caffeine alert! Drink water too."
elif choice == "4":
    note = "Sweet choice! Enjoy your treat."
else:
    note = "Enjoy your day!"

# Print final result card
print("\n------------------------------")
print(f"Customer       : {user_name}")
print(f"Coffee Order   : {coffee_name} x {quantity}")
print(f"Total Price    : {final_total} TRY")
print(f"Suggested Song : {suggested_song}")
print(f"Note           : {note}")
print("------------------------------")