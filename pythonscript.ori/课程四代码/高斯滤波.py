import cv2  as cv
import numpy as np


img = cv.imread(PictureAddress)                            # 高斯滤波,主要用于图像平滑和降噪处理
gaussian = cv.GaussianBlur(img, (5, 5), 2)    # (5,5)：5x5高斯核（必须为奇数），核尺寸越大模糊效果越强，会损失图像高频信息（边缘细节），2：X方向标准差（σ），值越大模糊越强
#gaussian = cv.GaussianBlur(img, (5, 5), 0)                # σ=0时自动根据核尺寸计算σ值

cv.imshow("input", img)                           # 显示原始图像
cv.imshow('output',gaussian)                      # 显示高斯模糊后的图像

cv.waitKey(0)                                              # 等待按键
cv.destroyAllWindows()                                     # 关闭所有窗口