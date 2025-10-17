import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)                                    # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)               # 创建可自动调整大小的窗口
cv.imshow("input", src)                                   # 显示图像
# cv.bilateralFilter（）即双边滤波，主要用于图像平滑处理的同时保留边缘细节   9：滤波核直径（必须是正奇数）
dst = cv.bilateralFilter(src, 9, 100,10)   # 100：颜色空间滤波参数（值越大，颜色相近的像素影响越大） 10：坐标空间滤波参数（值越大，距离越远的像素影响越大）
output = dst                                                       # 与高斯滤波对比,双边滤波能保留边缘但计算更耗时,高斯滤波会模糊所有高频信息
cv.imshow('output',output)

cv.waitKey(0)                                                      # 等待按键
cv.destroyAllWindows()                                             # 关闭所有窗口

