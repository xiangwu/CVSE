import cv2 as cv
import numpy as np


img = cv.imread(PictureAddress)                                             # 读取图像文件
kernel = np.ones((7,7),np.uint8)                                      # 创建7x7矩形结构元素
#黑帽操作是图像形态学处理中与顶帽操作相对应的技术，主要用于提取比结构元素小的暗区域或突出局部低对比度特征
blackhat  = cv.morphologyEx(img,cv.MORPH_BLACKHAT, kernel)                  # 执行黑帽操作（闭运算结果-原始图像）
# 显示
cv.imshow('output',blackhat)

cv.waitKey(0)                                                               # 等待按键
cv.destroyAllWindows()                                                      # 关闭所有窗口

