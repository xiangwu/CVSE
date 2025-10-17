import cv2 as cv
import numpy as np

image= cv.imread(PictureAddress)                  # 读取图像文件
src= cv.cvtColor(image,cv.COLOR_BGR2GRAY)         # BGR转换为灰度图像
# 使用Sobel算子计算图像的水平和垂直梯度
h, w = src.shape[:2]                              # 获取图像高宽
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)    #（1，0）计算水平方向（x轴）梯度（检测垂直边缘）
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)    #（0, 1‌）计算垂直方向（y轴）梯度（检测水平边缘）

# 可视化梯度（将Sobel梯度计算结果(x_grad/y_grad)转换为8位无符号整型（unit.8））
x_grad = cv.convertScaleAbs(x_grad)               # convertScaleAbs()自动完成绝对值转换和数值缩放
y_grad = cv.convertScaleAbs(y_grad)
cv.imshow("x_grad", x_grad)              # 显示水平方向梯度图像
cv.imshow("y_grad", y_grad)              # 显示垂直方向梯度图像

# 梯度幅值合成（cv.add）
dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)     # 将水平梯度x_grad和垂直梯度y_grad按元素相加，生成综合梯度幅值矩阵, 指定输出为16位有符号整数

# 绝对值转换（cv.convertScaleAbs）
dst = cv.convertScaleAbs(dst)                     # 将合成梯度转换为8位无符号整型（uint8）
cv.imshow('output',dst)                  # 显示梯度合成图像

cv.waitKey(0)                                     # 等待按键
cv.destroyAllWindows()                            # 关闭所有窗口
