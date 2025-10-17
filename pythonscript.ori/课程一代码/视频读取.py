import cv2 as cv
import numpy as np


capture = cv.VideoCapture(VideoAddress)                 # 创建视频捕获对象，视频地址例："D:/images/rain.mp4"
#capture = cv.VideoCapture(0) #打开摄像头
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)          # 视频帧高度(像素)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)            # 视频帧宽度(像素)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)            # 视频总帧数
fps = capture.get(cv.CAP_PROP_FPS)                      # 视频帧率(帧/秒)
print(height, width, count, fps)

#输出路径："D:/images/test.mp4"（DivX编码的MP4文件），编码格式：cv.VideoWriter_fourcc('D','I','V','X')指定DivX编码器，帧率：30 FPS，分辨率：640×480像素，True表示保存彩色视频
#out = cv.VideoWriter("D:/images/test.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 30,(640, 480), True)
out = cv.VideoWriter("D:/images/test.mp4", cv.VideoWriter_fourcc(*'mp4v'), 30,(640, 480), True)  #编码格式：MP4V编码器（兼容性较好的MPEG-4编码）

while True:                                             # 无限循环（while True），用于持续读取视频流或摄像头帧
    ret, frame = capture.read()                         # ret：布尔值，表示帧是否成功读取，frame: 实际读取的图像帧数据
    if ret is True:                                     # 检查帧是否成功读取的布尔条件
        cv.imshow("video-input", frame)        # 在"video-input"的窗口中显示当前帧图像
        out.write(frame)                                # 将当前帧写入视频输出文件（需提前创建VideoWriter对象）
        c = cv.waitKey(50) & 0xFF
        if c == 27:                                     # ESC键的ASCII码值
            break                                       # 退出无限循环（两种情况触发：按ESC键或读取帧失败）
    else:                                               # 当ret为False时（视频结束或设备断开）退出循环
        break

capture.release()                                       # 调用release()释放资源
out.release()                                           # 释放视频写入器资源


