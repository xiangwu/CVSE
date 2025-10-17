import cv2 as cv
import numpy as np


# 原始图像 → 灰度化 → 二值化 → 轮廓提取 → 计算Hu矩 → 形状匹配 → 可视化结果
#                      ↑
#               (Otsu自动阈值)


src = cv.imread(Picture1Address)                            # 读取图像文件1
cv.imshow("input1", src)                           # 显示图像1
src2 = cv.imread(Picture2Address)                           # 读取图像文件2
cv.imshow("input2", src2)                          # 显示图像2

# 提取图像轮廓
def contours_info(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)            # 转为灰度图
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)      # Otsu算法自适应确定二值化阈值
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)        # 轮廓发现，RETR_EXTERNAL只检测最外层轮廓
    return contours
# 轮廓提取
contours1 = contours_info(src)                              # 提取图像1轮廓
contours2 = contours_info(src2)                             # 提取图像2轮廓
# 几何矩计算与hu矩计算
mm2 = cv.moments(contours2[0])                              # 通过cv.moments()计算src2的几何矩（24个特征）
hum2 = cv.HuMoments(mm2)                                    # 转换为Hu矩（7个旋转/缩放不变特征）
# 轮廓匹配
for c in range(len(contours1)):                             # 遍历contours1
    mm = cv.moments(contours1[c])                           # 通过cv.moments()计算src1的几何矩
    hum = cv.HuMoments(mm)                                  # 转换为Hu矩
    # 形状匹配
    dist = cv.matchShapes(hum, hum2, cv.CONTOURS_MATCH_I1, 0)     # 计算形状距离，CONTOURS_MATCH_I1：使用第一种相似度度量方法
    if dist < 1:                                                           # 距离值dist越小表示形状越相似，这里选1.0是经验值，可根据实际调整
        cv.drawContours(src, contours1, c, (0, 0, 255), 2, 8)
    print("dist %f"%(dist))

# 显示
cv.imshow("contours_analysis", src)
#cv.imwrite("D:/contours_analysis.png", src)

cv.waitKey(0)                                              # 等待按键
cv.destroyAllWindows()                                     # 关闭所有窗口


