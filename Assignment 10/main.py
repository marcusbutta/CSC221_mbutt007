import functions

print("Test of car_dict:")
car = functions.car_dict('Honda', 'Civic', Color = 'Blue')
for key, value in car.items():
    print(f"{key.title()}: {value.title()}")
print("\nSecond test of car_dict:")
car = functions.car_dict('Ford', 'F150', Color = 'Red', Trailer = 'Yes')
for key, value in car.items():
    print(f"{key.title()}: {value.title()}")

print("\nTest of num_sum:")
sum, num_list = functions.num_sum(4, 5)
print(f"Numbers: {num_list}\nSum: {sum}")
print("\nSecond test of num_sum:")
sum, num_list = functions.num_sum(6)
print(f"Numbers: {num_list}\nSum: {sum}")