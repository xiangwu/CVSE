import cv2 as cv
import numpy as np


image = cv.imread(PictureAddress)                      # 读取图像文件
cv.imshow('input',image)                      # 显示图像
#高斯模糊预处理（GaussianBlur函数对输入图像进行平滑处理）
src = cv.GaussianBlur(image, (0, 0), 1)   # (0,0)表示自动计算核尺寸，设置标准差σ=1控制模糊程度（σ值越大模糊效果越明显）
cv.imshow('gaussian',src)                     # 显示高斯模糊后的图像

#拉普拉斯边缘检测,对模糊后图像应用cv.Laplacian二阶微分算子
dst = cv.Laplacian(src, cv.CV_32F, ksize=3, delta=127) # 表示使用3×3的Sobel核对输入图像src进行二阶微分运算,指定输出32位浮点型数据（保留负梯度值）,delta=127将所有结果偏移127（便于可视化处理）

#图像数据转换
dst = cv.convertScaleAbs(dst)                          # 对输入数组执行线性变换并取绝对值后转换为8位无符号整型
cv.imshow('output',dst)                       # 显示图像

cv.waitKey(0)                                          # 等待按键
cv.destroyAllWindows()                                 # 关闭所有窗口

