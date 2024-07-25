class Student:
    def set_details(self, name, rollno,age, grade):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.grade = grade

    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Age: ",self.age)
        print("Grade:", self.grade)
student = Student()
student.set_details("Asim Husain",19, 12, "A+")
student.display_details()