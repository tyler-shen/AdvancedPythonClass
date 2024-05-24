class ParkingSystem:
    def __init__(self, big, medium, small):
        self.spots = [big, medium, small]

    def addCar(self, carType):
        if self.spots[carType - 1] > 0:
            self.spots[carType - 1] -= 1
            return True
        else:
            return False

ps = ParkingSystem(1, 1, 0)
print(ps.addCar(1))
print(ps.addCar(2))
print(ps.addCar(3))
print(ps.addCar(1))
