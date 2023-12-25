class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee: ", result)


class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("CompEng: ", result)


class EEE(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("EEE: ", result)

e1 = Employee()

ce = CompEng()

eee = EEE()

e1.raisee()
ce.raisee()
eee.raisee()


employeeList = [ce, eee]

for employee in employeeList:
    employee.raisee()