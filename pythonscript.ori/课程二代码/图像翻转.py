import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                         # 读取图像
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)    # 创建可自动调整大小的窗口
cv.imshow("input", src)                        # 显示图像

# cv.flip(src, 0) 是OpenCV中的图像翻转函数，
# X Flip 倒影
dst1 = cv.flip(src, 0)                          # 0，垂直翻转，沿x轴
cv.imshow("x-flip", dst1)                      # 0：翻转模式代码（0=垂直，1=水平，-1=双向）

# Y Flip 镜像
dst2 = cv.flip(src, 1)                          # 1，水平翻转，沿y轴
cv.imshow("y-flip", dst2)

# XY Flip 对角
dst3 = cv.flip(src, -1)                                  # -1，对角翻转
cv.imshow("xy-flip", dst3)

cv.waitKey(0)                                            # 等待按键
cv.destroyAllWindows()                                   # 关闭所有窗口
