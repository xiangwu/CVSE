import cv2 as cv

src = cv.imread(PictureAddress)                                           # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                      # 创建可自动调整大小的窗口
cv.imshow("input", src)                                          # 显示图像

# 形态学梯度 - 基本梯度
# cv.MORPH_RECT：指定矩形结构元素；(3,3)：核的尺寸（宽×高）；(-1,-1)：锚点位置（默认中心点）
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
basic = cv.morphologyEx(src, cv.MORPH_GRADIENT, se)                       # cv.MORPH_GRADIENT：指定形态学梯度操作类型
#cv.imshow("basic gradient", basic)
gray = cv.cvtColor(basic, cv.COLOR_BGR2GRAY)                              # 转化为灰度图像
# 应用阈值处理以获取二值图像
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#cv.imshow("binary", binary)

# 生成1×5像素的垂直矩形核（适合检测垂直特征；锚点位于中心位置(-1,-1)
se = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
# 形态学膨胀操作‌：使用垂直核增强二值图像中的垂直结构；连接断裂的边缘并加粗垂直特征
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, se)
# 轮廓检测‌  ：cv.CHAIN_APPROX_SIMPLE：轮廓近似方法（压缩水平/垂直/对角线方向的冗余点）
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
# boundingRect()函数计算轮廓的最小外接矩形  x,y：矩形左上角坐标（像素单位） w,h：矩形的宽度和高度（像素单位）
    x, y, w, h = cv.boundingRect(contours[c])                             # contours[c]：从findContours()获取的轮廓集合中的第c个轮廓
    area = cv.contourArea(contours[c])                                    # 计算轮廓的像素面积（返回值：浮点型面积值）
    if area < 200:                                                        # 面积筛选‌：过滤掉面积小于200像素的轮廓（去除小噪点）
        continue
    if h > (3*w) or h < 20:                                               # 比例筛选‌：排除高度大于3倍宽度或高度小于20像素的轮廓（过滤线状干扰）
        continue
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)           # 矩形标注‌：对符合条件的轮廓用红色矩形标记（边框厚度1px）
# 显示
cv.imshow('output',src)

cv.waitKey(0)                                                             # 等待按键
cv.destroyAllWindows()                                                    # 关闭所有窗口


