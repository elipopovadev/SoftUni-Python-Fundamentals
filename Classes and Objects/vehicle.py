class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
        
    def buy(self, money, owner):
        if self.owner is None and self.price <= money:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}" 
        elif self.owner is None and self.price > money:
            return "Sorry, not enough money"
        else:
            return "Car already sold"
    
    def sell(self):
        if self.owner:
            self.owner = None
        else:
          return "Vehicle has no owner"
        
    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}" 
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
        
 
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
       
        
        
        
        
        
        
        
        
        
        
        
        
        
