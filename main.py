# grade_calculator.py
# This program calculates a student's final grade and letter grade.

def calculate_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Student Grade Calculator")

    assignment = float(input("Enter assignment average: "))
    quiz = float(input("Enter quiz average: "))
    exam = float(input("Enter exam average: "))

    final_score = (assignment * 0.4) + (quiz * 0.2) + (exam * 0.4)
    letter_grade = calculate_letter_grade(final_score)

    print("\nFinal Results")
    print("Final Score:", round(final_score, 2))
    print("Letter Grade:", letter_grade)


main()
