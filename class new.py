class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def calc(self):
        self.total_mark=self.sub1+self.sub2+self.sub3
        self.average=self.total_mark/3
        
    def disp(self):
        print("Student Name is",self.name)
        print(self.name,"roll no is ",self.roll)
        print(self.name,"total mark is ",self.total_mark)
        print(self.name,"average mark is ",self.average)
        print("")

students = []
for i in range(2):
    print("Enter details for Student",i+1)
    name = input("Enter Name: ")
    roll = int(input("Enter Roll No: "))
    marks=[]
    for j in range(3):
        marks=int(input("Enter the marks"))
        marks.append(marks)
    student=students(name,marks)
    students.append(student)

print("student report:")
for student in students:
    student.display()


        
