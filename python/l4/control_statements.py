# Control statements
# 1. if
# 2. if-else
# 3. chained if
# 3.1 nested if
# 4. for
# 5. while

# 2. if-else
x = 500

if x > 100:
    print("X is in it's 100s")
else:
    print("X is not greater than 100")


# 3. Chained if

x = int(input("Enter your grade: "))

if x >= 70:
    print("A")
elif x >= 60:
    print("B")
elif x >= 50:
    print("C")
elif x >= 40:
    print("D")
else:
    print("F")


# 3.1 nested if

x = 100
y = 50

if x == 100:
    if y == 50:
        print("Hello")


# 4. for

# i in [0,1,2,3,4,5,6,7,8,9]
for i in range(10): 
    print(f"Hello number {i}")


# 5. while

i = 0
while True:
    print(i)     # 3

    if i == 3:   # 3 == 3 : True
        break
    
    i = i + 1    # i = 2 + 1, i is 3

print ("Hello")



x = 45

if x >= 70:
    print("A")
elif x >= 60:
    print("B")
    
if x >= 40:
    print("D")
else:
    print("F") # F   (- 4)

i = 0
while True:
    if i == 2:
        print("Hmmm") # Hmmm
        break
    i = i + 1

if i == x:
    print(x)

t = input("Enter your name: ") # Prime

if t == "Gift":
    print("Hello Gift")
else:
    print("Good bye") # Good bye

6/10

# We rise by decieving others!