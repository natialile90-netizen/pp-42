import time
from functools import wraps


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Running {func.__name__}... Executed in {end - start:.2f} seconds.")

        return result

    return wrapper


@log_execution
def calculate_sum(a, b):
    """Adds two numbers."""
    time.sleep(2)
    return a + b


print(calculate_sum(25, 55))
print(calculate_sum.__name__)
print(calculate_sum.__doc__)