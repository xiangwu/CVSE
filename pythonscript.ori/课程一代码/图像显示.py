import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)                        # 读取图像文件，例："D:/images/nezha.png"
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)   # 创建可自动调整大小的窗口，cv.namedWindow("名称", " 模式")
cv.imshow("input", src)                       # 显示图像

# 生成512x512像素的白色图像模板，使用uint8数据类型确保像素值范围0-255，3通道结构对应BGR色彩空间
m5 = np.ones(shape=[512,512,3], dtype=np.uint8)
m5[:,:,0] = 255                                        # 所有行(:)和列(:)，第0通道（BGR色彩空间中的蓝色通道）设为255
cv.imshow("m5", m5)                           # 显示纯蓝色图像窗口

cv.waitKey(0)                                          # 等待按键，"0" 无止境等待下一个按键
cv.destroyAllWindows()                                 # 关闭所有窗口
