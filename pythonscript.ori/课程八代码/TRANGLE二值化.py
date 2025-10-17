import cv2 as cv
import numpy as np

src = cv.imread(PictureAddress)                           # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)      # 创建可自动调整大小的窗口
cv.imshow("input", src)                          # 显示图像

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)                # BGR格式的源图像src转换为灰度图像
# TRIANGLE阈值分割，TRIANGLE算法通过寻找灰度直方图的"三角形顶点"来确定阈值,特别适用于单峰直方图图像(如文档扫描件)，相比OTSU算法，在背景和前景比例悬殊时表现更好
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
print("ret :", ret)                                       # 打印三角法计算得到的实际阈值数值
result = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)           # 将二值图转回BGR格式
# 显示自动计算的阈值
# result：目标图像（BGR格式），f"TRIANGLE Threshold: {ret}"：动态生成的文本内容（含阈值数值），(10, 30)：文本左下角起始坐标（x,y），cv.FONT_HERSHEY_SIMPLEX：标准无衬线字体
cv.putText(result, f"TRIANGLE Threshold: {ret}", (10, 30),
          cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)   # 0.8：字体缩放比例，(0, 0, 255)：红色文本（BGR格式）2：文本线宽（像素）

cv.imshow('output',result)                       # 显示结果图像

cv.waitKey(0)                                             # 等待按键
cv.destroyAllWindows()                                    # 关闭所有窗口

