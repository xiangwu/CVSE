import cv2 as cv
import numpy as np


img = cv.imread(PictureAddress)                       # 读取图像文件
kernel = np.ones((3,3),np.uint8)                # 使用NumPy创建了一个3×3的全1矩阵
# cv2.dilate()函数对输入图像进行膨胀操作
dige_dilate = cv.dilate(img,kernel,iterations = 1)    # img：输入图像（通常为二值图像） iterations=1：指定膨胀操作执行的次数

# 显示
cv.imshow('output',dige_dilate)

cv.waitKey(0)                                         # 等待按键
cv.destroyAllWindows()                                # 关闭所有窗口
