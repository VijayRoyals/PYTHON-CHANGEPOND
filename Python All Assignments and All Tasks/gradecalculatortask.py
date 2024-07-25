def grade_calculator(grades):
    total_marks = sum(grades.values())
    num_subjects = len(grades)
    average_grade = total_marks / num_subjects
    return average_grade


grades = {
    'Math': 85,
    'Science': 90,
    'History': 88,
    'English': 82,
    'Art': 78
}

average_grade = grade_calculator(grades)
print(f"Average grade: {average_grade}")




def input_marks():
    marks = {}
    subjects = ["REACT", "PYTHON", "JAVA", "CLOUD DEVOPS"]

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter the mark for {subject}: "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100. Please try again.")
                else:
                    marks[subject] = mark
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return marks

def calculate_grade(marks):
    total_marks = sum(marks.values())

    if total_marks >= 400:
        return "Your Grade: O :)"
    elif total_marks >= 300:
        return "Your Grade: A"
    elif total_marks >= 200:
        return "Your Grade: B"
    else:
        return "Your Grade: F"

def main():
    marks = input_marks()
    print("\n________Result_________")
    print(calculate_grade(marks))

if __name__ == "__main__":
    main()
