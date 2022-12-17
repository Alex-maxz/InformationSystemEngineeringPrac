class car:


    def __init__(self, type, road, cost):
        self.wheels = 0
        self.chassis = 0
        self.engine = 0
        self.interior = 0
        self.builder = carbuilder

        if cost < 100 and road < 1:
            self.builder.basiccar(self)
        if cost > 100:
            self.builder.bettercar(self)

        self.calcspeed()
        self.calceconomy()


        

    def calcspeed(self):
        self.speed = sum(self.engine) / (sum(self.chassis) + sum(self.interior))
    def calceconomy(self):

        self.eco = self.speed * (sum(self.chassis) + sum(self.interior)) * self.chassis[1]**2
    
    def __str__(self):
        return str(self.speed) + " " + str(self.eco)

    




class carbuilder:

    def basiccar(car):
        car.engine = [2, 0]
        car.chassis = [1, 0.5]
        car.interior = [5, 0, 1]
        car.wheels = [15, 16, 1]

    def bettercar(car):
        car.engine = [3, 1]
        car.chassis = [2, 0.25]
        car.interior = [7, 2, 3]
        car.wheels = [21, 21, 1]


mycar = car(1, 0.5, 120)

print(mycar)