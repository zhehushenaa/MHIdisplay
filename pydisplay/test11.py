import re
import turtle

import socket

import numpy as np
import time
# string="b'177418{0: (0.44, 0.87, 0.0285, -0.1153, -0.0508, 0)}177420{0: (0.49, 0.82, 0.0255, -0.1089, -0.04, 0)}'"
# string="b'177418{0: (0.44, 0.87, 0.0285, -0.1153, -0.0508, 0),1: (0.48, 0.17, 0.0285, -0.1153, -0.0508, 0)}177420{0: (0.49, 0.82, 0.0255, -0.1089, -0.04, 0),1: (0.58, 0.07, 0.025, -0.1153, -0.0508, 0)}'"
#
# p4=re.search(r'[{](.*?)[}]',string, re.S).span()
# string=string[p4[0]:p4[1]]
# # print(string[p4[0]:p4[1]])
#
# p1 = re.compile(r'[(](.*?)[)]', re.S)  #最小匹配
# p5=re.findall(p1,string)
# print(p5)



def data_analysis(tdata):

    p4 = re.search(r'[{](.*?)[}]', tdata, re.S).span()
    string = tdata[p4[0]:p4[1]]
    # print(string)
    # #
    p1 = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
    tdata = re.findall(p1, string)
    # #
    # # print ("tdata")
    # print (tdata)
    return tdata




def falldection(tdata):
    global allxlist
    global allylist
    global allzlist
    n=20

    for v in tdata:
        a=v.split(",",5)

        xf=float(a[0])
        xf = int(xf * 100)

        yf=float(a[1])
        yf = int(yf * 100)

        z=float(a[3])
        z = int(z * 100)


        updatex_z.append(xf)
        updatey_z.append(yf)
        updatez.append(z)

    if updatez[0]!=0 and updatex_z[0]!=0 and updatey_z[0]!=0:
        listx = np.pad(updatez, (0, 8 - len(updatex_z)), 'constant')
        allxlist = np.insert(allxlist, 0, listx, axis=0)

        listy = np.pad(updatez, (0, 8 - len(updatey_z)), 'constant')
        allylist = np.insert(allylist, 0, listy, axis=0)

        listz = np.pad(updatez, (0, 8 - len(updatez)), 'constant')
        allzlist = np.insert(allzlist, 0, listz, axis=0)
    # allzlist = np.append(allzlist,listz,axis=0)
    if np.shape(allzlist)[0]==n:
        for i in range(len(tdata)):

            xx=np.max(allxlist.T[i])-np.min(allxlist.T[i])
            yy=np.max(allylist.T[i])-np.min(allylist.T[i])
            zz=((xx**2)+(yy**2))**0.5
            localTime = time.asctime(time.localtime(time.time()))
            print(localTime)
            print(str(np.max(allxlist.T[i])),str(np.min(allxlist.T[i])))
            print(zz)
            print((np.sum(allzlist.T[i]))/n)
            if zz<80 and (np.sum(allzlist.T[i])/n)<-10:
                print("跌倒啦！！")
                print("++++")


            # if (np.sum(allxlist.T[i])/n)<-15:
        allxlist = np.delete(allxlist, -1, axis=0)
        allylist = np.delete(allylist, -1, axis=0)
        allzlist = np.delete(allzlist, -1, axis=0)


    # if np.shape(allzlist)[0]==n:
    #     for ww in allzlist.T:
    #         # print(ww)
    #         ss = np.argwhere(ww == 0)
    #         if len(ss) == 0:
    #
    #             print(localTime)
    #             print(np.sum(ww) / n)
    #             if (np.sum(ww)/n)<-15:
    #                 print("跌倒!!")
            # print(ss)

        # print("allzlist:")
        # print(allzlist)





def turtledisplay(tdata):

    global oldlistlen

    # turtle.shape(image)
    culistlen=len(tdata)
    # print(culistlen)
    try:
        if oldlistlen==culistlen:
            pass
        if oldlistlen>culistlen:
            for i in range(oldlistlen-culistlen):
                turtleList.pop()
        if oldlistlen<culistlen:
            for j in range(culistlen-oldlistlen):
                turtleList.append(turtle.Turtle(shape=image))
    except:
        print("yichang")

        # turtleList[i].speed('normal')
    print("=====")





    for v in tdata:
        a=v.split(",",5)
        x=float(a[0])
        y=float(a[1])
        x = int(x * 100)
        y = int(y * 100)
        # z = int(z * 100)

        updatex.append(x)
        updatey.append(y)

        print("1")
        print(culistlen)
        for k in range(culistlen):
            # pass
            # turtleList[i].showturtle()
            turtleList[k].penup()
            # print ("updatex,updatey:")
            # print (updatex[k],updatey[k])
            # if k==op:
            #     turtleList[k].shape(name="circle")
            turtleList[k].goto(updatex[k], updatey[k])
            #
            # # turtle.speed(3)
            # # turtleList[i].delay(10)
            # turtleList[i].penup()
    oldlistlen=culistlen
    #
    # print (updatex[0],updatey[0])
    # turtleList[0].goto(updatex[0], updatey[0])
    # print("len:", str(len(turtleList)))

# def handle(p5):
#     for i in p5:
#         print(i)
#         a=i.split(",",5)
#         x.append(float(a[0]))
#         y.append(float(a[1]))
#         print(len(a))
#         print("-----")
#
#     print(x,y)
#
#
#
#     turtle.goto(i,j)



if __name__ == '__main__':



    poszlist = []
    velzlist = []
    acczlist = []
    P = 0
    bit = 1
    alarm = 0
    peoplep = 0
    poszsum = 0
    velzsum = 0
    acczsum = 0
    nopeoplenum=0
    originalbitheight = 0
    oldx = []
    oldy = []
    turtleList = []

    oldlistlen = 0

    poszlist = []
    velzlist = []
    acczlist = []
    maxPoints = 1150

    allmaxpoints = []

    MaxBytes = 1024 * 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(60)
    host = '192.168.1.182'
    # host = socket.gethostname()
    port = 11223
    server.bind((host, port))  # 绑定端口

    server.listen(1)  # 监听
    inputData = '2'
    # if (inputData == "quit"):
    #     print("我要退出了，再见")
    #     break


    image = "2.gif"  # 要插入的图片

    allxlist= np.zeros(shape=(0,8))
    allylist = np.zeros(shape=(0, 8))
    allzlist = np.zeros(shape=(0, 8))


    inputData = input("设备操作(1-设置，2-工作模式，3-恢复出厂设置，quit-退出)：")  # 等待输入数据
    screen = turtle.Screen()

    screen.addshape(image)
    print(inputData)
    if inputData=='2':
        # try:
        client, addr = server.accept()  # 等待客户端连接
        print(addr, " 连接上了")
        client.send(inputData.encode())
        while True:
            updatex = []
            updatey = []
            updatez = []
            updatex_z = []
            updatey_z = []


            tdata = str(client.recv(MaxBytes))
            print(tdata)
            if "{" in tdata:
                nopeoplenum=0
                tdata=data_analysis(tdata)
                print(tdata)
                falldection(tdata)
                turtledisplay(tdata)
            else:
                nopeoplenum=nopeoplenum+1
            if nopeoplenum==30:
                oldlistlen=0
                turtleList=[]
                turtle.clearscreen()
                nopeoplenum=0

                # if not tdata:
                #     print('数据为空，我要退出了')
                #     break
        # except BaseException as e:
        #     print("出现异常：")
        #     print(repr(e))
        # finally:
        #     server.close()  # 关闭连接
        #     print("我已经退出了，后会无期")

