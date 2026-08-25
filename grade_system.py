


def get_grade(mark):
    try:
        numeric_mark = float(mark)
    except (TypeError, ValueError):
        raise ValueError("Mark must be a number.")

    if not 0 <= numeric_mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if numeric_mark >= 90:
        return "A"
    elif numeric_mark >= 80:
        return "B"
    elif numeric_mark >= 70:
        return "C"
    elif numeric_mark >= 60:
        return "D"
    return "E"


while True:
    try:
        mark = float(input("Enter Your Mark: "))
        grade = get_grade(mark)
        print(f"Mark {mark}")
        print(f"Grade {grade}")
        break
    except ValueError:
        print("Please enter a valid mark between 0 and 100.")