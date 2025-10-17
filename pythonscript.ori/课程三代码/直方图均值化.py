import cv2 as cv
import numpy as np

# 定义一个函数，用于计算并显示灰度图像的直方图
def custom_hist_cv(gray, window_name):
    # 计算直方图
    # [gray]：输入的单通道灰度图像 [0]：指定计算第0个通道（灰度图只有1个通道） None：不使用掩模图像 [256]：直方图bin的数量 [0,256]：像素值范围为0到255
    hist = cv.calcHist([gray], [0], None, [256], [0, 256])
    # 归一化直方图数据,采用最小 - 最大值归一化（cv.NORM_MINMAX)  将直方图值线性映射到[0,255]区间（alpha=0, beta=255）  cv.CV_8UC1，8位无符号整型单通道
    hist = cv.normalize(hist, hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
    # 创建一个256行×512列的三通道黑色背景图像用于绘制直方图
    hist_img = np.zeros((256, 512, 3), dtype=np.uint8)
    # 设置线条颜色（BGR
    color = (255, 0, 0)                                   # 蓝色
    # 绘制直方图
    for i in range(256):                                  # 遍历0-255的灰度级
        intensity = int(hist[i][0])                       # 表示直方图中第i个bin的统计值（如像素频数),强制转换为整数，确保后续计算精度一致（hist[i][0]：获取第i个bin的像素数量）
        cv.line(hist_img, (i, 256), (i, 256 - intensity), color) # 在图像的第i列绘制垂直线,起点坐标：(i, 256)（图像底部）,终点坐标：(i, 256 - intensity)（高度由频数决定，根据频数向上延伸）
        cv.imshow(window_name, hist_img)                  # 显示直方图图像
    return hist_img

src = cv.imread(PictureAddress)                           # 读取图像文件
if src is None:
    print("Error: Image not found or path is incorrect.")
    exit()

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                # 将图像从BGR颜色空间转换为灰度颜色空间
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)      # 创建可自动调整大小的窗口，cv.namedWindow("名称", " 模式")
cv.imshow("input", gray)                         # 显示图像

# 使用直方图均衡化增强图像的对比度
dst = cv.equalizeHist(gray)                               # （）里的输入必须是8位单通道灰度图像
# 显示直方图均衡化后的图像
cv.namedWindow("eh", cv.WINDOW_AUTOSIZE)
cv.imshow("eh", dst)

# 调用自定义函数，显示原始灰度图像的直方图
srb = custom_hist_cv(gray, "Histogram of Original Image")
# 调用自定义函数，显示直方图均衡化后的图像的直方图
srd = custom_hist_cv(dst, "Histogram of Equalized Image")

cv.waitKey(0)                                             # 等待按键
cv.destroyAllWindows()                                    # 关闭所有窗口
