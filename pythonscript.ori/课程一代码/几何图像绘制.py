import cv2 as cv
import numpy as np


image= cv.imread(PictureAddress)                                     # 读取图像文件，例："D:/images/nezha.png"

# 在输入图像上绘制蓝色矩形（BGR格式(255,0,0)表示蓝色），矩形左上角坐标(100,100)，右下角坐标(300,300)，线宽为2像素，使用8-connected线型（cv.LINE_8）绘制，0指坐标的小数位数
src = cv.rectangle(image, (100, 100), (300, 300), (255, 0, 0), 2, cv.LINE_8, 0)
# 在输入图像上绘制红色圆形（BGR格式(0,0,255)表示红色），圆心坐标为(256,256)，半径50像素，边框线宽2像素，使用8-connected线型抗锯齿绘制
srb = cv.circle(image, (256, 256), 50, (0, 0, 255), 2, cv.LINE_8, 0)
# 在输入图像上绘制绿色椭圆（BGR格式(0,255,0)表示绿色），椭圆中心坐标为(256,256)，旋转角度360度，起始角度0度，结束角度360度（完整椭圆），边框线宽2像素，使用8-connected线型抗锯齿绘制
srd = cv.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv.LINE_8, 0)

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                 # 创建可自动调整大小的窗口，cv.namedWindow("名称", " 模式")
cv.imshow("input", image)                                   # 显示图像

# 补充
#image=np.zeros((500,500,3),np.uint8)                                # 创建500x500黑色背景图像
#cv.line(image,(0,0),(500,500),(255,255,255),5)                      # 上绘制一条白色对角线
#cv.rectangle(image,(100,150),(400,400),(0,0,255),5,cv.LINE_8,0)     # 图像上绘制一个红色矩形
#cv.circle(image,(250,250),50,(0,255,0),3,cv.LINE_8,0)               # 绘制一个绿色圆形
#cv.ellipse(image,(250,250),(100,50),50,0,360,(255,0,0),4,cv.LINE_8,0) # 绘制一个蓝色椭圆
#cv.imshow("output",image)                                           # 显示图像

cv.waitKey(0)                                                        # 等待按键
cv.destroyAllWindows()                                               # 关闭所有窗口
