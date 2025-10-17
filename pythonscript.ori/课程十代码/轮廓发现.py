import cv2 as cv
import numpy as np


def threshold_demo(image):                                 # 定义一个阈值函数
    # 去噪声+二值化
    dst = cv.GaussianBlur(image,(3, 3), 0)    # 使用3x3高斯核进行图像模糊去噪
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)             # 将彩色图像转为灰度图
    # 自动阈值二值化(使用OTSU算法)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY) # 应用OTSU自动阈值算法进行二值化，返回阈值(ret)和处理后的二值图像(binary)
    cv.imshow("binary", binary)                   # 显示二值化结果窗口
    return binary                                          # 返回二值图像

src = cv.imread(PictureAddress)                            # 读取指定路径的图片文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)       # 创建可自动调整大小的显示窗口
cv.imshow("input", src)                           # 显示原始图像
binary = threshold_demo(src)                               # 调用threshold_demo函数处理图像

# 轮廓发现
# OpenCV 4.x及以上版本改为返回2个值：(contours, hierarchy)
# cv.findContours是用于检测图像中物体轮廓的核心函数，cv.RETR_TREE：建立完整的轮廓层级关系树，cv.CHAIN_APPROX_SIMPLE：压缩水平/垂直/对角线方向的冗余点
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)# hierarchy：轮廓间的层级关系（树形结构）,contours：检测到的轮廓列表（每个轮廓是点集的数组）
for c in range(len(contours)):                             # contour_count = len(contours)，轮廓数量
# 绘制轮廓  src：目标图像矩阵（会被直接修改）;contours：轮廓集合（通常来自findContours的返回值）;c：指定绘制轮廓的索引（-1表示绘制所有轮廓）
    cv.drawContours(src, contours, c, (0, 255, 0), 1, 8)
# 显示
cv.imshow("contours-demo", src)

cv.waitKey(0)                                               # 等待按键
cv.destroyAllWindows()                                      # 关闭所有窗口


