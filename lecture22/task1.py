import multiprocessing
import time


def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == '__main__':

    numbers = [45000, 57000, 65000, 78000]

    start = time.time()

    for number in numbers:
        factorial(number)

    end = time.time()

    print(f"Single-process time: {end - start}")

    start = time.time()

    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=factorial, args=(number,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end = time.time()

    print(f"Multiprocessing time: {end - start}")

