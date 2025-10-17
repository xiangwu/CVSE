import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread(PictureAddress, 0)            # 0 表示读取为灰度图像

# 对图像进行二维快速傅里叶变换（执行FFT及中心化）
f= np.fft.fft2(img)
fshift = np.fft.fftshift(f)                    # 执行频域中心化操作

# 设置低通滤波器的参数
D0 = 50                                        # 截止频率，可以根据需要调整
rows, cols = img.shape                         # 获取输入图像的尺寸
mask = np.zeros((rows, cols), np.uint8)  # 注意这里我们不再需要第三个维度（颜色通道）
crow, ccol = rows // 2, cols // 2              # 计算图像中心点坐标
for i in range(rows):                          # 通过双重循环遍历图像每个像素位置
    for j in range(cols):
        # 计算当前点到中心的距离
        d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)    # d = √[(i-crow)² + (j-ccol)²]
        # 应用低通滤波器 （圆形掩模）
        if d <= D0:                            # 截止条件
            mask[i, j] = 1

# 应用滤波器
fshift_filtered = fshift * mask                # 实现频域成分的选择性保留/滤除
# 逆傅里叶变换
f_ishift = np.fft.ifftshift(fshift_filtered)   # 逆中心移位 (ifftshift)
img_back = np.fft.ifft2(f_ishift)              # 逆傅里叶变换
img_back = np.abs(img_back)                    # ‌取模运算，提取复数的幅度部分，获得最终可显示的真实图像数据

# 由于结果可能包含复数，我们只取幅度部分（归一化与类型转换）
# 数据归一化‌：将图像像素值线性映射到0-255范围，公式：(当前值 - 最小值)/(最大值 - 最小值)*255，确保所有像素值分布在标准灰度范围内
img_back = (img_back - np.min(img_back)) / (np.max(img_back) - np.min(img_back)) * 255
img_back = np.uint8(img_back)                  # 将浮点型数据转换为8位无符号整型(np.uint8)

# 显示原图像和滤波后的图像
# 使用plt.subplot(121)和plt.subplot(122)创建1行2列的并排子图布局，左侧子图位置编号121，右侧122
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.xticks([]), plt.yticks([])                 # 隐藏坐标轴刻度
plt.subplot(122), plt.imshow(img_back, cmap='gray'), plt.title('Lowpass Filtered Image')
plt.xticks([]), plt.yticks([])                 # 隐藏坐标轴刻度
plt.show()