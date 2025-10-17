import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 定义一个函数，用于计算并显示灰度图像的直方图
def custom_hist_cv(gray, window_name):                    # gray：输入的灰度图像，window_name：显示窗口名称
    # cv.calcHist（）计算直方图    [gray]：输入的灰度图像（单通道） [0]：指定计算第0个通道的直方图 None：不使用掩模 [256]：直方图的bin数量为256 [0, 256]：像素值范围为0到255
    hist = cv.calcHist([gray], [0], None, [256], [0, 256]) # 返回一个256x1的数组hist，每个元素表示对应灰度级的像素数量
    # 归一化直方图数据（两个hist表示原地修改直方图数据）         采用最小-最大值归一化（cv.NORM_MINMAX） 将直方图值线性映射到[0,255]区间（alpha=0, beta=255） cv.CV_8UC1，8位无符号整型单通道
    hist = cv.normalize(hist, hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
    # 创建一个空白的黑色图像用于绘制直方图
    hist_img = np.zeros((256, 512,3), np.uint8)
    # 设置线条颜色（BGR）
    color = (255, 0, 0)                                   # 蓝色
    # 绘制直方图(线条)
    for i in range(256):
      intensity = int(hist[i][0])                         # 表示直方图中第i个bin的统计值（如像素频数),强制转换为整数，确保后续计算精度一致（hist[i][0]：获取第i个bin的像素数量）
      # cv.line()函数用于在直方图可视化图像上绘制垂直线条       在图像的第i列绘制垂直线,起点坐标：(i, 256)（图像底部）,终点坐标：(i, 256 - intensity)（高度由频数决定，根据频数向上延伸）
      cv.line(hist_img, (i, 256), (i, 256 - intensity), color)    # 256-intensity实现垂直翻转（OpenCV坐标系原点在左上角，每个柱状图宽度为1像素（i作为x坐标）
      cv.imshow(window_name, hist_img)
    return hist_img                                       # 用于返回包含直方图可视化结果的图像矩阵

src = cv.imread(PictureAddress)                           # 读取图像
if src is None:
            print("Error: Image not found or path is incorrect.")
            exit()
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                # 将图像从BGR颜色空间转换为灰度颜色空间
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)      # 创建可自动调整大小的窗口
cv.imshow("input", gray)                         # 显示图像

srb = custom_hist_cv(gray, "Histogram of Orignal Image")    # 显示灰度图像的直方图

cv.waitKey(0)                                             # 等待按键
cv.destroyAllWindows()                                    # 关闭所有窗口
