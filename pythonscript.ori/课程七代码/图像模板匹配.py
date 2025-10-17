import cv2 as cv
import numpy as np


def template_demo():                                         # 定义一个模板匹配函数
    src = cv.imread(Picture1Address)                         # 读取源图像（待搜索的大图）
    tpl = cv.imread(Picture2Address)                         # 读取模板图像（待匹配的小图）
    cv.imshow("input", src)                         # 显示源图像
    cv.imshow("tpl", tpl)                           # 显示模板图像窗口
    th, tw = tpl.shape[:2]                                   # 提取模板的高度(th)和宽度(tw)
    # 执行模板匹配
    result = cv.matchTemplate(src, tpl, cv.TM_CCORR_NORMED)  # 返回值result矩阵中每个元素表示对应位置的匹配置信度（0~1，越接近1匹配度越高）
    #cv.imshow("result", result)                             # 创建一个窗口显示归一化后的匹配得分矩阵，亮度越高表示匹配概率越大
    #cv.imwrite("D:/039_003.png", np.uint8(result * 255))    # 将浮点型匹配结果（0~1范围）转换为8位灰度图（0~255），并通过cv.imwrite保存到指定路径
    # 设置匹配阈值并定位结果
    t = 0.955                                                # 相似度阈值（可调整，范围0-1）
    loc = np.where(result > t)                               # 获取匹配度高于阈值的位置坐标，返回值为元组(y_array, x_array)，需反转顺序为(x,y)
    # 绘制匹配区域矩形框
    for pt in zip(*loc[::-1]):                               # 遍历所有匹配位置，loc[::-1]：将(y,x)坐标反转为(x,y)格式，zip(*...)：解包并重组为(x,y)坐标点序列
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0) # 在源图像上绘制蓝色矩形框标记匹配区域（0代表x轴，1代表y轴）
    cv.imshow("llk-demo", src)                      # 显示带有匹配标记的源图像窗口
    #cv.imwrite("D:/039_003.png", np.uint8(result*255))      # 存储图像

template_demo()                                              #调用定义的模板匹配函数

cv.waitKey(0)                                                # 等待按键
cv.destroyAllWindows()                                       # 关闭所有窗口
