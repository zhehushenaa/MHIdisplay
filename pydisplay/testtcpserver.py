import socket
import time

MaxBytes = 1024 * 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(60)
host = '192.168.1.182'
# host = socket.gethostname()
port = 11223
server.bind((host, port))  # 绑定端口

server.listen(1)  # 监听
try:
    client, addr = server.accept()  # 等待客户端连接
    print(addr, " 连接上了")
    data = client.recv(MaxBytes)
    print(data)
    while True:

        # if not data:
        #     print('数据为空，我要退出了')
        #     break
        inputData = input("模式选择(1为开始，2为重置)：")  # 等待输入数据
        if (inputData == "quit"):
            print("我要退出了，再见")
            break
        sendBytes = client.send(inputData.encode())
        if sendBytes <= 0:
            break
        #localTime = time.asctime(time.localtime(time.time()))
        #print(localTime, ' 接收到数据字节数:', len(data))
        print(sendBytes)
        #client.send(data)
except BaseException as e:
    print("出现异常：")
    print(repr(e))
finally:
    server.close()  # 关闭连接
    print("我已经退出了，后会无期")
