import cv2 as cv
import numpy as np


src = cv.imread(PictureAddress)                          # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)     # 创建可自动调整大小的窗口
cv.imshow("input", src)                         # 显示图像

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)               # BGR格式的源图像src转换为灰度图像
# 自动阈值分割 OTSU  （适用于前景和背景对比度不明显的图像），cv.threshold() 是OpenCV中的阈值处理函数
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)   # ret：自动计算的最佳阈值，binary：二值化结果图像（黑白两色），参数0和255表示二值化后的像素取值范围
print("ret:", ret)                                       # 输出OTSU算法计算得到的具体阈值数值
cv.imshow("binary", binary)                     # 创建名为"binary"的窗口显示二值化结果图像


# 补充
# result：目标图像（BGR格式），f"OTSU Threshold: {ret}"：动态生成的文本内容（含阈值数值），(10, 30)：文本左下角起始坐标（x,y），cv.FONT_HERSHEY_SIMPLEX：标准无衬线字体
#result = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
#cv.putText(result, f"OTSU Threshold: {ret}", (10, 30),
#          cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)   # 0.8：字体缩放比例，(0, 0, 255)：红色文本（BGR格式）2：文本线宽（像素）
#cv.imshow('output',result)

cv.waitKey(0)                                             # 等待键盘输入
cv.destroyAllWindows()                                    # 关闭所有窗口
