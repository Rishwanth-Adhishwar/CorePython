class Student:
    def getStudentInfo(self):
        self.__rollNo = input("Enter Roll No: ")
        self.__name = input("Enter Name: ")

    def printStudentInfo(self):
        print("Roll No:", self.__rollNo)
        print("Name:", self.__name)


class Marks(Student):
    def getMarks(self):
        self.getStudentInfo()

        self.__mark1 = float(input("Enter mark of Subject 1: "))
        self.__mark2 = float(input("Enter mark of Subject 2: "))
        self.__mark3 = float(input("Enter mark of Subject 3: "))

    def getStudentMarkInfo(self):
        self.printStudentInfo()

        print("Subject 1 Mark:", self.__mark1)
        print("Subject 2 Mark:", self.__mark2)
        print("Subject 3 Mark:", self.__mark3)

    def cal_total(self):
        return self.__mark1 + self.__mark2 + self.__mark3


class Result(Marks):
    def getResult(self):
        self.getMarks()
        self.__total = self.cal_total()

    def putResults(self):
        self.getStudentMarkInfo()
        print("Total Marks out of 300:", self.__total)


obj = Result()

obj.getResult()
obj.putResults()