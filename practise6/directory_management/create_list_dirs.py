import os

#ex1 
os.mkdir("test1_fol")

#ex2 
os.makedirs("lv1/lv2/lv3")

#or

os.makedirs("parent/child", exist_ok = True)

#ex3
files = os.listdir()
print(files)