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

# user input
name = input("Enter your name: ")
department = input("Enter your department: ")
print("\nEnter the scores for the following courses...\n")
score_english = int(input("English: "))
score_history = int(input("History: "))

# calculated
grade_english = ""
grade_history = ""

# calculate grade for english
if score_english >= 70:
    grade_english = "A"
if score_english >= 60 and score_english <= 69:
    grade_english = "B"
if score_english >= 50 and score_english <= 59:
    grade_english = "C"
else:
    grade_english = "F"

# calculate grade for history
if score_history >= 70:
    grade_history = "A"

if score_history >= 60 and score_history <= 69:
    grade_history = "B"

if score_history >= 50 and score_history <= 59:
    grade_history = "C"
else:
    grade_history = "F"

# outputs
print()
print(f"Name      : {name}")
print(f"Department: {department}\n")
print("Course Grades...")
print(f"English : {grade_english}")
print(f"History : {grade_history}")


'''
variable declaration

1. must only consist of letters a-z, A-Z, or "_" or 0-9
2. must not start with a number (0-9)
3. no space in between
'''