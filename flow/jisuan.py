# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import math
import csv

def quaternion_to_euler(x, y, z, w):

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))

        return X, Y, Z

def seek_value(inText,seekSign):
        sSite = inText.find(seekSign, 0) + len(seekSign)
        eSite = inText.find("\n", sSite)
        # print(inText[sSite:eSite])
        # print(sSite,eSite)
        outValue = float(inText[sSite:eSite])
        return outValue


def seek_orientation(inText):
        x = seek_value(inText,r"x: ")
        # y = seek_value (inText, r"y: ")
        # z = seek_value (inText, r"z: ")
        # w = seek_value (inText, r"w: ")
        print(type(x))
        return x

# 打开文件
def init_file(InPath):
    try:
        fs = open(InPath, 'w', newline='')
        WriterFile = csv.writer(fs)
        return WriterFile, fs
    except:
        return False, False


def write_file_menu(path_file ,x,y,MenuLen):
    WriterFile, fs = init_file(path_file)
    if (WriterFile != False):
        WriterFile.writerow(["liuliang"])
        # print(int(inTemp[0][0:-1]))
        for n in range(0, MenuLen):
        # for n in x:
                # print(n)
                WriterFile.writerow ([x[n],y[n]])

        fs.close()

def sign_num(inText,textlen):
    textLen = len(inText)
    iSite = 0
    outNum  =0
    for n in range(0,8298):

        startSite = text.find (r"orientation:", iSite) + textlen
        if(startSite > 0):
            iSite = startSite
            outNum = outNum + 1
        else:
            break
    return outNum

if __name__ == '__main__':
        # with open ("huati.log", "rb",encoding='utf-16-le') as f:  # 打开文件
        #         data = f.read ()  # 读取文件
        #         print(data)
        with open ("1.log", "rb") as data:
                # header = data.read (8)
                text = data.read ().decode ('utf-16-le')
                # print(re.search (r"orientation:", text))
                # endSite = text.find(r"orientation:", 0)
                # print(text[221:300])

                textlen = len("traffic:")
                initialSite = 0
                # print(sign_num(text,textlen))
                maxNum = 137
                liuliang=[0]*maxNum
                reslut= [0]*maxNum

                # y=[0]*maxNum
                # z=[0]*maxNum
                # w=[0]*maxNum
                # Pitch=[0]*maxNum
                # Yaw=[0]*maxNum
                # Roll=[0]*maxNum


                for n in range(0,maxNum):
                        startSite = text.find (r"traffic:", initialSite)+ textlen
                        endSite = text.find (r",xishu:", startSite)
                        initialSite = endSite
                        # print(text[startSite:endSite])
                        liuliang[n] = text[startSite:endSite]
                        # print(float(text[startSite:endSite]))
                        # liuliang = seek_orientation (text[startSite:endSite])
                        # Pitch[n], Yaw[n], Roll[n] = quaternion_to_euler(x[n], y[n], z[n], w[n])
                        # print(x[n], y[n], z[n], w[n])
                        # print( Pitch[n], Yaw[n], Roll[n])
                # print(liuliang)
                addData = 0
                sumData = 0
                jiData = 0
                useData = 3
                linData = [0] * useData
                for n in liuliang:

                    if(addData >= useData):
                        print("shiyan",linData)
                        sumData = sum(linData) - max(linData) - min(linData)
                        reslut[jiData] = sumData//(useData-2)
                        jiData+=1
                        addData=0
                        sumData = 0
                    else:
                        linData[addData] = float(n)
                        addData += 1


                print("result:",reslut)

                write_file_menu ("./result2.csv",liuliang,reslut,maxNum)
                print("++++++++++++++ Succed +++++++++++")
        print("+++++++++++ End +++++++++++")






                # for line in data.readlines():
                #         print(line.decode ('utf-16-le'))

                # print(text)


        # print(quaternion_to_euler (0.0,0.0,-0.341585142476,0.939850834143))

