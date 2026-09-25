total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")
    
    # Exit the loop if the user enters 'q'
    if name == "q":
        break
        
    # Get the score from the user as a string
    score_input = input("Enter score: ")
    
    # Convert the string input to a float number
    score = float(score_input)
    
    # Check if the score is between 0 and 100
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue  # Go back to the start of the loop
        
    # Determine the letter grade
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
        
    # Print the student's result
    print(f"{name}: {int(score) if score == int(score) else score} -> {letter_grade}")
    
    # Update total score and student count
    total_score += score
    student_count += 1

# Print final results after the loop ends
if student_count > 0:
    average_score = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average_score:.2f}")
else:
    print("No students entered.")
