from random import randint
from abc import ABC

class Company():

    @staticmethod
    def __nameValidator(name):
        if(isinstance(name, str) and len(name) != 0):
            return True
        raise Exception("Wrong name")
    
    @staticmethod
    def __salaryValidator(salary):
        if((isinstance(salary, int) or isinstance(salary, float)) and salary >0):
            return True
        raise Exception("Wrong salary")
    

    def __init__(self, companyName):
        self.__companyName = companyName
        self.__WorkersList = {}
        self.__income = randint(10_000, 100_000_000)

    
    def hire(self, name:str, post:str, salary:float):
        if(self.__nameValidator(name) and self.__salaryValidator(salary)):
            self.__WorkersList[name]=[post, salary]

    def getWorkers(self):
        print(self.__WorkersList)

    def hireAll(self, listW):
        if(isinstance(listW, list)):
            for w in listW:
                self.hire(w[0], w[1], w[2])
        else:
            raise Exception("Wrong list")

    def fire(self, name):
        if(name in self.__WorkersList.keys()):
            self.__WorkersList.pop(name)

    def getIncome(self):
        return self.__income
    
    
#workers
class Worker(ABC):
    @staticmethod
    def _companyIncomeValidator(companyIncome):
        if((isinstance(companyIncome, float) or isinstance(companyIncome, int)) and companyIncome>0):
            return True
        raise Exception("Wrong company income")

    def getMonthSalary(self):
        pass

class Manager(Worker):
    def __init__(self):
        self.__fixedPart = 100_000
    
    def getMonthSalary(self, companyIncome):
        if(Worker._companyIncomeValidator(companyIncome)):
            return self.__fixedPart + companyIncome*.05
    
class TopManager(Worker):
    def __init__(self):
        self.__fixedPart = 150_000
    
    def getMonthSalary(self, companyIncome):
        if(Worker._companyIncomeValidator(companyIncome)):
            if(companyIncome > 10_000_000):
                return self.__fixedPart*2.5
            return self.__fixedPart
    
class Operator(Worker):
    def __init__(self):
        self.__fixedPart = 50_000

    def getMonthSalary(self):
        return self.__fixedPart
        



c = Company("ООО \"ЗЕЛЕНОГЛАЗОЕ ТАКСИ\"")
c.hireAll([["vova", "dvornik", 150],["sanya", "hr", 200], ["petya", "lox", 10]])
# print(c.getTopSalaryStaff(3))
c.getWorkers()
# c.fire("vova")
# c.getWorkers()


v = Operator()
print(v.getMonthSalary())