class Fridge:

    def __new__(cls, brand, dimensions, capacity):
        try:
            assert len(dimensions) == 3, "incorrect dimensions"
        except AssertionError as e:
            print(e)
            return
        else:
            instance = super().__new__(cls)
            return(instance)

    def __init__(self, brand, dimensions, capacity):
        self.brand = brand
        self.dimensions = dimensions
        self.status = False
        self.foods = []
        self.capacity = capacity

    def __str__(self):
        return "This is a fridge. The brand is {} and its dimensions are {}".format(self.brand, self.dimensions)

    def __del__(self):
        print("The fridge has been deleted :(")

    def open(self):
        self.status = True
        print("The fridge is open now!")

    def close(self):
        self.status = False
        print("The fridge is closed now!")

    def put_in(self,food):
        try:
            assert self.status, "Open the fridge first"
        except AssertionError as e:
            print(e)
            return
        else:
            self.foods.append(food)
            print("Put {} in the fridge".format(food))
            self.status = False #OR self.close()

    def take_out(self,food):
        try:
            assert self.status, "Open the fridge first!"
            assert food in self.foods, "No {} in the fridge".format(food)
        except AssertionError as e:
            print(e)
            return
        else:
            self.foods.remove(food)
            print("Taking {} out...".format(food))
            self.close() #OR self.status = False
            
    def can_fit(self, item_size):
        if item_size > self.capacity:
            print("The item is too big to fit in the fridge!")
            return False
        return True

if __name__ == "__main__":
    f0 = Fridge('Samsung', [10,20,30], 10000)
f1 = Fridge('Samsung', [10,20,30], 10000)

