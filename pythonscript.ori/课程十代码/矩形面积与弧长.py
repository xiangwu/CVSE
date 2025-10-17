import cv2 as cv
import numpy as np


def canny_demo(image):                                                # 定义一个名为canny_demo的函数
    t = 80                                                            # 设置Canny边缘检测的低阈值为80
    canny_output = cv.Canny(image, t, t * 2)                          # 高阈值t * 2为160
    cv.imshow("canny_output", canny_output)                  # 显示边缘检测结果
    #cv.imwrite("D:/canny_output.png", canny_output)                  # 存储结果
    return canny_output                                               # 返回边缘检测后的二值图像（白色为边缘，黑色为背景）

src = cv.imread("D:/images/nezha.png")                                # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                  # 创建可自动调整大小的窗口
cv.imshow("input", src)                                      # 显示图像

edge_binary = canny_demo(src)                                         # 调用canny_demo函数
k = np.ones((3, 3), dtype=np.uint8)                             # 创建了一个3×3的全1矩阵（卷积核）
binary = cv.morphologyEx(edge_binary, cv.MORPH_DILATE, k)             # 图像形态学膨胀操作

# 轮廓发现
# OpenCV 4.x及以上版本改为返回2个值：(contours, hierarchy)
# cv.findContours是用于检测图像中物体轮廓的核心函数，cv.RETR_EXTERNAL提取所有外部轮廓，cv.CHAIN_APPROX_SIMPLE：压缩水平/垂直/对角线方向的冗余点
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # x, y, w, h = cv.boundingRect(contours[c]);                      # cv.boundingRect() 计算轮廓的最小正外接矩形（非旋转矩形）
    # cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)            # 绘制轮廓线（红色）
    # cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0);    # 绘制外接矩形
    area = cv.contourArea(contours[c])                                # 第c个轮廓的像素面积
    arclength = cv.arcLength(contours[c], True)                # arclength(弧长)通常指通过函数计算曲线或闭合轮廓的周长
    # print(area, arclength)
    # 轮廓筛选
    if area < 100 or arclength < 100:                                 # 跳过面积<100或周长<100的小轮廓
        continue
    # minAreaRect()返回包含旋转矩形信息的元组，格式为：((cx, cy), (width, height), angle)
    rect = cv.minAreaRect(contours[c])                                # 计算轮廓的最小面积外接旋转矩形
    cx, cy = rect[0]                                                  # 获取矩形中心点坐标
    box = cv.boxPoints(rect)                                          # 获取矩形的4个顶点坐标
    box = np.int32(box)
    cv.drawContours(src,[box],0,(0,0,255),2)                                              # 在原始图像上绘制红色矩形框
    cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)         # 在中心点绘制蓝色圆点
# 显示
cv.imshow("contours_analysis", src)
#cv.imwrite("D:/contours_analysis.png", src)                          # 存储结果

cv.waitKey(0)                                                         # 等待按键
cv.destroyAllWindows()                                                # 关闭所有窗口


