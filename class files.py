class student:
    def __init__(self):
        self.name=input("Enter your Name :")
        self.roll=int(input("Enter your roll:"))
        self.sub1=int(input("Enter your sub1 mark:"))
        self.sub2=int(input("Enter your sub2 mark:"))
        self.sub3=int(input("Enter your sub3 mark:"))
    def calc(self):
        self.total_mark=self.sub1+self.sub2+self.sub3
        self.average=self.total_mark/3
        
    def disp(self):
        print("Student Name is",self.name)
        print(self.name,"roll no is ",self.roll)
        print(self.name,"total mark is ",self.total_mark)
        print(self.name,"average mark is ",self.average)
        print("")

s1=student()
s2=student()

s1.calc()
s1.disp()

s2.calc()
s2.disp()



        
        