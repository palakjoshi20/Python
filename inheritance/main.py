class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showname(self):
        print("name is ",self.name)
    def showage(self):
        print("age is ",self.age)
class student(person):
    def __init__(self,r,c):
        #person.__init__(self,"Bobby",33)
        super().__init__("Bobby", 33)

        self.rollno=r
        self.course=c
    def showrn(self):
        print("roll no is ",self.rollno)
    def showc(self):
        print("course is ",self.course)
s1=student(100,"bsc")
s1.showrn()
s1.showc()
s1.showname()
s1.showage()
s2=student(45,"btech")
s2.showrn()
s2.showc()
s2.showname()
s2.showage()


