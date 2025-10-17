import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src1 = cv.imread(Picture1Address)                               # 读取图像1
src2 = cv.imread(Picture2Address)                               # 读取图像2
#src3 = cv.imread("D:/images/flower.png")
#src4 = cv.imread("D:/images/test.jpg")

cv.namedWindow("input1", cv.WINDOW_AUTOSIZE)           # 创建可自动调整大小的窗口
cv.namedWindow("input2", cv.WINDOW_AUTOSIZE)
cv.imshow("input1", src1)                              # 显示图像1
cv.imshow("input2", src2)                              # 显示图像2
#cv.imshow("input3", src3)
#cv.imshow("input4", src4)

hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)                      # BGR转换为HSV
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
#hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)
#hsv4 = cv.cvtColor(src4, cv.COLOR_BGR2HSV)

# 计算HSV色彩空间的2D直方图  [hsv1]：输入图像列表（单幅HSV图像） [0,1]：计算通道0(H)和1(S)的联合直方图 None：不使用掩模 [60,64]：H维度60个bin，S维度64个bin [0,180,0,256]：H值范围0-180，S值范围0-256
hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
#hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])
#hist4 = cv.calcHist([hsv4], [0, 1], None, [60, 64], [0, 180, 0, 256])
print(hist1.dtype)                                              # hist1.dtype通常会输出float32或float64，因为calcHist()函数返回的直方图数据默认是浮点型数组
# 归一化
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX, dtype=cv.CV_32F)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
#cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)
#cv.normalize(hist4, hist4, 0, 1.0, cv.NORM_MINMAX)

match1= cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)          # 计算相关性（值域[-1,1]，1表示完全匹配
match2= cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)          # 卡方检验（值域[0,∞)，0表示完全匹配）
match3= cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)   # 巴氏距离（值域[0,1]，0表示完全匹配）
match4= cv.compareHist(hist1, hist2, cv.HISTCMP_INTERSECT)       # 直方图交集（值域[0,∞)，值越大相似度越高）
print("相似性: %s，卡方: %s，巴氏距离: %s，交集: %s"%(match1, match2, match3, match4))


# 补充
#methods = [cv.HISTCMP_CORREL, cv.HISTCMP_CHISQR,cv.HISTCMP_INTERSECT, cv.HISTCMP_BHATTACHARYYA]
#str_method = ""
#for method in methods:
    #src1_src2 = cv.compareHist(hist1, hist2, method)             # 对每对直方图(hist1/hist2和hist3/hist4)分别计算相似度
    #src3_src4 = cv.compareHist(hist3, hist4, method)
    #if method == cv.HISTCMP_CORREL:                              # 根据方法类型动态生成可读性结果描述
    #   str_method = "Correlation"
    #if method == cv.HISTCMP_CHISQR:
    #    str_method = "Chi-square"
    #if method == cv.HISTCMP_INTERSECT:
    #    str_method = "Intersection"
    #if method == cv.HISTCMP_BHATTACHARYYA:
    #    str_method = "Bhattacharyya"
    #print("%s src1_src2 = %.2f, src3_src4 = %.2f"%(str_method, src1_src2, src3_src4))  # 数值保留2位小数

cv.waitKey(0)                                                     # 等待按键
cv.destroyAllWindows()                                            # 关闭所有窗口
