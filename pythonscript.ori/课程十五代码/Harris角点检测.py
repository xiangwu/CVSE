import numpy as np
import cv2 as cv


def process(image, opt=1):                                     # opt: 处理选项(默认1)1: 灰度化 2: 边缘检测 3: 高斯模糊4: 直方图均衡化
    # Detector parameters（检测器参数）
    blockSize = 2                                              # blockSize（系统块儿大小）=2：角点检测的邻域窗口大小（2×2像素区域）；值越小，检测到的角点越精细但可能噪声更多
    # 在OpenCV中apertureSize通常在Canny()或Sobel()函数中使用
    apertureSize = 3                                           # apertureSize指定Sobel算子内核大小，必须是奇数（如3/5/7）（‌值=3时‌：表示使用3×3的Sobel核计算图像梯度），必须是奇数，增大该值可增强抗噪性但会模糊边缘
    k = 0.04                                                   # Harris响应函数中的经验常数，推荐范围0.04~0.06，值越小检测到的角点越多
    # Detecting corners（检测角点）
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)               # 转换为灰度图
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)    # 调用cv2.cornerHarris()计算角点响应
    # Normalizing
    dst_norm = np.empty(dst.shape, dtype=np.float32)           # 创建一个与输入矩阵dst形状相同的空矩阵，数据类型为np.float32，用于存储归一化后的结果
    # 对Harris响应矩阵dst进行最小 - 最大归一化，结果存储在dst_norm中
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst_norm_scaled = cv.convertScaleAbs(dst_norm)             # 用于数据格式转换的关键操作，主要用于将归一化后的Harris角点响应矩阵转换为8位无符号整型格式
    # Drawing a circle around corners（在拐角处画一个圆）
    for i in range(dst_norm.shape[0]):                         # 遍历矩阵的行（高度方向）
        for j in range(dst_norm.shape[1]):                     # 遍历矩阵的列（宽度方向）
            if int(dst_norm[i, j]) > 80:                       # 将浮点响应值转换为整数进行比较
                # 为检测到的特征点分配随机颜色（生成3个0-256之间的随机整数，别对应BGR颜色空间的蓝色、绿色和红色通道）
                b = np.random.randint(0, 256)        # random_integers()在numpy 1.11中已弃用，建议改用：np.random.randint(0, 256)
                g = np.random.randint(0, 256)        # randint是random+integer拼接简写而成
                r = np.random.randint(0, 256)
                # 绘制圆形：使用之前生成的随机BGR颜色(b,g,r)，这里注意OpenCV的xy坐标顺序，要进行坐标转换
                cv.circle(image, (j, i), 5, (int(b), int(g), int(r)), 2)
    return image

src = cv.imread(PictureAddress)                                 # 读取源图像
cv.imshow("input", src)                                # 显示源图像
result = process(src)                                           # 调用定义的process（函数）
cv.imshow('result', result)                            # 显示结果图像

cv.waitKey(0)                                                   # 等待按键
cv.destroyAllWindows()                                          # 关闭所有窗口

