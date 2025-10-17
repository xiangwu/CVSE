import cv2 as cv
import numpy as np


src=cv.imread(Picture1Address)                              # 读取源图像（待搜索的大图）
tpl=cv.imread(Picture2Address)                              # 读取模板图像（待匹配的小图）
cv.imshow("input", src)                            # 显示源图像
cv.imshow("tpl", tpl)                              # 显示模板图像窗口


th, tw = tpl.shape[:2]                                      # 提取模板的高度(th)和宽度(tw)
#cv.matchTemplate()是OpenCV中用于实现模板匹配的核心函数，其功能是通过滑动窗口算法在源图像中寻找与模板图像最相似的区域
result = cv.matchTemplate(src, tpl, cv.TM_SQDIFF_NORMED)    # 使用归一化平方差匹配算法（TM_SQDIFF_NORMED）在源图像src中搜索模板tpl，返回匹配结果矩阵，值越小匹配度越高
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)   # 从结果矩阵中提取最小值/最大值及其坐标位置
top_left = min_loc                                          # 将最小值坐标作为最佳匹配区域的左上角点（x,y）
bottom_right = (top_left[0] + tw, top_left[1] + th)         # 计算匹配区域右下角坐标：x轴加模板宽度，y轴加模板高度（0代表x轴，1代表y轴）
cv.rectangle(src, top_left, bottom_right, (0,255,0), 2)     # 在源图像上绘制绿色矩形框标记匹配区域，线宽为2像素
cv.imshow("match", src)                            # 显示带有匹配标记的源图像窗口

cv.waitKey(0)                                               # 等待按键
cv.destroyAllWindows()                                      # 关闭所有窗口