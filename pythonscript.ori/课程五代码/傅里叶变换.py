import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import magnitude_spectrum


img = cv.imread(PictureAddress)                                    # -1参数表示按原样加载图像（包括Alpha通道）
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                     # BGR转化为灰度图像
# 对灰度图像的离散傅里叶变换（DFT）
# np.float32(img_gray)将灰度图像转换为32位浮点格式，这是OpenCV傅里叶变换的必要输入数据类型
dft = cv.dft(np.float32(img_gray),flags = cv.DFT_COMPLEX_OUTPUT)   # 单通道灰度图作为输入时，输出复数结果需显式指定DFT_COMPLEX_OUTPUT标志
# 执行频域中心化操作,图像频域处理
dftShift = np.fft.fftshift(dft)                                    # dft必须是通过cv2.dft()得到的复数矩阵（双通道数组）
# 执行频域数据的逆中心化操作
ishift = np.fft.ifftshift(dftShift)
# cv2.idft()执行逆傅里叶变换，将经过np.fft.fftshift()中心化处理的频域数据ishift还原为空间域图像
iImage = cv.idft(ishift)
# 计算复数矩阵幅度,应用于频域图像处理后的结果转换，与cv2.dft()和np.fft.fftshift()配合实现完整的频域处理流程
iImg = cv.magnitude(iImage[:,:,0],iImage[:,:,1])  # iImage[:,:,0]为实部（Re），iImage[:,:,1]为虚部（Im）
# 使用plt.subplot(121)和plt.subplot(122)创建1行2列的并排子图布局，左侧子图位置编号121，右侧122
plt.subplot(121),plt.imshow(img,cmap = "gray"),plt.title("original"),plt.axis('off') # plt.axis('off')隐藏坐标轴，plt.title()为每幅图添加说明性标题
plt.subplot(122),plt.imshow(iImg,cmap = "gray"),plt.title("inverse"),plt.axis('off')
plt.show()

cv.imshow("inverse",iImg)                                 # 显示iImg
cv.waitKey(0)                                                      # 等待按键
cv.destroyAllWindows()                                             # 关闭所有窗口
