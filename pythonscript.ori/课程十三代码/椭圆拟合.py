import cv2 as cv
import numpy as np


def canny_demo(image):                                        # 定义一个名为canny_demo的函数
    t = 80                                                    # 设置Canny边缘检测的低阈值为80
    canny_output = cv.Canny(image, t, t * 2)                  # 高阈值t * 2为160
    cv.imshow("canny_output", canny_output)          # 显示边缘检测结果
    #cv.imwrite("D:/canny_output.png", canny_output)          # 存储结果
    return canny_output                                       # 返回边缘检测后的二值图像（白色为边缘，黑色为背景）

src = cv.imread(PictureAddress)                               # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)          # 创建可自动调整大小的窗口
cv.imshow("input", src)                              # 显示图像
edge_binary = canny_demo(src)                                 # 调用canny_demo函数
k = np.ones((3, 3), dtype=np.uint8)                     # 图像处理中用作卷积核
binary = cv.morphologyEx(edge_binary, cv.MORPH_DILATE, k)     # 膨胀操作

# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)    # cv.RETR_EXTERNAL提取所有外部轮廓
for c in range(len(contours)):
    # 椭圆拟合,cv.fitEllipse() 对轮廓点集进行最小二乘椭圆拟合，返回椭圆几何参数
    (cx, cy), (a, b), angle = cv.fitEllipse(contours[c])      # (cx, cy)：椭圆中心坐标（浮点精度）;(a, b)：长短轴长度（注意a不总是长轴）， angle：旋转角度（顺时针方向，单位：度）
    # 绘制椭圆
    cv.ellipse(src, (np.int32(cx), np.int32(cy)),             # (np.int32(cx), np.int32(cy)), 椭圆中心坐标（强制转换为整型），(np.int32(a/2), np.int32(b/2)), 半轴长度（需除以2后取整）
    (np.int32(a/2), np.int32(b/2)), angle, 0, 360, (255, 0, 255), 2, 8, 0)   # angle,旋转角度， 0, 360,起始和结束角度（0-360表示完整椭圆）
# 显示
output = src
cv.imshow('output',output)

cv.waitKey(0)                                                 # 等待按键
cv.destroyAllWindows()                                        # 关闭所有窗口

