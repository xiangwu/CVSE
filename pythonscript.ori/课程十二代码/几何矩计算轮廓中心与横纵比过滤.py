import cv2 as cv
import numpy as np


# 二值图像 → 轮廓提取 → 几何分析 → 特征计算 → 分类标注
#               │              ├→ 宽高比 → 形状分类
#               │               └→ 质心坐标 → 精确定位
#               └→ 旋转矩形 → 顶点坐标 → 可视化

# 边缘检测
def canny_demo(image):                                      # 定义一个名为canny_demo的函数
    t = 80                                                  # 设置Canny边缘检测的低阈值为80
    canny_output = cv.Canny(image, t, t * 2)                # 高阈值t * 2为160
    cv.imshow("canny_output", canny_output)        # 显示边缘检测结果
    #cv.imwrite("D:/canny_output.png", canny_output)        # 存储结果
    return canny_output                                     # 返回边缘检测后的二值图像（白色为边缘，黑色为背景）

src = cv.imread(PictureAddress)                             # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)        # 创建可自动调整大小的窗口
cv.imshow("input", src)                            # 显示图像
edge_binary = canny_demo(src)                               # 调用canny_demo函数
k = np.ones((3, 3), dtype=np.uint8)                   # 图像处理中用作卷积核
binary = cv.morphologyEx(edge_binary, cv.MORPH_DILATE, k)   # 膨胀操作

# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # 从二值图像中提取所有外部轮廓
for c in range(len(contours)):                              # 遍历所有检测到的轮廓
    rect = cv.minAreaRect(contours[c])                      # cv.minAreaRect()用于获取轮廓最小外接旋转矩形的函数
    cx, cy = rect[0]                                        # 矩形中心点坐标 (x,y)
    ww, hh = rect[1]                                        # 矩形尺寸 (width, height)‌注意‌：ww和hh不区分长宽，需后续比较确定
    ratio = np.minimum(ww, hh) / np.maximum(ww, hh)         # 计算宽高比（Aspect Ratio）的归一化值，接近1.0：正方形/圆形，接近0.0：细长形
    print(ratio)
    mm = cv.moments(contours[c])                            # 计算轮廓的24个几何矩
    m00 = mm['m00']                                         # 提取零阶空间矩矩(m00)作为轮廓面积
    m10,m01 = mm['m10'], mm['m01']                          # 提取一阶矩(m10,m01)用于质心计算
    #计算轮廓质心坐标
    cx = np.int32(m10 / m00)                                # 质心X坐标（像素整型）
    cy = np.int32(m01 / m00)                                # 质心Y坐标
    box = cv.boxPoints(rect)                                # 获取矩形四个顶点
    box = np.int32(box)                                     # 转换为整数坐标
    if ratio > 0.9:                                         # 接近正方形的形状
        cv.drawContours(src, [box], 0, (0, 0, 255), 2)                                       # 红色矩形框
        cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)        # 蓝色质心点
    if ratio < 0.5:                                         # 细长形状
        cv.drawContours(src, [box], 0, (255, 0, 255), 2)                                     # 品红矩形框
        cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (0, 0, 255), 2, 8, 0)        # 红色质心点

# 显示
cv.imshow("contours_analysis", src)
#cv.imwrite("D:/contours_analysis.png", src)

cv.waitKey(0)                                               # 等待按键
cv.destroyAllWindows()                                      # 关闭所有窗口


