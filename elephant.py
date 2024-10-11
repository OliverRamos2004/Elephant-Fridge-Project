import time

class elephant:

    def __init__(self, weight , height , age):
        self.weight = weight
        self.height = height
        self.age = age

    def __str__(self):
        return "This is an elephant. It is {} years old, {} feet tall, and weights {} pounds!".format(self.age , self.height , self.weight)

    def __del__(self):
        print("The elephant has been deleted :( ....")

    def eat(self, n):
        for i in range(n):
            print("\rThe elephant is eating food... {}%".format(100*(i+1) / n), end = " ")
            time.sleep(1)

        print("Finished!")

    def walk(self, distance, direction):
        for i in range(distance):
            print("\rThe elephant is talking towars {} : {} feets".format(direction, i+1), end = " ")
            time.sleep(1)

        print("finished!")

    def sleep(self, n):
        for i in range(n):
            print("\rThe elephant is sleeping! he will wake up in {} hours.".format(i+1), end = " ")
            time.sleep(1)

        print("He's awaken...")