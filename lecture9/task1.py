def create_user_profile(first_name, last_name, role="Student", is_active=True):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }


print(create_user_profile("Ana", "Beridze"))

print(create_user_profile(
    "Natia",
    "Maisuradze",
    role="Teacher",
    is_active=False
))