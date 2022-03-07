
import socket               # 导入 socket 模块
import time

def apsetting():
    s = socket.socket()         # 创建 socket 对象
    host = '192.168.4.1'      # esp32 ip
    port = 10000                # 设置端口号

    s.connect((host, port))

    print("wifi已连接")
    # msg = input()
    time.sleep(0.05)
    # Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    msg1 = input("请输入wifi名称：")

    # msg1="test"
    # Time=Time.encode()
    msg2 = input("请输入wifi密码：")
    # msg2="henganzhuoyue"
    msg3 = input("请输入您的IP地址：")
    msg4 = input("请输入房间长度：")

    msg5 = input("请输入房间宽度：")

    msg1 = msg1.encode()
    msg2 = msg2.encode()
    msg3 = msg3.encode()
    msg4 = msg4.encode()
    msg5 = msg5.encode()
    s.send(msg1)
    time.sleep(0.05)
    s.send(msg2)
    time.sleep(0.05)
    s.send(msg3)
    time.sleep(0.05)
    s.send(msg4)
    time.sleep(0.05)
    s.send(msg5)
    data = s.recv(1024)  # 接收数据（1024字节大小）
    print(data)

def working():
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

    try:
        client, addr = server.accept()  # 等待客户端连接
        print(addr, " 连接上了")
        client.send(inputData.encode())
        while True:
            data = client.recv(MaxBytes)
            print(data)
            if not data:
                print('数据为空，我要退出了')
                break
            # localTime = time.asctime(time.localtime(time.time()))
            # print(localTime, ' 接收到数据字节数:', len(data))
            # print(sendBytes)
            # client.send(data)
    except BaseException as e:
        print("出现异常：")
        print(repr(e))
    finally:
        server.close()  # 关闭连接
        print("我已经退出了，后会无期")

def reset():
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
            #inputData = input("模式选择(1为开始，2为重置)：")  # 等待输入数据
            inputData='3'
            # if (inputData == "quit"):
            #     print("我要退出了，再见")
            #     break
            sendBytes = client.send(inputData.encode())
            if sendBytes <= 0:
                break
            if inputData=='3':
                print("reset,success!!")
                break
            # localTime = time.asctime(time.localtime(time.time()))
            # print(localTime, ' 接收到数据字节数:', len(data))
            print(sendBytes)
            # client.send(data)
    except BaseException as e:
        print("出现异常：")
        print(repr(e))
    finally:
        server.close()  # 关闭连接
        print("我已经退出了，后会无期")

if __name__ == '__main__':
    inputData = input("设备操作(1-设置，2-工作模式，3-恢复出厂设置，quit-退出)：")  # 等待输入数据
    print(inputData)
    if inputData=='1':
        apsetting()
    if inputData=='2':
        working()
    if inputData=='3':
        reset()
    # if (inputData == "quit"):
    #     print("我要退出了，再见")
