from rent.py import CarRent, BikeRent, Customer
bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

mainMenu = True
while True:
    if mainMenu:
        print("""
              ***** Vehicle Rental Shop *****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        mainMenu = False

        choice = input("Enter choice: ")

        if choice == "A" or choice == "a":
            print("""
                  ***** BIKE MENU *****
                  1.Display available bikes
                  2.Request a bike on hourly basics $ 5
                  3.Request a bike on daily basics $ 84
                  4.Return a bike
                  5.Main Menu
                  6.Exit
                  """)
            choice = input("Enter choice")

            try:
                choice: int(choice)
            except ValueError:
                print("It is not integer")
                continue

            if choice == 1:
                bike.displayStock()
                choice = "A"
            elif choice == 2:
                customer.rentalTimeB = bike.rentHourly(
                    customer.requestVehicle("bike"))
                customer.rentalBasisB = 1
                mainMenu = True
                print("----------------------")
            elif choice == 3:
                customer.rentalTimeB = bike.rentDaily(
                    customer.requestVehicle("bike"))
                customer.rentalBasisB = 2
                mainMenu = True
                print("----------------------")
            elif choice == 4:
                customer.bill = bike.returnVehicle(
                    customer.returnVehicle("bike"), "bike")
                customer.rentalBasisB, customer.rentalTimeB, customer.bikes = 0, 0, 0
                mainMenu = True
            elif choice == 5:
                mainMenu = True
            elif choice == 6:
                break
            else:
                print("Invalid Input please enter a number 1-6")
                mainMenu = True
        elif choice == "B" or choice == "b":
            print("""
                  ***** CAR MENU *****
                  1.Display available cars
                  2.Request a car on hourly basics $ 10
                  3.Request a car on daily basics $ 192
                  4.Return a car
                  5.Main Menu
                  6.Exit
                  """)
            choice = input("Enter choice")

            try:
                choice: int(choice)
            except ValueError:
                print("It is not integer")
                continue

            if choice == 1:
                car.displayStock()
                choice = "B"
            elif choice == 2:
                customer.rentalTimeC = car.rentHourly(
                    customer.requestVehicle("car"))
                customer.rentalBasisC = 1
                mainMenu = True
                print("----------------------")
            elif choice == 3:
                customer.rentalTimeC = car.rentDaily(
                    customer.requestVehicle("car"))
                customer.rentalBasisC = 2
                mainMenu = True
                print("----------------------")
            elif choice == 4:
                customer.bill = car.returnVehicle(
                    customer.returnVehicle("car"), "car")
                customer.rentalBasisC, customer.rentalTimeC, customer.cars = 0, 0, 0
                mainMenu = True
            elif choice == 5:
                mainMenu = True
            elif choice == 6:
                break
            else:
                print("Invalid Input please enter a number 1-6")
                mainMenu = True
        if choice == "Q" or choice == "q":
            break
        else:
            print("Invalid input Please Enter A-B-Q")
            mainMenu = True
        print("Thank you for using the cehicle rental shop")
                
        