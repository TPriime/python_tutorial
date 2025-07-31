# def add(x, y):
#     ans = x + y
#     return ans

# answer = add(2, 3)
# print(f"answer = {answer}")  

# A function that takes a score and returns a grade

def grade(score):
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:        
        return "C"
    return "F"

print(grade(40))