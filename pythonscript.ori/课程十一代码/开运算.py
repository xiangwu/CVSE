import cv2 as cv
import numpy as np


img = cv.imread(PictureAddress)                                # 读取图像文件

kernel = np.ones((5,5),np.uint8)                         # 结构元素（如5×5全1矩阵），决定操作中邻域像素的影响范围
# 开运算原理：先腐蚀去除微小干扰，再膨胀恢复主要物体形状，能有效保持物体主要特征同时消除噪声
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)          # 指定开运算类型

# 显示
cv.imshow('output',opening)

cv.waitKey(0)                                                  # 等待按键
cv.destroyAllWindows()                                         # 关闭所有窗口
