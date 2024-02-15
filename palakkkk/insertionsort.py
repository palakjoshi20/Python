# def second_max_min(a):
#     for i in range (1,len(a)):
#         key=a[i]
#         j=i-1
#         while j>=0 and key<a[j]:
#             a[j+1]=a[j] #shift elememts to right to make room for key
#             j=j-1
#         else:
#             a[j+1]=key
#     print("sorted list is ",a)#First we have a sorted list
#     print("The second maximum element is ",a[len(a)-2])#the second last element of the sorted list will be The second max
#     print("The second minimum element is ",a[1])#the second element of the sorted list will be The second min
#
# a=[15,6,13,22,3,53,2]
# second_max_min(a)


#
# array=[0,0,1,0,1,1,0,1]#given array that needs to be sorted
#
# array1=[]#create an empty array
#
# count0=0
# count1=0
#
# for i in array:
#     if i==0:
#         count0+=1#increase 0 count
#     else:
#         count1+=1#increase 1 count
#
# #Append number of 0's in the empty array according to count0
# for i in range(count1):
#     array1.append(0)
#
# #Append number of 1's in the empty array according to count1
# for i in range(count0):
#     array1.append(1)
#
# print(array1)#Required Output array
#


# def valid_email(email):
#     if "@" in email and "." in email:
#         # Split the email address into local and domain parts
#         local, domain = email.split("@")
#
#         # Check local part: it should not start or end with a dot, and no consecutive dots are allowed
#         if local and not local.startswith(".") and not local.endswith(".") and ".." not in local:
#             # Check domain part: it should not start or end with a dot, and contain at least one dot
#             if domain and not domain.startswith(".") and not domain.endswith(".") and "." in domain:
#                 return True
#     return False
#
#
# # Example usage
# email = "example@email.com"
# if valid_email(email):
#     print(f"{email} is a valid email address.")
# else:
#     print(f"{email} is not a valid email address.")


def valid_email(email):
    if "@" and "." in email:#to check if there's @ and "." in the given string
        if len(email) < 3:#len should be>3
            return False

        if email.count("@")!=1 and email.count(".")<=2:
            return False
        #split the string into 2 parts one before the @ and one after the @

        front,back = email.split('@')
        if front[0] == '.' or front[-1] == '.' or back[0] == '.' or back[-1] == '.':
            return False

        if front.count(".")>1 or back.count(".")>1:
            return False

        return True
#Note: I've tried to put all test cases in the code above but few may have missed
email=input("Enter the Email: ")
if valid_email(email)==True:
    print(True)
else:
    print(False)

