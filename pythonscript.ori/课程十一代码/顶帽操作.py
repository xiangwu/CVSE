import cv2 as cv
import numpy as np


img = cv.imread(PictureAddress)                            # 读取图像文件
kernel = np.ones((7,7),np.uint8)                     # 创建7x7矩形结构元素
# 顶帽运算用于提取图像中比结构元素小的明亮区域或突出局部高对比度特征
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)     # 执行顶帽运算（原始图像 - 开运算结果）

# 显示
cv.imshow('output',tophat)

cv.waitKey(0)                                              # 等待按键
cv.destroyAllWindows()                                     # 关闭所有窗口

