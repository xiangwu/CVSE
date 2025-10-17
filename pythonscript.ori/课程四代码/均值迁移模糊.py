import cv2 as cv
import numpy as np


# 均值迁移模糊，实现边缘保留的平滑效果，常用于去除噪声同时保持边缘清晰
# 对比双边滤波，均值迁移滤波通过迭代收敛更适用于复杂色彩分布的场景，但计算量较大，双边滤波则直接基于空间和色彩权重计算，实时性更好
src = cv.imread(PictureAddress)                 # 读取图像文件
cv.imshow('input',src)                 # 显示输入图像
# 均值漂移滤波（Mean Shift Filtering），主要用于图像分割和边缘保留平滑处理   参数15表示空间窗口半径，30表示颜色窗口半径   终止条件设置为最大迭代5次或误差小于1
dst = cv.pyrMeanShiftFiltering(src, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))
cv.imshow('output',dst)                # 显示输出图像


cv.waitKey(0)                                   # 等待按键
cv.destroyAllWindows()                          # 关闭所有窗口

