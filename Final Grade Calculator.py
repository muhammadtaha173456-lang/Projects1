#Practice Problem: Class grade avg calculator
# Final grade calculator

quiz_scores = float(input("Enter quiz averages: "))
lab_score = float(input("Enter lab averages: "))
exam_score = float(input("Enter exam score: "))
project_score = float(input("Enter project score: "))

final_grade = quiz_scores*.15 + lab_score*.25 + exam_score*.4 + project_score*.2

print(f"The final grade is {final_grade}")

