
import os

path="C:/Users/xxxx/JPEGImages"
#测试图片所在目录，linux路径用pwd获取

lists=os.listdir(path)
list_txt = open('train.txt', 'w')
for list in lists:
    if list[-4:]==".jpg":
        list_txt.write(path+"/"+list+"\n")
    print("save--"+path+"/"+list)
list_txt.close()

"""
train.txt:

C:/Users/xxxx/JPEGImages/1_000000.jpg
C:/Users/xxxx/JPEGImages/1_000001.jpg
"""
    
