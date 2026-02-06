# Basic Class And Object
# Q1. Create a Car class with attributes like brand and model. Then create an instance of class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_class_obj_1 = Car('Toyota', 'Corola')
print(my_class_obj_1.brand)
print(my_class_obj_1.model)

my_class_obj_2 = Car('Tata', 'Safari')
print(my_class_obj_2.brand)
print(my_class_obj_2.model)


