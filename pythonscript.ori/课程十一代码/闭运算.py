import cv2 as cv
import numpy as np

img = cv.imread(PictureAddress)                           # 读取图像文件
# 创建5x5矩形结构元素
kernel = np.ones((5,5),np.uint8)                    # 与cv.getStructuringElement(cv.MORPH_RECT, (5,5))生成的核效果相同
#闭运算原理：先膨胀填补孔洞/连接断裂，再腐蚀恢复物体大致形状，与开运算形成对偶操作，常用于后处理阶段改善分割结果
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)    # 执行闭运算
# 显示
cv.imshow('output',closing )

cv.waitKey(0)                                             # 等待按键
cv.destroyAllWindows()                                    # 关闭所有窗口

