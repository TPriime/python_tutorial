while True:
    year_of_birth = input("Enter your year of birth (enter 'q' to quit): ")

    if year_of_birth == 'q':
        exit(0)

    age = 2024 - int(year_of_birth)

    print(f"Your age is {age}\n")
