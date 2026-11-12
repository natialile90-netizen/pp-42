def validate_name(name):
    if name.strip():
        return True
    return False


def validate_age(age):
    try:
        age = int(age)
        if 16 <= age <= 70:
            return True
        return False
    except ValueError:
        return False


def validate_roll_number(roll_number):
    if roll_number.strip():
        return True
    return False


def validate_grade(grade):
    try:
        grade = int(grade)
        if 0 <= grade <= 100:
            return True
        return False
    except ValueError:
        return False
