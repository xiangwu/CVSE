import numpy as np
import cv2 as cv


src = cv.imread(PictureAddress, cv.IMREAD_GRAYSCALE)           # cv.IMREAD_GRAYSCALE 表示以灰度模式读取图像，图像地址例："D:/images/nezha.png"
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)           # 创建可自动调整大小的窗口
cv.imshow('input',src)                                # 显示图像


# cv.minMaxLoc()是OpenCV中用于分析图像矩阵的核心函数，主要用于获取单通道图像（如灰度图）的极值信息
# minVal：图像中的最小像素值（浮点数；maxVal：图像中的最大像素值（浮点数）；minLoc:最小值坐标 (x, y) 的元组；maxLoc：最大值坐标 (x, y) 的元组
min, max, minLoc, maxLoc = cv.minMaxLoc(src)
print("min: %.2f, max: %.2f"%(min, max))                       # %.2f：控制浮点数保留2位小数
print("min loc: ", minLoc)                                     # 输出最小值所在位置坐标
print("max loc: ", maxLoc)                                     # 输出最大值所在位置坐标

cv.waitKey(0)                                                  # 等待按键
cv.destroyAllWindows()                                         # 关闭所有窗口