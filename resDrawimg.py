import cv2
import os

import numpy as np
import matplotlib.pyplot as plt

imgPath="./haze"
resPath="./result/2/"

#先删掉txt开头结尾无用信息 第一个检测用时较长统一长度Predicted in 211.740000 milli-seconds -->21.740000 milli-seconds
with open("result.txt", "r") as f:
    #print(type(f))
    name=""
    imgList=[] #存放name每个图片为一个元素
    imgBoxes=[] #存放name+"*"+检测框，每个框为一个元素
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        #Enter Image Path: /xxx/xxx/xxx/xxx/JPEGImages/huwai_1_000008.jpg: Predicted in 21.531000 milli-seconds.
        if line[18]=="/":
            # print("-----name-----")
            #xx/xx/xx/huwai_1_000008.jpg -->huwai_1_000008
            name=line[70:][:-43]
            imgList.append(line[70:][:-43])
            #print(line[70:][:-43])
        else:
            # print(name+line)
            imgBoxes.append(name+"*"+line)
            #huwai_1_000008*class: 99%	(left_x:  118   top_y:   63   width:   68   height:   62)
        # print("-----draw-----")
        # if line[0:3]=="cow":
            # print(name+line)
        # else
    # for box in imgBoxes:
        # print(box[0:box.rfind('*')]) #取*前面的name
        # print(box[box.rfind('*')+1:]) #取*后面的name包含的box
        
    
    # for imgName in imgList:
        # print(imgName)
    # for box in imgBoxes:
        # print(box[0:box.rfind('*')])
    #得到两个List后
    
    cmap = plt.get_cmap('tab20b')
    colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]
    color = colors[int(4) % len(colors)]
    #修改int(4)里面的数字换为其他颜色
    color = [i * 255 for i in color]     
    
    for imgName in imgList:
        i=0 #一个图片几个框
        im = cv2.imread(os.path.join(imgPath,imgName)+".jpg")
        print(imgName)
        for box in imgBoxes:
            i=i+1
            print(box[0:box.rfind('*')])
            if box[0:box.rfind('*')]==imgName: #匹配name，对于imgName的box
                boxList=box[box.rfind('*')+1:].split() #name包含的box [class,conf,_,x,_,y,_,w,_,h] str类型
                sx1=int(boxList[3])
                sy1=int(boxList[5])
                sx2=int(boxList[3])+int(boxList[7])
                sy2=int(boxList[5])+int(boxList[9][:-1])
                text=boxList[0]+boxList[1]
                
                #画框，文本
                cv2.rectangle(im,(sx1,sy1),(sx2,sy2),color,3)
                if sy1 > 25:
                    cv2.rectangle(im, (sx1, sy1-20), (sx1+(len(boxList[0])+1)*17, sy1), color, -1)
                    cv2.putText(im, text,(sx1, sy1-10),0, 0.75, (255,255,255),2)
                else:
                    cv2.rectangle(im, (sx1, sy1), (sx1+(len(boxList[0])+1)*17, sy1+20), color, -1)
                    cv2.putText(im, boxList[0]  + boxList[1],(sx1, sy1+20),0, 0.75, (255,255,255),2)
            else:
                break      
        cv2.imwrite(os.path.join(resPath,imgName)+"_result.jpg",im)
        print("save result:\t"+os.path.join(resPath,imgName)+"_result.jpg")
        del imgBoxes[0:i-1] #删除已经画过的框
