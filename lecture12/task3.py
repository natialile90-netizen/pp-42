from functools import wraps


def require_role(allowed_role="admin"):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)

            print("Permission Denied: User is not an admin.")

        return wrapper

    return decorator


@require_role(allowed_role="admin")
def dashboard(user_role):
    print("Welcome to the admin dashboard!")

role=input("Enter your role: ")


dashboard(user_role=role)