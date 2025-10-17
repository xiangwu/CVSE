import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                                  # 读取图像文件
# 标准差sigma= 5、15、25
blur_img = cv.GaussianBlur(src, (0, 0), 5)          # (0, 0)：内核大小（自动根据sigma计算）
# 非锐化掩模（通过原图(src)与高斯模糊图(blur_img)的加权差实现边缘增强）
usm = cv.addWeighted(src, 1.5, blur_img, -0.5, 0)  # 1.5和-0.5的权重组合是经典的非锐化掩模参数，最终gamma值设为0保持亮度中性

cv.imshow('input',src)                                  # 显示原图
cv.imshow('gussian',blur_img)                           # 显示高斯模糊后的图像
cv.imshow('output',usm)                                 # 显示锐化增强后的图像


cv.waitKey(0)                                                    # 等待按键
cv.destroyAllWindows()                                           # 关闭所有窗口
