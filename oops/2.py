# x=10
# class student:
#     def set(self):
#         global x
#         x=20
#         print("inside value of x",x)
# s1=student()
# s1.set()
# print("Outside function value of x is",x)


class student:
    a=10#1st method
    def __init__(self):
        self.x=20#instance variable
        student.b=20#2nd method
    @staticmethod
    def f1():
        student.c=30 #3rd method
    def f2(self,a):#instance member function //instance method
        student.d = a #4th method
        self.a = a #instance method
    @classmethod
    def f3(cls):  #class method
        cls.e= 77 # 5th method
        student.f = 60 # 6th method
        print('CLass Method')
student.g=70#static var 7th method
s1=student()
s1.f1()
student.f1()
print(student.__dict__)















