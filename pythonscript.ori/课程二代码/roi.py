import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)             # 读取图像
h, w = src.shape[:2]                        # 提取图像的二维尺寸信息（高度和宽度）

# 获取ROI（Region of Interest）
cy = h//2                                   #计算图像中心点坐标(cx, cy)
cx = w//2
# 纵向范围：中心向上260像素至向下50像素，中心左右各100像素，冒号表示保留所有颜色通道
roi = src[cy-260:cy+50,cx-100:cx+100,:]

# copy ROI
image = np.copy(roi)                        # 用NumPy创建图像ROI区域的独立副本，避免原图被修改。保持与原ROI相同的尺寸和数据类型

# modify ROI （直接在原数据上修改）
#roi[:, :, 0] = 0                           # 将ROI区域的蓝色通道置零，图像会呈现蓝绿色调缺失的效果

# modify copy roi
image[:, :, 2] = 0                          # 将拷贝图像的红色通道(R)置零，图像会呈现红色调缺失的效果

output = image
cv.imshow('output',output)         # 显示图像


cv.waitKey(0)                               # 等待按键
cv.destroyAllWindows()                      # 关闭所有窗口
