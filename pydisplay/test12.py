import re
import turtle
import numpy
import numpy as np

string="b'177418{0: (0.44, 0.87, 0.0285, -0.1153, -0.0508, 0)}177420{0: (0.49, 0.82, 0.0255, -0.1089, -0.04, 0)}'"
string="b'177418{0: (0.44, 0.87, 0.0285, -0.1153, -0.0508, 0),1: (0.48, 0.17, 0.0285, -0.1153, -0.0508, 0)}177420{0: (0.49, 0.82, 0.0255, -0.1089, -0.04, 0),1: (0.58, 0.07, 0.025, -0.1153, -0.0508, 0)}'"

# p4=re.search(r'[{](.*?)[}]',string, re.S).span()
# string=string[p4[0]:p4[1]]
# print(string[p4[0]:p4[1]])
# #

image = "2.gif"  # 要插入的图片


# turtle.setup(600,600)
# screen = turtle.Screen()
#
# screen.addshape(image)
# turtle.shape(name="circle")  # 设置当前的画笔形状为实心圆
# # turtle.shape(image)
turtleList=[]
print("----")
# print(tdata)

# turtleList.append(turtle.Turtle(shape=image))
# turtleList.append(turtle.Turtle(shape=image))

# print("----")
#
# for i in range(4):
#     if i==0:
#         turtleList.append(turtle.Turtle(shape=image))
#     if i==1:
#         turtleList.append(turtle.Turtle(shape="circle"))
#     # turtleList[i].speed('normal')
# print("=====")
#
#
# while True:
#
#     turtleList[0].goto(80, 49)
#
#     turtleList[1].goto(180, 49)
#     turtleList[0].shape(name="circle")
#     turtleList[0].goto(-70,90)


# def hus():
#     global oldlistlen
#     try:
#
#         if oldlistlen=='23':
#             pass
#         else:
#             print("ooooo")
#     except:
#         print("yichang")
#     print(oldlistlen)
#     oldlistlen="uhihi"
#     print(oldlistlen)
#
# if __name__ == '__main__':
#
#
#     oldlistlen=0
#     for i in range(2):
#         # hus()
#         print(i)
#         print("oo")

# arr=[]
# arr = np.append(arr,23)
# arr = np.append(arr,245)
# arr = np.append(arr,list1)
# oss=np.r_(arr,list4)

# a = np.array([[1,2,3]])
# b = np.array([2,5,8])
# 2代表下标，这里代表插入到第三列，axis=1，插入一列，axis=0，插入一行
# a1=np.insert(a, 0, list3, axis=0)
# a2=np.insert(a1, 0, list4, axis=0)
# a3=np.insert(a2, 0, list4, axis=0)
# print(a1)
# print("---")
# print(a2)
# print("---")
# print(a3)
# print("---")
#
# value = np.sum(a3, axis=0)
# print(value)
# sss=float(value[0])
# # print(type(sss))
# # print(value[0])
# # print(value[1])
# for i in value:
#     print(i)
#     if i>35:
#         list5.append(i)
# # print(i)
# print(list5)
# ss=np.argwhere(value > 10)
# # print(ss)
# for i in ss:
#     print(i)
#
# if 5 in ss:
#     print(",.,.,.")
# value = np.sum(a3, axis=1)
# print(value)
# print(np.insert(list1, 0, list2, axis=1))
# arr = np.append(arr,list2,axis=1)
# arr = np.append(arr,list3,axis=1)
# arr = np.append(arr,list4,axis=1)
# np.insert(arr, [0,1], c, axis=1)
# print(arr)
# print(oss)
def huu():
    global aa

    print(aa)
    aa=aa+1
    # print("12")
if __name__ == '__main__':
    aa=0
    # for i in range(5):
    #     huu()
    # list5 = []
    # n = 4
    a = numpy.zeros(shape=(0, 8))
    # print(a)
    # # for i in range(4):
    # #     list5.append(i)
    # # arr = np.append(6,list1)
    # list1 = [[1, 2, 3, 4]]
    list2 = [1, 3,2,3,3,2]
    list4=np.pad(list2, (0, 8-len(list2)), 'constant')

    list3 = [0, 3,3,3,3,2]
    list5=np.pad(list3, (0, 8-len(list3)), 'constant')

    list6 = [8, 2,0,3,3,2]
    list8=np.pad(list6, (0, 8-len(list6)), 'constant')

    print(list4)
    a1=np.insert(a, 0, list4, axis=0)
    a2 = np.insert(a1, 0, list5, axis=0)
    a3 = np.insert(a2, 0, list8, axis=0)
    print(a3)
    ssss=a3
    # ssss=a3.transpose()
    # # for z in ssss:
    # print(ssss)
    # a_1=np.delete(ssss,0,axis=0)
    # print(a_1)
    # value = np.sum(ssss, axis=1)
    # print(value)
    print("=-=-=-=")
    print(np.shape(ssss)[0])
    print(ssss.T[0])
    print("!!!!!!")
    for ww in range(len(list6)):
        print(ww)
        print(ssss.T[ww])
        print(np.sum(ssss.T[ww]))
        print(np.max(ssss.T[ww]))
        print(np.min(ssss.T[ww]))
        print(".....")
    # a_1 = np.delete(ssss, -1, axis=0)
    # print(a_1)
    #     ss = np.argwhere(ww == 0)
    #     if len(ss)==0:
    #         print(np.sum(ww)/6)
    #         print("正常!!")
        # print(ss)
    # print(a3)
    # print(ssss)
    # ss = np.argwhere(a2[0] > 10)
    # print(ss)
    # for i in range(5):
    #     print(i)
    #     a.append(i)
    # for z in range(8):
    #     b.append(z)
    # c.append(a)
    # c.append(b)
    # c.append(b)
    # print(c)
    # for z in
    # list_to_array = np.array(c)
    # print(list_to_array)

