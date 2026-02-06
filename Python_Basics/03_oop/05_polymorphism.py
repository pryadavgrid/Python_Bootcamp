# Q5. Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar class but diffrent behavior

# Best Example of polimorphism is "+", 
# When we add two string "hello" + "python" then return "Hello Python"
# When we add two number 10 + 20 then return 30

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

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


my_Electric_Car = ElectricCar('Tesla',"Model S", "85kWh")
print(my_Electric_Car.fuel_type()) 


my_car = Car('Tata', 'Safari')
print(my_car.fuel_type())
