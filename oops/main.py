# class student:
#     rollno=1
#     name="rahul"
# s1=student()#object s1
# print(s1.name)
# print(s1.rollno)
#


# #constructor
# class student:
#     def __init__(self,n,r,s):#(local variables)
#         self.name=n#(name is instance variable here)
#         self.rollno=r
#         self.school=s
# s1=student("palak",22,"Beersheba")#object s1 will pass in place of self
# s1.name="Bobby"
# print(s1.name,s1.rollno,s1.school)


# class student():
#     def details(self,n,r,s):
#         self.name=n
#         self.rollno=r
#         self.school=s
# s1=student()
# s1.details("Bobby",0,"Beersheba")
# print(s1.name,s1.rollno,s1.school)



class student():
    def details(self):
        print("hello world")
s1=student()
s1.details()
