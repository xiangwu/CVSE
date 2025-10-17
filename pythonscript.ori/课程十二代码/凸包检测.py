import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)                                                            # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                                       # 创建可自动调整大小的窗口
cv.imshow("input", src)                                                           # 显示图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                                                 # 转换为灰度图
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # OTSU二值化
k = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))                                  # 创建3x3矩形核
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, k)                                         # 开运算（先腐蚀后膨胀）
# cv.imshow("binary", binary)

# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)    # 从二值图像中提取所有外部轮廓
for c in range(len(contours)):                                                             # 遍历所有检测到的轮廓
    # cv.isContourConvex()：基于Sklansky算法判断轮廓凸性
    ret = cv.isContourConvex(contours[c])                                                  # 检查轮廓是否为凸包，返回值：布尔值（True表示凸轮廓）
    # cv.convexHull()：基于Andrew's monotone chain算法
    points = cv.convexHull(contours[c])                                                    # Andrew's单调链算法计算轮廓的凸包
    total = len(points)
    # 获取凸包相邻顶点坐标（实现多边形边遍历）   [i]选择第i个顶点  [0]获取去掉单维后的坐标值
    for i in range(len(points)):
        x1, y1 = points[i%total][0]                                                        # points是形状为(N,1,2)的NumPy数组，存储轮廓顶点坐标，通过[0]操作提取去掉单维后的二维坐标
        x2, y2 = points[(i+1)%total][0]                                                    # 通过取模运算%total实现环形访问（首尾顶点自动连接），例：当i=last_index时，(i+1)%total=0
        cv.circle(src, (x1, y1), 4, (255, 0, 0), 2, 8, 0)         # 绘制蓝色顶点，顶点半径4px确保可视化清晰度
        cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)        # 绘制红色边线
    print(points)                                                                          # 输出凸包顶点坐标
    print("convex : ", ret)                                                                # 输出凸性检测结果

# 显示
cv.imshow("contours_analysis", src)
#cv.imwrite("D:/contours_analysis.png", src)

cv.waitKey(0)                                                                              # 等待按键
cv.destroyAllWindows()                                                                     # 关闭所有窗口

