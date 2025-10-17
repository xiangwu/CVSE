import cv2 as cv
import numpy as np


src=cv.imread(PictureAddress)                                  # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)           # 创建可自动调整大小的窗口
cv.imshow("input", src)                               # 显示图像

def canny_demo(image):                                         # 定义一个名为canny_demo的函数
    t = 80                                                     # 设置Canny边缘检测的低阈值为80
    canny_output = cv.Canny(image, t, t * 2)                   # 高阈值t * 2为160
    #cv.imshow("canny_output", canny_output)                   # 显示边缘检测结果
    #cv.imwrite("D:/canny_output.png", canny_output)           # 存储结果
    return canny_output                                        # 返回边缘检测后的二值图像（白色为边缘，黑色为背景）

edge_binary = canny_demo(src)                                  # 调用canny_demo函数
cv.imshow("binary", edge_binary)                      # 显示二值边缘图像

#霍夫直线检测
# 1：距离分辨率（像素单位）;np.pi/180：角度分辨率（1°的弧度值）;250：累加器阈值（值越高检测到的直线越显著）；None,可选输出参数（通常忽略）；0,最小线长度（0表示无限制）；0最大线间距（0表示无限制）
lines = cv.HoughLines(edge_binary, 1, np.pi / 180, 250, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        # lines[i]定位到第i条直线（形状1×2的数组）;[0][1] 索引表示取该直线第二个参数theta（θ）
        rho = lines[i][0][0]                                   # 极坐标中的ρ值（直线到原点的垂直距离）
        theta = lines[i][0][1]                                 # 极坐标中的θ值（直线旋转角度，弧度制）
        a = np.cos(theta)                                      # 计算直线法向量的x分量
        b = np.sin(theta)                                      # 计算直线法向量的y分量
        # 通过极坐标参数(ρ,θ)计算直线在图像边界上的两个端点
        x0 = a * rho                                           # (x0, y0) 表示直线垂足点的坐标
        y0 = b * rho
        # 直线端点计算                                           # 1000是任意大的缩放系数，确保直线足够长以跨越整个图像
        x1 = int(x0 + 1000 * (-b))                             # 端点1的x坐标（沿直线方向延伸1000像素），(-b) 即 -sinθ 表示x方向增量
        y1 = int(y0 + 1000 * a)                                # 端点1的y坐标，a即 cosθ 表示y方向增量
        x2 = int(x0 - 1000 * (-b))                             # 端点2的x坐标（反向延伸）
        y2 = int(y0 - 1000 * a)                                # 端点2的y坐标
        cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)   # 直接在原图上绘制红色线条
        # 补充（下面三行是对上面的总结）
        #pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        #pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        #cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

# 显示
cv.imshow("hough line demo", src)
#cv.imwrite("D:/contours_analysis.png", src)

cv.waitKey(0)                                                   # 等待按键
cv.destroyAllWindows()                                          # 关闭所有窗口




