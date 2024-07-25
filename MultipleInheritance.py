class Personal:
    def __init__(self,name,age,vill,pin):
        self.name = name
        self.age = age
        self.vill = vill
        self.pin = pin

    def showPersonal(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Village: ",self.vill)
        print("Pin: ",self.pin)

class Education:
    def __init__(self,rollno,course,college):
        self.rollno = rollno
        self.course = course
        self.college = college

    def showEducation(self):
        print("Enrollment No: ",self.rollno)
        print("Course: ",self.course)
        print("College: ",self.college)

class Marks:
    def __init__(self,sub1,sub2,sub3,sub4,sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        
    def showMarks(self):
        print("Maths: ",self.sub1)
        print("Python: ",self.sub2)
        print("DSA: ",self.sub3)
        print("DBMS: ",self.sub4)
        print("DECO: ",self.sub5)

class Student(Personal, Education, Marks):
    def __init__(self, name, age, vill, pin, rollno, course, college, sub1, sub2, sub3, sub4, sub5):
        Personal.__init__(self, name, age, vill, pin)
        Education.__init__(self, rollno, course, college)
        Marks.__init__(self, sub1, sub2, sub3, sub4, sub5)

    def Details(self):
        self.showPersonal()
        self.showEducation()
        self.showMarks()
        self.Percentage()

    def Percentage(self):
        total_Marks = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5
        percentage = (total_Marks / 5)
        print("Percentage: ", percentage)

student = Student("Asim Husain", 19, "Shahpur Sirpura", 244304, "TCA2259012", "B.Tech CS-AI [A]", "TMU Moradabad", 89, 88, 78, 99, 79)
student.Details()