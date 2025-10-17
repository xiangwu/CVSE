from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np

# Create an image (创建400x400像素的纯黑图像（4*r=400）)
r = 100
src = np.zeros((4*r, 4*r), dtype=np.uint8)
# Create a sequence of points to make a contour（创建一系列点以形成轮廓）
#定义了一个六边形的顶点坐标，常用于计算机图形学中的多边形绘制
vert = [None]*6                                                           # 使用[None]创建单元素列表，通过*6运算符复制6次
# 六边形顶点坐标的数学表达式六边形顶点坐标的数学表达式
vert[0] = (3*r//2, int(1.34*r))     # 第一象限顶点                          # 3*r//2：计算x坐标（半径的1.5倍取整），int(1.34*r)：计算y坐标（1.34倍半径取整)，1.34≈2-sqrt(3)/2（六边形的垂直偏移系数）
vert[1] = (1*r, 2*r)                # 第二象限上部顶点
vert[2] = (3*r//2, int(2.866*r))    # 第二象限下部顶点                       # 垂直间距：约0.866*r（sin(60°)*r）
vert[3] = (5*r//2, int(2.866*r))    # 第三象限顶点
vert[4] = (3*r, 2*r)                # 第四象限顶点
vert[5] = (5*r//2, int(1.34*r))     # 第一象限下部顶点

# 补充
# OpenCV绘制六边形示例
#pts = np.array(vert, np.int32)
#cv.polylines(src, [pts], True, (0,255,0), thickness=2)

# Draw it in src（在原图中绘制它）
for i in range(6):                                                          # range(6) 遍历六边形的6个顶点，
    cv.line(src, vert[i],  vert[(i+1)%6], ( 255 ), 3)              # vert[i]：当前顶点坐标，vert[(i+1)%6]：通过取模运算实现环形索引（第6点连接回第1点），(i+1)%n是处理闭合多边形的经典模式

# Get the contours（获取轮廓）
contours, _ = cv.findContours(src, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)    # cv.RETR_TREE：检索所有轮廓并重建层级关系

# Calculate the distances to the contour
raw_dist = np.empty(src.shape, dtype=np.float32)                            # 使用NumPy创建了一个与输入图像src维度相同的空浮点数组，是图像处理中常见的预分配内存操作
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        # cv.pointPolygonTest() 执行点与多边形的几何关系检测，返回三种值：正数：点到轮廓内部的最近距离，负数：点到轮廓外部的最近距离，零：点在轮廓上
        # (j,i)：测试点坐标（注意OpenCV的(x,y)对应numpy的[行,列]即(i,j); contours[0]：输入的多边形轮廓（通常来自findContours结果）
        raw_dist[i,j] = cv.pointPolygonTest(contours[0], (j,i), True)     # True：启用带符号距离计算（正值为内部，负值为外部）

# 获取最大值即内接圆半径，中心点坐标
# minVal：矩阵中的最小值（最近距离） maxVal：矩阵中的最大值（最远距离）  _：忽略的最小值位置（用占位符_表示）  maxDistPt：最大值坐标点（Point类型）
minVal, maxVal, _, maxDistPt = cv.minMaxLoc(raw_dist)
# 取绝对值，确保距离值为正
minVal = abs(minVal)
maxVal = abs(maxVal)                                                         # 在形状分析中，maxVal常表示物体的最大内接圆半径

# Depicting the  distances graphically（用图形描绘距离）
drawing = np.zeros((src.shape[0], src.shape[1], 3), dtype=np.uint8)    # 创建了一个用于图像绘制的空白RGB画布; src.shape[0]：图像高度（行数);src.shape[1]：图像宽度（列数）
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
# 根据距离值(raw_dist)的正负进行不同通道的着色; 采用反相处理(255-x)增强视觉对比度
        if raw_dist[i,j] < 0:                                                 # 负距离值：蓝色通道(B)渐变（距离越近值越大）,使用minVal进行归一化到[0,255]
            drawing[i,j,0] = 255 - abs(raw_dist[i,j]) * 255 / minVal
        elif raw_dist[i,j] > 0:                                               # 正距离值：红色通道(R)渐变（距离越近值越大）,使用maxVal进行归一化到[0,255]
            drawing[i,j,2] = 255 - raw_dist[i,j] * 255 / maxVal
        else:                                                                 # 零值点显示为白色(RGB=255,255,255)
            drawing[i,j,0] = 255
            drawing[i,j,1] = 255
            drawing[i,j,2] = 255

# max inner circle
# maxDistPt：圆心坐标(Point类型);int(maxVal)：圆半径（取整后的最大距离值）;0：位移参数（默认0）
cv.circle(drawing,maxDistPt, int(maxVal),(255,255,255), 1, cv.LINE_8, 0)   # 半径使用maxVal保证包含所有有效区域
#cv.imshow('Source', src)
cv.imshow('Distance and inscribed circle', drawing)

cv.waitKey(0)                                                                # 等待按键
cv.destroyAllWindows()                                                       # 关闭所有窗口
