# mis203-basic-programming 

* **Name:** Sevim Sarıkaya
* **Student Number:** [2404109006]
* **Department:** Management Information Systems
* **Course Name:** MIS203 Basic Programming

---

### AI Usage Information / week01
* **AI Tool Used:** Gemini
* **Prompt Used:** "Write a simple Python program that asks the user for their Name, Department, Age, and Career Goal, then prints a formatted Student Profile."
* **What did you change?:** I reviewed the generated code and verified that the output structure matched the required assignment format.

---

## Week 02

* **AI Tool Used:** Gemini
* **Prompt Used:** "Create a Python program using while True, break, and continue to calculate student letter grades and average scores."
* **What did you change?:** I made the code simpler by using float conversion instead of try-except blocks, and I checked that the output matches the assignment requirements.
* **What does break do in your program?:** The break statement stops the infinite loop immediately when the user enters 'q' for the student name.

---

## Week 03
* **AI Tool Used:** Gemini
* **Prompt Used:** "Write a Python program for a cinema ticket office simulation that validates user inputs (age, day, student status) in a loop, applies conditional discount logic based on strict rule priorities, and prints formatted receipts and sales summaries."
* **What did you change?:** "I simplified the code structure to match class topics, added strict input validation to handle invalid entries, and verified that all outputs match the assignment format exactly." 
* **Tests:**
    1. 'Ali, 30, weekend, no' -> 'Ali: 250.00 TRY (Standard)'
    2. 'Can, 5, WEEKEND, no, -> 'Can: 0.00 TRY (Free)'
    3. 'Mert, 9, weekday, yes -> 'Deniz: 120.00 TRY (Child)'
* **Why does the order of the rules matter?:** "Python checks conditions from top to bottom and applies the first match. If the Student rule came before the Child rule, a 10-year-old student would get a 30% student discount instead of the higher 40% Child discount."

---

## Week 4 - Surprise Assignment

* **AI Tool Used:** Gemini
* **Prompt Used:** "Create a simple Python coffee program that matches coffee choices with popular songs, checks user input with a while loop, uses math and random libraries, and prints a simple receipt."
* **What did you change?:** I simplified the code to fit our class topics. I removed complex error blocks, added B1-level English comments, replaced date formatting with the math library, and added matching songs for each coffee type's mood.
* **Libraries Used:** 
  1. `random`: I used `random.choice()` to pick a random song from the coffee's song list.
  2. `math`: I used `math.ceil()` to round up the total price to a whole number.
* **Tests:**
  1. Ceylin, Choice 1 (Espresso), 1 cup -> Total: 100 TRY | Song: Dua Lipa - Training Session | Note: Enjoy your day!
  2. Mert, Choice 8 (Invalid) -> Choice 2 (Latte), 1 cup -> Warning shown, then Total: 180 TRY | Song: Coldplay - Yellow | Note: Enjoy your day!
  3. Sevda, Choice 3 (Filter Coffee), 2 cups -> Total: 200 TRY | Song: Imagine Dragons - Believer | Note: High caffeine alert! Drink water too.
* **Why did we use a while loop?:** We used the while loop to check the user's choice. If the user types a number outside 1-4, the program asks again until they enter a valid option. This stops the program from crashing.