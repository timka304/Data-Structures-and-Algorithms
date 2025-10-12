class Car():
    # characteristics/ features / attributes
# CONSTRUCTOR
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
    
    # functions / methods / behavior/actions
    def start(self):
        print(f"{self.model} is starting")
    
    def stop(self):
        print(f"{self.model} is stopping")



#instances/objects

ford = Car("Mustang", "Red", 2020, 30000)

bmw = Car("M5", "Gray", 2024, 70000)

ford.start()
print(ford.color)

print("color is ", bmw.color)
