#from typing import get_origi
import cv2 as cv

src = cv.imread(PictureAddress)                       # 读取图像，例："D:/images/nezha.png"
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)  # 创建可自动调整大小的窗口
cv.imshow("input", src)                      # 显示图像
h, w, ch = src.shape
print("h: %s , w: %s , ch: %s "%(h, w, ch))           # 打印高度(h)、宽度(w)和通道数(ch)的变量值

# 遍历图像中的所有像素并获取它们的BGR值
for row in range(h):                                  # 外层循环，遍历图像的高度方向（垂直方向）
   for col in range(w):                               # 内层循环，遍历图像的宽度方向（水平方向）
     b, g, r = src[row, col]                          # 获取当前像素点的BGR三通道值，src：图像矩阵，row, col：当前像素坐标
     print(b,g,r)                                     # 打印当前像素的BGR分量值
cv.imshow("output", src)                     # 在"output"的窗口中显示图像

# 打印高度(h)、宽度(w)和通道数(ch)的变量值的补充
#h=src.shape[0]                                       # 返回图像矩阵的第一维度大小，获取图像高度（行数）
#w=src.shape[1]                                       # 返回图像矩阵的第二维度大小，获取图像宽度（列数）
#ch=src.shape[2]                                      # 返回图像矩阵的第三维度大小（仅彩色图像存在），获取图像通道数
#print("h: %s , w: %s , ch: %s "%(h, w, ch))

cv.waitKey(0)                                         # 等待按键，"0" 无止境等待下一个按键
cv.destroyAllWindows()                                # 关闭所有窗口