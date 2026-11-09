def validate_name(name):
    return bool(name.strip())


def validate_age(age):
    try:
        age = int(age)
        return 6 <= age <= 100
    except ValueError:
        return False


def validate_grade(grade):
    try:
        grade = int(grade)
        return 0 <= grade <= 100
    except ValueError:
        return False
