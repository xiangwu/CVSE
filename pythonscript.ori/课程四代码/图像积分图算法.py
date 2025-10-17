import cv2 as cv
import numpy as np

# 积分图中矩形区域像素值的快速求和计算（核心原理是通过四个角点的积分图值进行加减运算，快速得到任意矩形区域的像素和）
def get_block_sum(ii, x1, y1, x2, y2, index):
    tl = ii[y1, x1][index]                               # (y1,x1)：矩形区域左上角坐标，y在前符合opencv行列约定
    tr = ii[y2, x1][index]
    bl = ii[y1, x2][index]
    br = ii[y2, x2][index]                               # (y2,x2)：矩形区域右下角坐标
    s = (br - bl - tr + tl)                              # 公式 s = br - bl - tr + tl 计算矩形区域和
    return s

# 基于积分图(ii)（Integral Image）的快速均值模糊
def blur_demo(image, ii):
    h, w, dims = image.shape                             # 获取图像的基本维度信息（高度、宽度和通道数）
    result = np.zeros(image.shape, image.dtype)          # 创建一个与输入图像尺寸和数据类型完全相同的全零矩阵，常用于图像处理中存储计算结果
    ksize = 15                                           # 设定卷积核大小为15x15像素
    radius = ksize // 2                                  # 计算核半径（整除运算得7）

    # 该循环配合内层的列循环(col)共同完成对整个图像的遍历，每个(row,col)位置对应一个处理中心点(cy,cx)
    for row in range(0, h + radius, 1):                  # 从0开始到图像高度h加上模糊半径radius，步长为1表示逐行处理
        # 边界条件判断，确保卷积窗口坐标不超出图像范围
        y2 = h if (row + 1)> h else (row + 1)            # 判断(row + 1)是否超出图像高度h，若超出则取h作为边界值，否则取(row + 1)
        y1 = 0 if (row - ksize) < 0 else (row - ksize)   # 判断(row - ksize)是否小于0（上边界），若越界则取0，否则取(row - ksize)，确保卷积核访问不会越出图像上边界
        for col in range(0, w + radius, 1):              # range(0, w + radius, 1)表示从0开始到图像宽度w加上模糊半径radius，步长为1实现逐列移动
            x2 = w if (col + 1)>w else (col + 1)         # 判断(col + 1)是否超出图像宽度w，若超出则取w作为右边界，否则取(col + 1)
            x1 = 0 if (col - ksize) < 0 else (col - ksize)# 判断(col - ksize)是否小于0（左边界），若越界则取0，否则取(col - ksize)
            # 通过边界检查确保卷积中心点不越界
            cx = 0 if (col - radius) < 0 else (col - radius)
            cy = 0 if (row - radius) < 0 else (row - radius)
            num = (x2 - x1)*(y2 - y1)                    # 通过(x2-x1)*(y2-y1)计算当前卷积窗口的实际像素面积，用于后续归一化处理（如均值模糊）
            #通过range(0,3,1)依次处理BGR三通道，每个通道独立进行卷积运算，通过get_block_sum获取每个通道的矩形区域像素和
            for i in range(0, 3, 1):
                s = get_block_sum(ii, x1, y1, x2, y2, i) # (x1,y1)-(x2,y2)：矩形区域坐标
                # 将区域和除以num（区域像素数）得到均值，(cy,cx)：结果存储位置
                result[cy, cx][i] = s // num             # s // num实现窗口内像素值的均值计算，计算结果写入result[cy, cx][i]对应通道

    cv.imshow("integral fast blur", result)      # 在窗口中显示经过积分图快速模糊处理的结果图像
    cv.imwrite("D:/images/result.png", result)   # 将处理结果保存到指定路径

src = cv.imread(PictureAddress)                           # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)      # 创建可自动调整大小的窗口
cv.imshow("input", src)                          # 显示图像

#使用OpenCV的integral()函数计算图像的积分图（和表）
sum_table = cv.integral(src, sdepth=cv.CV_32S)            # 其中src是输入图像，sdepth=cv.CV_32S指定输出积分图的数据类型为32位有符号整数
blur_demo(src, sum_table)                                 # 利用积分图实现快速区域模糊

cv.waitKey(0)                                             # 等待按键
cv.destroyAllWindows()                                    # 关闭所有窗口
