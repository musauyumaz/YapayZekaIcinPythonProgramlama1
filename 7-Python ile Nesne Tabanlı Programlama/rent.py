import datetime


class VehicleRent:
    def __init__(self, stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        print("Vehicle avaliable to rent: ", self.stock)
        return self.stock

    def rentHourly(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry {self.stock} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"Rented a {n} vehicle for hourly at {self.now.hour} hours")

            self.stock -= n
            return self.now

    def rentDaily(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry {self.stock} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"Rented a {n} vehicle for daily at {self.now.hour} hours")

            self.stock -= n
            return self.now

    def returnVehicle(self, request, brand):
        carHPrice = 10
        carDPrice = carHPrice * 8 / 10 * 24
        bikeHPrice = 5
        bikeDPrice = bikeHPrice * 7 / 10 * 24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*carHPrice*numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/3600*24*carDPrice*numOfVehicle

                if 2 <= numOfVehicle:
                    print("You have extra 20% discount")
                    bill = bill * 0.8

                print("Thank you for returning your car")
                print(f"Price: ${bill}")
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bikeHPrice*numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/3600*24*bikeDPrice*numOfVehicle

                if 4 <= numOfVehicle:
                    print("You have extra 20% discount")
                    bill = bill * 0.8

                print("Thank you for returning your bike")
                print(f"Price: ${bill}")
                return bill
        else:
            print("You do not rent a vehicle")


class CarRent(VehicleRent):

    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)

    def displayStock(self, bill):
        bill = bill - (bill*discount_rate)/100


class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasisB = 0
        self.rentalTimeB = 0

        self.cars = 0
        self.rentalBasisC = 0
        self.rentalTimeC = 0

    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be number")

            if bikes < 1:
                print("number of bikes should be greated than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            if brand == "car":
                cars = input("How many cars would you like to rent?")
                try:
                    cars = int(cars)
                except ValueError:
                    print("Number should be number")

                if cars < 1:
                    print("number of cars should be greated than zero")
                    return -1
                else:
                    self.cars = cars
                return self.cars
        else:
            print("Request vehicle error")

    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTimeB and self.rentalBasisB and self.bikes:
                return self.rentalTimeB and self.rentalBasisB and self.bikes
            else:
                return 0, 0, 0
        elif brand == "car":
            if self.rentalTimeC and self.rentalBasisC and self.cars:
                return self.rentalTimeC and self.rentalBasisC and self.cars
            else:
                return 0, 0, 0
        else:
            print("Return vehicle error")



