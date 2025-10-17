import cv2 as cv 

src = cv.imread(PictureAddress)                                                             # 读取图像文件
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)                                        # 创建可自动调整大小的窗口
cv.imshow("input", src)                                                            # 显示图像

h, w = src.shape[:2]                                                                        # 提取图像的二维尺寸信息（高度和宽度）
print(h, w)

# 使用cv2.resize()函数对图像进行尺寸变换，绝对尺寸和相对比例两种参数模式
# (300,300)指定目标尺寸，fx/fy=0.75表示宽高各变为原来的0.75倍，当目标尺寸与缩放系数冲突时，以目标尺寸优先
dst1 = cv.resize(src, (300, 300), fx=0.75, fy=0.75, interpolation=cv.INTER_NEAREST)   # 使用最近邻插值(INTER_NEAREST)方式（最快）
cv.imshow("INTER_NEAREST", dst1)                                                   # 显示图像

dst2 = cv.resize(src, (w*1, h*1), interpolation=cv.INTER_LINEAR)                      # 仅使用绝对尺寸（优先执行），采用双线性插值算法INTER_LINEAR,平衡速度与质量（默认)
cv.imshow("INTER_LINEAR", dst2)

dst3 = cv.resize(src,None,fx=0.75, fy=0.75, interpolation=cv.INTER_CUBIC)             # 仅使用缩放因子，采用三次卷积插值算法INTER_CUBIC（较高质量）
cv.imshow("INTER_CUBIC", dst3)

dst4 = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_LANCZOS4)                    # 仅使用绝对尺寸，采用Lanczos插值算法
cv.imshow("INTER_LANCZOS4", dst4)

#补充
dst5=cv.resize(src, None,fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)                 # cv.INTER_AREA 使用区域插值算法（INTER_AREA适合图像缩小操作）
cv.imshow("INTER_AREA", dst5)

cv.waitKey(0)                                                                               # 等待按键
cv.destroyAllWindows()                                                                      # 关闭所有窗口