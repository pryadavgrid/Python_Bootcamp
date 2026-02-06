# Modify the Car Class to encapsulate the brand attribute/variable, making it private, and provide getter methor for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    

class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size


my_Electric_Car = ElectricCar('Tesla',"Model S", "85kWh")
# print(my_Electric_Car.brand) 

# we can't access this variable beacuse this "brand" is private attribute of class "__brand" it mean "__brand" access only own class

# if we want user can access this we crate the getter method of private attribute 
# eg. def get_brand(self): return self.__brand

# For the acees we call get_brand()

print(my_Electric_Car.get_brand())

# print(my_Electric_Car.model)
# print(my_Electric_Car.battry_size)
# print(my_Electric_Car.full_name())