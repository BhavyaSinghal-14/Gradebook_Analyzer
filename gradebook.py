"""
Author: Bhavya Singhal
Date: November 5, 2025
Title: Gradebook Analyzer
Description:— A GradeBook Analyzer that collects student names and marks through manual input and computes various statistics, grades, and summaries automatically.
"""
import statistics

#Task1: 

def welcome_message():
    print(" Welcome to Gradebook Analyzer")
    print("\nMenu:")

#Task2: 

def get_student_data():

    marks = {}
    n = int(input("\nHow many students are in the class? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        mark = int(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks

#Task3:

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

def show_statistics(marks):
    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)

    print("\nStatistics")
    print(f"Average Marks: {avg:.2f}")
    print(f"Median Marks: {median}")
    print(f"Highest Score: {max_name} ({max_score})")
    print(f"Lowest Score: {min_name} ({min_score})")

#Task4:

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def count_grades(grades_dict):
    summary = {}
    for grade in grades_dict.values():
        summary[grade] = summary.get(grade, 0) + 1
    return summary

def show_grade_summary(grades):
    summary = count_grades(grades)
    print("\nGrade Distribution")
    for grade, count in summary.items():
        print(f"{grade}: {count} student(s)")

#Task5:

def pass_fail_lists(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students

def show_pass_fail_summary(marks):
    passed, failed = pass_fail_lists(marks)
    print("\n Pass/Fail Summary ")
    print(f"Passed Students ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed Students ({len(failed)}): {', '.join(failed) if failed else 'None'}")

#Task6:

def display_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks_dict:
        print(f"{name:<12}\t{marks_dict[name]:<5}\t{grades_dict[name]}")
    print("-" * 30)

def main():
    welcome_message()

    while True:
        choice = input("\nEnter your choice (Analyze or Exit): ")

        if choice == 'Exit':
            print("Thank you for using Gradebook Analyzer. Goodbye!")
            break

        elif choice == 'Analyze':
        
            marks = get_student_data()

            show_statistics(marks)

            grades = assign_grades(marks)
            show_grade_summary(grades)

            show_pass_fail_summary(marks)

            display_table(marks, grades)

            rerun = input("\nDo you want to analyze another class? (Yes/No): ").lower()
            if rerun != 'Yes':
                print("Exiting Gradebook Analyzer. Have a great day!")
                break
        else:
            print("Invalid choice. Please enter Analyze or Exit.")

if __name__ == "__main__":
    main()

        