import cv2 as cv

src = cv.imread(PictureAddress)                       # 读取图像文件
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)    # 创建可自动调整大小的窗口
cv.imshow("rgb", src)                        # 显示图像
# BGR to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to YUV
yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow("yuv", yuv)

# BGR to YUV
ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
cv.imshow("ycrcb", ycrcb)
#output = src
#cv.imshow('output',output)

# 补充BGR转灰度图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)


cv.waitKey(0)                                          # 等待按键
cv.destroyAllWindows()                                 # 关闭所有窗口

