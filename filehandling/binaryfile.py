import pickle
# def write():
#     f=open("sanchit.dat","wb")
#     list=["physics","chem","english"]
#     pickle.dump(list,f)
#     f.close()
# def read():
#     f=open("sanchit.dat","rb")
#     lst=pickle.load(f)
#     print(lst)
#     f.close()
# write()
# read()


# student={}
# studentfile=open("student.dat","wb")
# ans='y'
# while ans=='y':
#     print("student record")
#     name = input("enter the name: ")
#     rollno = int(input("enter the rollnumber: "))
#     marks = float(input("enter the marks: "))
#     student['name']=name
#     student['rollno']=rollno
#     student['marks']=marks
#     pickle.dump(student,studentfile)
#     ans=input("y/n")
# studentfile.close()

f=open('student.dat','rb')
try:
    while True:
        student=pickle.load(f)
        print(student)
except EOFError:
    f.close()

