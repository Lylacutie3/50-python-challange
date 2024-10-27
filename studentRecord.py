#student record using python
import os #for clear screen

class StudentInfo():

    #CONSTRUCTOR      
    def __init__(self, name, q1, q2, q3): 
        self.name = name
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def average(self):
        return round((self.q1 + self.q2 + self.q3)/3, 2)
    
    def grade(self):
        if self.average() >= 90:
            return 'A'
        elif self.average() >= 85:
            return 'B'
        elif self.average() >= 80:
            return 'C'
        elif self.average() >= 75:
            return 'D'
        else:
            return 'E'
    

    def display(self):
        print(f"Student name: {self.name}")
        print(f"Quiz 1 score: {self.q1}")
        print(f"Quiz 2 score: {self.q2}")
        print(f"Quiz 3 score: {self.q3}")
        print(f"Average: {self.average()}")
        print(f"Grade: {self.grade()}")
    
    def updateScore(self):
        pick = int(input("What Quiz you want to update?\n1. Quiz 1\n2. Quiz 2.\n3. Quiz 3\n"))
        score = int(input("Input Updated Score: "))
        if pick == 1:
            self.q1 = score
            print("Successfully Updated")
        elif pick == 2:
            self.q2 = score
            print("Successfully Updated")
        elif pick == 3:
            self.q3 = score
            print("Successfully Updated")
        else:
            print("Invalid choice")
    
    def updateName(self, name):
        self.name = name
        print("Successfully Updated")



#for section
class ClassRecord():

    def __init__(self, size):
        self.last = 0
        self.size = size
        self.student = []   

    def ifempty(self):
        return self.last == 0

    def iffull(self):
        return self.last == self.size

    def add(self):
        if self.iffull():
            print("Class is full")
        else:
            name = input("Enter Student Name: ")
            q1 = int(input("Enter Quiz 1 Score: "))
            q2 = int(input("Enter Quiz 2 Score: "))
            q3 = int(input("Enter Quiz 3 Score: "))
            self.student.append(StudentInfo(name, q1, q2, q3))
            self.last += 1

    def display(self):
        if self.ifempty():
            print("No Student in the class")
        else:
            for i in range(len(self.student)):
                self.student[i].display()

    def update(self):
        name = input("Enter Student Name: ")
        for i in range(self.last): 
            if self.student[i].name == name:
                print("What do you want to update? ")
                print("1. Name")
                c = int(input(("2. Quizes")))

                if c == 1:
                    self.student[i].updateName(input("Enter New Name: "))
                elif c == 2:
                    self.student[i].updateScore()
                else:
                    print("Invalid choice")
                return
        
        print("Name not found")
        return


student = ClassRecord(30);

pick = 0
while pick != 4:
    os.system("clear")
    print("MENU: ") 
    print("1. Add Student")
    print("2. Display Student")
    print("3. Update Student")
    print("4. Exit")
    pick = int(input("Enter your choice: "))
    if pick == 1:
        os.system("clear");student.add();input("Press Enter to continue...") 
    elif pick == 2:
        os.system("clear");student.display();input("Press Enter to continue...")  
    elif pick == 3:
        os.system("clear");student.update();input("Press Enter to continue...") 
    else:
        os.system("clear");print("invalid input");input("Press Enter to continue...")