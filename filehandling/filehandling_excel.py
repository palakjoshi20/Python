#for excel file
# import csv
# fh=open("palak.csv","w")
# stu=csv.writer(fh)#writer function to write in this file,,stu variable h
# stu.writerow(["Name","rollno","marks"])
# for i in range(5):
#     print("student record")
#     name=input("enter the name: ")
#     rollno=int(input("enter the rollnumber: "))
#     marks=float(input("enter the marks: "))
#     sturec=[name,rollno,marks]#student record
#     stu.writerow(sturec)#function to write a row
# fh.close()



#writerows
'''import csv
fh=open("bobby.csv","w",newline="")#newline m hi jaega
stu=csv.writer(fh)#is file m write krna h
stu.writerow(["Name","rollno","marks"])
list=[]
for i in range(5):
    print("student record")
    name=input("enter the name: ")
    rollno=int(input("enter the rollnumber: "))
    marks=float(input("enter the marks: "))
    sturec=[name,rollno,marks]
    list.append(sturec)
stu.writerows(list)  # to write too many lines in bulk
fh.close()'''

# import csv
# fh=open("palak.csv","r")
# stu=csv.reader(fh)
# for rec in stu:
#     print(rec)
# fh.close()




