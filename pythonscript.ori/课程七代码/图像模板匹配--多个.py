import cv2 as cv
import numpy as np


src=cv.imread(Picture1Address)                 # 读取源图像（待搜索的大图）
tpl=cv.imread(Picture2Address)                 # 读取模板图像（待匹配的小图）
cv.imshow("input", src)               # 显示源图像
cv.imshow("tpl", tpl)                 # 显示模板图像窗口

h,w=tpl.shape[:2]                              # 提取模板的高度(th)和宽度(tw)
# 使用归一化平方差匹配算法（TM_SQDIFF_NORMED）在源图像src中搜索模板tpl，返回匹配结果矩阵，值越小匹配度越高
result = cv.matchTemplate(src, tpl, cv.TM_CCOEFF_NORMED)
threshold = 0.6                                # 相似度阈值（可调整，范围0-1）
# 多目标检测需结合阈值筛选：locations = np.where(result >=threshold)
loc = np.where(result >=threshold)             # 获取匹配度大于等于阈值的位置坐标，返回值为元组(y_array, x_array)，需反转顺序为(x,y)
# 生成所有匹配位置的左上角坐标点迭代器
for pt in zip(*loc[::-1]):                     # loc[::-1]:将坐标元组从(y,x)顺序反转为(x,y)顺序;*操作符：解包元组为独立参数;zip()：将x坐标数组和y坐标数组组合成(x,y)坐标点序列
    bottom_right = (pt[0] + w, pt[1] + h)      # 计算匹配区域右下角坐标：x轴加模板宽度，y轴加模板高度（0代表x轴，1代表y轴）
    cv.rectangle(src, pt, bottom_right, (0, 255, 0), 2)    # 在源图像上绘制绿色矩形框标记匹配区域，线宽为2像素
    cv.imshow("result", src)

cv.waitKey(0)                                  # 等待按键
cv.destroyAllWindows()                         # 关闭所有窗口