import pyautogui as p
import time
message=input("enter your message")
limit=input("enter the limit")
i=0
time.sleep(5)
while i<int(limit):
    p.typewrite(message)
    p.press("enter")
    i+=1
