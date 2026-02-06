# Q2. Add a method to the Car class that display the full name of the car (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_class_obj_1 = Car('Toyota', 'Corola')
# print(my_class_obj_1.brand)
# print(my_class_obj_1.model)
print(my_class_obj_1.full_name())

my_class_obj_2 = Car('Tata', 'Safari')
# print(my_class_obj_2.brand)
# print(my_class_obj_2.model)