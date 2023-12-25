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
                bike.returnVehicle(customer.returnVehicle("bike"), "bike")
                customer.rentalBasisB, customer.rentalTimeB, customer.bikes = 0, 0, 0
                mainMenu = True
            elif choice == 5:
                mainMenu = True
            elif choice == 6:
                break
            else:
                print("Invalid Input please enter a number 1-6")


