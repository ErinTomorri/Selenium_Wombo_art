'''
You dont need to run this part. this will just put a blue square in the middle

'''



from selenium import webdriver
import time
import glob
import os
PATH = 'C:\Program Files (x86)\chromedriver.exe'
path = "enter path to where u keep ur images"
a = glob.glob(path)

num = 0
num1 = 45
print (a)
# Absolute path of a file
old_name = a
new_name = test1
os_re = test3+'Zima-Blue#'+str(num1)+'.jpg', test2+'Zima-Blue#'+str(num1)+'.jpg'
# Renaming the file
for num in range(len(a)):
    os.rename(a[num], 'Zima-Blue#'+str(num1)+'.jpg')
    os.replace(os_re)
    num1+=1
    num+=1
