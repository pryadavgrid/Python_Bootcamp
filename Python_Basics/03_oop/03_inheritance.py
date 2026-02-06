# Create an ElectricCar class that inherit from the Car Class and has an additional attribute/variable "battry_size"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size


my_Electric_Car = ElectricCar('Tesla',"Model S", "85kWh")
print(my_Electric_Car.brand)
print(my_Electric_Car.model)
print(my_Electric_Car.battry_size)
print(my_Electric_Car.full_name())