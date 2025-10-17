import cv2 as cv
from numpy.ma.extras import dstack

img = cv.imread(PictureAddress)               # 读取图像文件
# cv.medianBlur是中值滤波函数，用于图像去噪       5：滤波核的尺寸（必须是大于1的奇数）
median = cv.medianBlur(img, 5)          # 中值滤波,用窗口内像素值的中位数替代中心像素值，有效消除孤立噪声点
dst=median                                    # 相比均值滤波（cv2.blur），能更好保留边缘且对椒盐噪声效果显著
cv.imshow("input",img)               # 计算耗时约为均值滤波的5倍,大核尺寸（如7×7）会显著增加处理时间
cv.imshow('output',dst)


# 补充
#def median_blur_demo(image):                 # 定义一个中值滤波的函数
    #dst=cv.medianBlur(image,5)
    #cv.imshow('output',dst)
#image= cv.imread("D:/images/nezha.png")
#cv.imshow("input",img)
#median_blur_demo(image)


cv.waitKey(0)                                # 等待按键
cv.destroyAllWindows()                       # 关闭所有窗口
