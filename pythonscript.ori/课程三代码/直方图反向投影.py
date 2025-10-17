import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt


def back_projection_demo():                                       # 定义直方图反向投影函数
    # 读取样本图像和目标图像
    sample = cv.imread(Picture1Address)                           # 读取图像文件1
    target = cv.imread(Picture2Address)                           # 读取图像文件2
    #转换为HSV色彩空间
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    # show images（显示原始图像）
    cv.namedWindow("sample", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("target", cv.WINDOW_AUTOSIZE)         # 创建可自动调整大小的窗口
    cv.imshow("sample", sample)                          # 显示样本图像
    cv.imshow("target", target)                          # 显示目标图像
    # 计算样本直方图（H-S通道）
    # [roi_hsv]表示输入的是单幅HSV格式图像        [0,1]指定同时计算H(色调)和S(饱和度)两个通道的联合直方图，忽略V(亮度)通道  None表示不对图像区域进行掩模处理，计算全图的直方图
    # [32,32]将H通道和S通道分别划分为32个bin，最终生成32x32的二维直方图矩阵   [0,180,0,256]指H通道和S通道的取值范围
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    # 归一化直方图（cv.NORM_MINMAX采用最小-最大值归一化方法）
    # roiHist同时作为输入和输出参数，表示直方图数据将被原地修改           0, 255指定将直方图值线性缩放至0-255区间
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    # 计算反向投影
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)

# 计算并可视化图像的二维直方图
def hist2d_demo(image):                                           # 定义hist2d_demo()函数
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)                    # 转换为HSV图像
    hist = cv.calcHist([hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    # plt.figure（）Matplotlib库中用于创建图形窗口的配置语句
    plt.figure(figsize=(10, 8), dpi=100)                          # figsize=(10,8)设置图形宽度为10英寸，高度为8英寸，控制最终输出的物理尺寸dpi=100 指定图像分辨率为100像素/英寸
    # 可视化
    # 用Matplotlib的imshow()函数显示二维直方图数据
    plt.imshow(hist, interpolation='nearest')
    # 补充
    #plt.title("2D Histogram")                                    # 添加标题
    #plt.colorbar()                                               # 添加色阶条
    #plt.xlabel("Saturation")                                     # 设置X轴标签
    #plt.ylabel("Hue")                                            # 设置y轴标签
    plt.show()
    return hist

back_projection_demo()                                            # 调用back_projection_demo()函数
# 读取样本图像和目标图像
sample = cv.imread(Picture1Address)
target = cv.imread(Picture2Address)
hist2d_demo(sample)                                               # 调用hist2d_demo()函数
#hist2d_demo(target)

cv.waitKey(0)                                                     # 等待按键
cv.destroyAllWindows()                                            # 关闭所有窗口

