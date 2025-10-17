import cv2 as cv


src = cv.imread(PictureAddress)                                                             # 读取图像文件
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)                                                   # 转化为灰度图
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)   # 二值化
# kernel用于定义形态学操作（如腐蚀、膨胀等）中像素邻域的几何形状和大小
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))                              # cv.MORPH_RECT：指定结构元素形状为矩形
# cv.erode()函数对二值图像进行腐蚀操作，属于形态学图像处理的基本操作
# 腐蚀操作原理：将kernel锚点滑过图像每个像素，只有当kernel覆盖区域全为前景时，锚点位置才保留前景值，否则置为背景值。
dst = cv.erode(binary, kernel)                                                             # binary：输入的二值图像（通常为黑白图像，前景为白色255，背景为黑色0
# 显示
cv.imshow('output',dst)

cv.waitKey(0)                                                                              # 等待按键
cv.destroyAllWindows()                                                                     # 关闭所有窗口




