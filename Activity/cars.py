
cars = ["BMW", "Mercedes", "Audi", "Toyota", "Honda"]

for car in cars:
    if car == "BMW":
        print (car.upper())
else:
    print (car.title())

is_car_bmw = car == "BMW"
print (is_car_bmw)

# Why does it continue to print out false?
# The reason is that the variable 'car' retains the last value from the loop,
# which is "Honda". Therefore, when we check if 'car' is equal to "BMW", 
# it evaluates to False. To fix this, we should check for "BMW" within the loop or reset the variable 'car' after the loop.
