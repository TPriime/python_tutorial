'''
variable declaration

1. must only consist of letters a-z, A-Z, or "_" or 0-9
2. must not start with a number (0-9)
3. no space in between
'''

# bad variable declaration
# depart ment = "History"
# 4history = "Nigeria"
# depart.ment = "Bad"

# examples of good variables
department = "History"
_department = "English"
department6 = "Agriculture"
depart_ment = "Mathematics"
depa4383h4ubfubayuvcdsvc4ewfw4 = "French"

## Variables cannot be referenced differently

department = "English"
# print(Department)  # wrong

score_English = 6
# print(score_english)  # wrong  
print(score_English)