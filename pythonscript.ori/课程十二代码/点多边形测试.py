import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                                                                 # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                                            # 创建可自动调整大小的窗口
cv.imshow("input", src)                                                                # 显示原始图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                                                      # 转换为灰度图
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)       # OTSU二值化
cv.imshow("binary", binary)                                                            # 显示二值图像

# 轮廓发现
image = np.zeros(src.shape, dtype=np.float32)                                                   # src.shape 继承原始图像的宽高和通道数，np.float32 确保支持负距离值存储
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)         # RETR_EXTERNAL 仅检测最外层轮廓
h, w = src.shape[:2]                                                                            # 获取图像的宽高
for row in range(h):
    for col in range(w):
        # cv.pointPolygonTest()用于计算点与多边形关系，返回三种值：正数：点到轮廓内部的最近距离，负数：点到轮廓外部的最近距离，零：点在轮廓上
        dist = cv.pointPolygonTest(contours[0], (col, row), True)                # (col, row)：待测试点的坐标（注意是(x,y)格式）
        if dist == 0:
            image[row, col] = (255, 255, 255)                                                  # 边界点（dist=0）：纯白色
        if dist > 0:
            image[row, col] = (255 - dist, 0, 0)                                               # 蓝色渐变
        if dist < 0:
            image[row, col] = (0, 0, 255 + dist)                                               # 红色渐变

dst = cv.convertScaleAbs(image)                                                                # cv.convertScaleAbs()：执行线性变换并取绝对值,自动将结果缩放到0-255范围
dst = np.uint8(dst)                                                                            # 强制转换为8位无符号整型,确保数据格式符合图像显示要求

# 显示
cv.imshow("contours_analysis", dst)
#cv.imwrite("D:/contours_analysis.png", dst)

cv.waitKey(0)                                                                                  # 等待按键
cv.destroyAllWindows()                                                                         # 关闭所有窗口


