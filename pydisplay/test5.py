import cv2

# 获取摄像头
capture = cv2.VideoCapture(0)
# 设置格式
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# 设置输出文件路径和大小
out_file = cv2.VideoWriter("out.mp4", fourcc, 20, (640, 480))

while capture.isOpened():
    # 读取一帧,读取成功ret为True，frame为帧信息
    ret, frame = capture.read()
    if ret:
        # 将读取的帧写入文件
        out_file.write(frame)
        # 显示该帧图像
        cv2.imshow('frame', frame)
        # 设置退出按键
        if cv2.waitKey(1) == ord('q'):
            break