class Fruits:
    def __init__(self, name, color, taste, shape, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.shape = shape
        self.price = price
    #getter methods
    def get_shape(self):
        print(self.shape)

    def get_price(self):
        print(self.price)
    
    def show_fruit(self):
        print("I am a fruit with following characteristics {} {} {} {} {}".format(self.name, self.color, self.taste, self.shape, self.price))

    #setter methods
    def set_price(self, new_price):
        self.price = new_price

apple = Fruits("Apple", "Red", "Sweet", "Round", 100)
banana = Fruits("Banana", "Yellow", "Sweet", "Long", 50)

banana.show_fruit()
banana.get_price()
apple.set_price(100)
apple.show_fruit()

apple.get_shape()