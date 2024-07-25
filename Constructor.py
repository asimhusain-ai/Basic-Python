class Student:
    def __init__(self,name,rollno,age,grade):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.grade = grade
    
    def displaydetails(self):
        print("Name: ",self.name)
        print("RollNo: ",self.rollno)
        print("Age: ",self.age)
        print("Grade: ",self.grade)
student = Student("Asim Husain",12,19,"A+")
student.displaydetails()