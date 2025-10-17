import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)                        # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)   # 创建可自动调整大小的窗口
cv.imshow("input", src)                       # 显示图像


# t1 = 100, t2 = 3*t1 = 300  低阈值（t1），强度梯度低于此值被抑制，高阈值（t2=3*t1），梯度高于此值判定为强边缘
edges= cv.Canny(src, 100, 300)                         # 先用Canny算法检测图像边缘（输出二值图）
edge_src = cv.bitwise_and(src, src, mask=edges)        # 通过bitwise_and将原图与边缘掩膜结合,最终效果：仅保留原图中边缘对应的像素区域，双src输入表示对同一图像做自操作
h, w = src.shape[:2]                                   # h, w：获取原图高度/宽度
result = np.zeros([h, w*2,3], dtype=src.dtype)   # result：创建3通道黑色画布（宽度为原图2倍，用于并排显示）
result[0:h,0:w,:] = src                                # 左半区（0:w）填充原图
result[0:h,w:2*w,:] = edge_src                         # 右半区（w:2*w）填充边缘融合结果
# 文本标注：(10, 30)表示从图像左上角向右10像素、向下30像素的位置开始绘制
cv.putText(result, "original", (10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)   # 在图像左上角(10,30)位置添加红色文字"original"
cv.putText(result, "edge_src", (w+10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2) # 在图像右侧(w+10,30)位置添加红色文字"edge_src"（w变量应表示第一张图像的宽度，确保标注出现在拼接图像的右侧区域）

cv.imshow('output',result)                    # 显示结果图像

cv.waitKey(0)                                          # 等待按键
cv.destroyAllWindows()                                 # 关闭所有窗口

























