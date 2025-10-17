import cv2 as cv
import numpy as np


def laplacian_demo(pyramid_images):
    # 获取输入金字塔的层级数
    level = len(pyramid_images)                                      # len()函数会返回pyramid_images列表中的元素数量，即高斯金字塔或拉普拉斯金字塔的层级数
    # 从顶层向底层反向遍历
    for i in range(level-1, -1, -1):                                 # 生成从level-1到0（不包含-1）的递减序列，步长为-1
        if (i-1) < 0:                                                # 处理最底层特殊情况
            h, w = src.shape[:2]                                     # 获取原始图像尺寸
            # cv.pyrUp（）是高斯金字塔上采样操作，通过插值扩大图像尺寸，dstsize强制指定输出尺寸
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))     # 上采样到原图尺寸
            lpls = cv.subtract(src, expand) + 127                    # 计算与原始图像的差分（+127用于可视化偏移）
            cv.imshow("lpls_" + str(i), lpls)                        # 创建一个名为"lpls_i"的窗口（i为当前层级序号），显示拉普拉斯金字塔第i层图像（显示当前层特征）
        else:                                                        # 常规层级处理
            h, w = pyramid_images[i-1].shape[:2]                     # 获取下一层尺寸
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))     # 上采样到下层尺寸
            lpls = cv.subtract(pyramid_images[i-1], expand) + 127    # 计算层间差分
            cv.imshow("lpls_"+str(i), lpls)                          # 显示特征图

def pyramid_up(image, level=3):
    # temp = image.copy() 会创建输入图像的独立副本，防止后续操作污染原始图像数据
    temp = image.copy()                                               # 与直接赋值(temp = image)不同，.copy()确保新对象拥有独立的内存空间
    # cv.imshow("input", image)
    # pyramid_images = []是Python中初始化空列表的标准操作
    pyramid_images = []                                               # 创建空列表用于存储各层级金字塔图像
    for i in range(level):                                            # 循环控制：执行level次迭代，每次迭代生成一个更粗糙尺度的图像
        dst = cv.pyrDown(temp)                                        # 高斯模糊+降采样（图像宽高减半）
        pyramid_images.append(dst)                                    # 将当前层级结果存入列表，存储顺序：从原始尺度到最粗糙尺度
        #cv.imshow("pyramid_up_" + str(i), dst)
        temp = dst.copy()                                             # 更新处理源为当前层级图像的副本
    return pyramid_images                                             # 返回包含所有层级图像的列表，输出结构实例：[层级1图像, 层级2图像, 层级3图像]


src = cv.imread(PictureAddress)                                       # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                  # 创建可自动调整大小的窗口
cv.imshow("input", src)                                      # 显示图像

#pyramid_up(src)
laplacian_demo(pyramid_up(src))                                       # 调用laplacian_demo（）函数

cv.waitKey(0)                                                         # 等待按键
cv.destroyAllWindows()                                                # 关闭所有窗口

