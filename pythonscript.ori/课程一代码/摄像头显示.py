import cv2
import numpy as np

# 打开默认摄像头（通常是0，如果有多个摄像头，则可能是1, 2, ...）
cap = cv2.VideoCapture(0)
# 检查摄像头是否成功打开
if not cap.isOpened():                                 # cap.isOpened() 检查视频捕获对象初始化状态
    print("Error opening video stream or file")
    exit()                                             # 终止程序
while True:                                            # 无限循环（while True），用于持续读取视频流或摄像头帧
    # 读取一帧
    ret, frame = cap.read()                            # ret：布尔值，表示帧是否成功读取，frame: 实际读取的图像帧数据
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 显示结果帧
    cv2.imshow('Camera', frame)
    # 等待用户按键，如果按下'q'时执行break退出循环
    # cv2.waitKey(1)：这个函数等待用户按键，最多等待1毫秒。如果用户按下了某个键，它返回该键的ASCII值；如果没有按键，则返回 - 1
    # & 0xFF的按位与操作只取cv2.waitKey(1)返回值最后八位，因为有些系统cv2.waitKey(1)的返回值不止八位
    # cv2.waitKey(1) & 0xFF，与位运算，当按‘q’时返回ASCII=113
    if cv2.waitKey(1) & 0xFF == ord('q'):              # ord('q') 获取字符'q'的ASCII码，即113
        break

# 释放摄像头并关闭所有OpenCV窗口
cap.release()                                          # 调用release()释放资源
cv2.destroyAllWindows()                                # 关闭所有窗口












