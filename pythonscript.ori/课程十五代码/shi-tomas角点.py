import numpy as np
import cv2 as cv


def process(image, opt=1):                                       # opt: 处理选项(默认1)1: 灰度化 2: 边缘检测 3: 高斯模糊4: 直方图均衡化
    # Detecting corners（检测角点）
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)                 # 转换为灰度图
    # cv.goodFeaturesToTrack() 是一个用于检测图像中强角点（特征点）的函数 ;maxCorners,返回的最大角点数量,这里100用来限制检测到的最大角点数量
    # qualityLevel:角点质量等级阈值, 在Shi-Tomasi角点检测中，qualityLevel表示角点质量的最低阈值，取值范围通常为0.01~0.1
    corners = cv.goodFeaturesToTrack(gray, 100, 0.05, 10)              # 10：角点间最小像素距离（避免密集角点）
    print(len(corners))                                          # 输出检测到的角点总数，验证cv.goodFeaturesToTrack()的实际检测数量
    for pt in corners:
        print(pt)
        b =  200                                                 # b, g, r = 200, 200, 200设置绘制颜色为灰色（BGR格式）
        g =  200
        r =  200
       # 获取第一个角点的x和y坐标，pt[0][0]获取第一个维度的x坐标（浮点型），pt[0][1]获取第一个维度的y坐标（浮点型），np.int32()将浮点坐标强制转换为32位整型
        x = np.int32(pt[0][0])                                   # 优化:x, y = map(int, pt.ravel())  pt.ravel() 将嵌套数组结构 [[x, y]] 展平为 [x, y]，map(int, ...) 对两个坐标值同时执行整型转换
        y = np.int32(pt[0][1])
        # 标记角点位置                                             thickness:标记线条粗细（正值表示边框宽度，-1 表示实心填充）
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    return image


src = cv.imread(PictureAddress)                                  # 读取源图像
cv.imshow("input", src)                                 # 显示源图像
result = process(src)                                            # 调用定义的process（函数）
cv.imshow('result', result)                             # 显示结果图像

cv.waitKey(0)                                                    # 等待按键
cv.destroyAllWindows()                                           # 关闭所有窗口


