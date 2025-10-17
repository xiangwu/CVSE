import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                                           # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                      # 创建可自动调整大小的窗口
cv.imshow("input", src)                                          # 显示图像
#gray=cv.pyrMeanShiftFiltering(src,10,100)                                # 基于金字塔的均值漂移（Mean Shift）图像滤波函数，用于图像平滑和边缘保留的降噪
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                                # 将BGR图像转为灰度图（减少计算维度）
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)               # 用9x9核进行高斯模糊（消除硬币边缘的高频噪声，避免Canny边缘检测产生伪边缘）
dp = 2                                                                    # 累加器分辨率与图像分辨率的反比（值越小检测越精细，但计算量越大）,2表示累加器是图像一半大小
param1 = 100                                                              # 边缘检测的高阈值（Canny检测用）（低阈值自动设为一半）
param2 = 80                                                               # 累加器阈值（决定圆检测的灵敏度，值越小假圆越多，建议根据实际检测效果动态调整）
# 用于圆形检测的HoughCircles函数调用, gray：输入灰度图像（需经过高斯模糊预处理）
# minDist=10：检测圆之间的最小中心距（单位：像素）;minRadius=20/maxRadius=100：硬币半径范围约束,过滤非目标半径的圆
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp, 300, None, param1, param2, 20, 150)
for c in circles[0,:]:                                                    # circles[0,:]从霍夫圆检测结果中提取N×3矩阵（每行包含圆心坐标(cx, cy)和半径r）
    print(c)
    cx, cy, r = c
    # 绘制圆心
    cv.circle(src, (int(cx), int(cy)), 2, (0, 255, 0), 2, 8, 0)     # 用绿色小圆点（半径2像素）标出圆心位置。
    # 绘制圆环
    cv.circle(src, (int(cx), int(cy)), int(r), (0, 0, 255), 2, 8, 0)      # 用红色线条（厚度2像素）勾勒检测到的圆边界。

# 显示
cv.imshow("hough line demo", src)
#cv.imwrite("D:/contours_analysis.png", src)

cv.waitKey(0)                                                              # 等待按键
cv.destroyAllWindows()                                                     # 关闭所有窗口



