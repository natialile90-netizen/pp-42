class Car:
    wheels_count= 4
    steering_wheel = 1

car_1 =Car()
print(type(car_1))
print(id(car_1))
print(car_1.wheels_count)
print(car_1.steering_wheel)

print("=" * 40)

car_2 = Car()
print(type(car_2))
print(id(car_2))
print(car_2.wheels_count)
print(car_2.steering_wheel)

num = 10
print (type(num))