import cv2 as cv

img = cv.imread(PictureAddress)                 # 读取图像文件
# 均值滤波，该操作可有效抑制高斯噪声和随机噪声，但会导致边缘模糊，对椒盐噪声效果较差，此时建议改用中值滤波（cv2.medianBlur()），均值滤波时高频细节（如边缘）会被平滑，需权衡去噪与特征保留
blur = cv.blur(img, (3, 3))               # 核尺寸过大会导致过度模糊，建议根据噪声程度选择3×3或5×5
dst= blur
cv.imshow('output',dst)
cv.imshow("input", img)

# 补充
#def blur_demo(image):                          # 定义一个均值滤波函数
    #dst = cv.blur(image, (3, 3))
    #cv.imshow('blur',dst)
#src= cv.imread("D:/images/nezha.png")
#cv.imshow("input", src)
#blur_demo(src)

cv.waitKey(0)                                   # 等待按键
cv.destroyAllWindows()                          # 关闭所有窗口
