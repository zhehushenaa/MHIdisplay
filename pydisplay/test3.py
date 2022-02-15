
import socket               # 导入 socket 模块
import time

s = socket.socket()         # 创建 socket 对象
host = '192.168.87.87'      # esp32 ip
port = 10000                # 设置端口号

s.connect((host, port))

if __name__ == '__main__':
    while True:
        # msg = input()
        time.sleep(0.05)
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        msg="you"
        Time=Time.encode()
        msg=msg.encode()
        s.send(Time)
        s.send(msg)
        data = s.recv(1024)  # 接收数据（1024字节大小）
        print(data)