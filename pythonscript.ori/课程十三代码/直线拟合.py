import cv2 as cv
import numpy as np


def canny_demo(image):                                        # 定义一个名为canny_demo的函数
    t = 80                                                    # 设置Canny边缘检测的低阈值为80
    canny_output = cv.Canny(image, t, t * 2)                  # 高阈值t * 2为160
    cv.imshow("canny_output", canny_output)          # 显示边缘检测结果
    #cv.imwrite("D:/canny_output.png", canny_output)          # 存储结果
    return canny_output                                       # 返回边缘检测后的二值图像（白色为边缘，黑色为背景）

src = cv.imread(PictureAddress)                               # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)          # 创建可自动调整大小的窗口
cv.imshow("input", src)                              # 显示图像
edge_binary = canny_demo(src)                                 # 调用canny_demo函数
k = np.ones((3, 3), dtype=np.uint8)                     # 图像处理中用作卷积核
binary = cv.morphologyEx(edge_binary, cv.MORPH_DILATE, k)     # 膨胀操作
cv.imshow("binary", binary)                          # 显示二值化图像
# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)     # cv.RETR_EXTERNAL提取所有外部轮廓

# 直线拟合
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])                 # 获取轮廓最小外接矩形参数，左上角坐标(x,y)和宽高(w,h) ，坐标系：x向右递增，y向下递增（OpenCV标准）
    m = max(w, h)                                             # 取矩形最大边长作为特征尺寸
    if m < 30:                                                # 尺寸阈值过滤，30px对应典型图像中5mm物体（600DPI下）
        continue                                              # 跳过噪声轮廓
# cv.fitLine()：对轮廓点集进行直线拟合，返回 直线方向向量(vx,vy) 和 经过点(x0,y0)，cv.DIST_L1,距离类型（L1范数更抗噪声）， 0,径向距离参数（0表示自动）， 0.01, 0.01 拟合精度参数
    vx, vy, x0, y0 = cv.fitLine(contours[c], cv.DIST_L1, 0, 0.01, 0.01)
    #计算斜截式方程
    k = vy/vx                                                 #（斜率）
    b = y0 - k*x0                                             #（截距）
    #初始化极值点坐标（用于后续线段端点计算）
    maxx = 0
    maxy = 0
    miny = 10000
    minx = 0

# 显示
cv.imshow("contours_analysis", src)

cv.waitKey(0)                                                # 等待按键
cv.destroyAllWindows()                                       # 关闭所有窗口
