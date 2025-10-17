import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                              # 读取图像文件
# cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                # 创建可自动调整大小的窗口
# cv.imshow("input", src)                                    # 显示图像

# 卷积核直接锐化法（3x3卷积核（Kernel））
#sharpen_op = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)  # 总和为1 （9 + 8*(-1) = 1）保证亮度不变
sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32) # 总和为1 （5 + 4*(-1) = 1）保证亮度不变
# cv.filter2D()是OpenCV中用于图像卷积运算的核心函数，通过自定义核矩阵实现多种图像处理效果
sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)     # 生成含负值的浮点结果
# cv.convertScaleAbs()是用于处理卷积结果的关键后处理步骤，其作用是将锐化后的浮点型数据转换为可视化的8位无符号整型图像（0-255范围）
sharpen_image = cv.convertScaleAbs(sharpen_image)

cv.imshow('input',src)                             # 显示原图
cv.imshow('output',sharpen_image)                  # 显示锐化后的图像

cv.waitKey(0)                                               # 等待按键
cv.destroyAllWindows()                                      # 关闭所有窗口

