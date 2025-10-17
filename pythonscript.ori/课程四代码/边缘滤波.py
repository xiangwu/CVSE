import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                           # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)      # 创建可自动调整大小的窗口
cv.imshow("input", src)                          # 显示图像

h, w = src.shape[:2]                                      # 获取图像宽高
#cv.edgePreservingFilter()是用于实现边缘保留滤波的核心函数，主要用于图像平滑处理时保护边缘结构不被模糊
dst = cv.edgePreservingFilter(src, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)  # sigma_s控制空间域平滑，sigma_r控制颜色域平滑，采用递归滤波方式(flags=cv.RECURS_FILTER)
result = np.zeros([h, w*2, 3], dtype=src.dtype)     # 创建左右并排的对比画布
result[0:h,0:w,:] = src                                   # 左侧显示原图
result[0:h,w:2*w,:] = dst                                 # 右侧显示处理结果


cv.imshow("result", result)                       # 显示处理后的图像结果
cv.imwrite("D:/images/result.png", result)        # 将结果图像保存到指定路径

cv.waitKey(0)                                              # 等待按键
cv.destroyAllWindows()                                     # 关闭所有窗口