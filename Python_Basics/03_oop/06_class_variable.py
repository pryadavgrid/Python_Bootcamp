# Q6. Add a class variable to Car that keep track of number of car created.

class Car:
    no_of_car_created = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

        Car.no_of_car_created = Car.no_of_car_created + 1


    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol and Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size

    def fuel_type(self):
        return "Electric Charge"


# my_Electric_Car = ElectricCar('Tesla',"Model S", "85kWh")
# print(my_Electric_Car.fuel_type()) 


my_car = Car('Tata', 'Safari')
my_car_2 = Car('Tata', 'Nexon')
my_car_3 = Car('Tata', 'Tata')

print(Car.no_of_car_created)
# print(my_car.fuel_type())

# Note : in this case when we create a object using ElectricCar Class then it increase the " no_of_car_created " because inside the ElectricCar Class we cal super.__init__() Method S