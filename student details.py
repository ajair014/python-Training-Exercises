def students():
        name=input("Enter your Name :")
        age=int(input("Enter your age :"))
        sub1=int(input("Enter math mark :"))
        sub2=int(input("Enter physics mark :"))
        sub3=int(input("Enter your chemistry mark :"))

        print("Name :",name)
        print("AGE :",age)
        tot=sub1+sub2+sub3
        print("Total :",tot)
        aver=tot//3
        print("Average :",aver)
        if(aver>85 and aver<100):
            print("class : first class")
        elif(aver>65 and aver<84):
            print("Class : Second class")
        elif(aver>50 and aver<64):
            print("Class : Third Class")
        elif(aver<50):
            print("Fail !!")
        else:
            print("Enter valid mark")
stud=1
student=students()
for i in range(1,10):
    print("Student",stud)
    student()
    stud+=1
    

