import cv2 as cv
import numpy as np


def connected_components_demo(src):
    # 预处理：高斯模糊和灰度转换
    src = cv.GaussianBlur(src, (3, 3), 0)      # 使用3×3核进行高斯平滑，消除高频噪声
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)              # 将BGR三通道图像转为单通道灰度图
    # 自动阈值二值化(使用OTSU算法)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # cv.connectedComponents()是用于二值图像连通域分析的函数
    output = cv.connectedComponents(binary, connectivity=8, ltype=cv.CV_32S)   # connectivity=8：使用8邻域连通规则，ltype=cv.CV_32S：输出标签矩阵类型为32位整型
    num_labels=output[0]                                    # output[0]：num_labels表示检测到的连通域总数（包含背景）
    labels = output[1]                                      # output[1]：labels是与输入同尺寸的标记矩阵矩阵，背景标记为0，其他区域从1开始编号
    colors = []                                             # 创建名为colors的空列表对象,准备存储RGB元组或其他颜色表示形式
    for i in range(num_labels):
        b = np.random.randint(0, 256)             # 生成随机RGB颜色（0-255范围）
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))                            # 将生成的RGB颜色值添加到颜色列表中
    colors[0] = (0, 0, 0)                                   # 索引0对应背景，强制设为黑色(0,0,0)
    h, w = gray.shape                                       # 获取图像尺寸
    image = np.zeros((h, w, 3), dtype=np.uint8)       # 创建一个全零的三维数组
    # 通过双重循环遍历每个像素位置(row,col)
    for row in range(h):
        for col in range(w):
            # 这段代码是图像处理中连通域标记结果的可视化核心语句，用于将分类标记矩阵转换为彩色图像。
            image[row, col] = colors[labels[row, col]]      # 使用labels矩阵中存储的连通域编号作为索引，从预定义的colors数组中取出对应颜色值赋给输出图像
    cv.imshow("colored labels", image)
    #cv.imwrite("D:/labels.png", image)
    print("total rice : ", num_labels - 1)

src = cv.imread(PictureAddress)                             # 读取图像文件
connected_components_demo(src)                              # 调用connected_components_demo()函数

cv.waitKey(0)                                               # 等待按键
cv.destroyAllWindows()                                      # 关闭所有窗口