'''
Create a program that collects the user's name, department, and scores for 5 courses. The program should output/display the user's information with the grades of their courses.

sample output:

Name      : Gift
Department: Relations

Course Grades...
English : B
History : A
Grooming: B
Python  : C
'''

def grade(score):
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:        
        return "C"
    return "F"

# user input
name = input("Enter your name: ")
department = input("Enter your department: ")
print("\nEnter the scores for the following courses...\n")
score_ice_cream = int(input("Ice cream: "))
score_english = int(input("English: "))
score_history = int(input("History: "))

# calculated
grade_english = grade(score_english)
grade_history = grade(score_history)
grade_ice_cream = grade(score_ice_cream)

# outputs
print()
print(f"Name      : {name}")
print(f"Department: {department}\n")
print("Course Grades...")
print(f"English : {grade_english}")
print(f"History : {grade_history}")
print(f"Ice cream : {grade_ice_cream}")