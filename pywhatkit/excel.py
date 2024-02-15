import pywhatkit as py
import openpyxl
wb=openpyxl.load_workbook("Pywhat.xlsx")
ws=wb['Sheet1']
rows=ws.iter_rows(min_row=1,max_row=2,min_col=1,max_col=2)
phone=[]
for a,b in rows:
    phone.append(a.value)
print(phone)


img_path="C:/Users/palak/PycharmProjects/pywhatkit/sunny.png"

str="""
 opens In Manas College of Science Technology and Management.
For following Streams: 
BSc (I.T) Information Technology
B.Voc Hotel Management
B.Voc Graphic Designing and Animation
B.Voc Ecommerce and Digital Marketing
B.Voc Healthcare and Nutrition Management
B.Voc Banking and Financial Management
B.Voc Logistics Management
"""
for i in range(len(phone)):
    py.sendwhats_image(phone[i],img_path,str,10,True)