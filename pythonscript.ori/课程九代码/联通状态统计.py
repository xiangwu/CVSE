import cv2 as cv
import numpy as np

#连通区域是指图像中具有相同像素值且位置相邻的前景像素点组成的区域
def connected_components_stats_demo(src):
    # 预处理：高斯模糊和灰度转换
    src = cv.GaussianBlur(src, (3, 3), 0)     # 使用3×3核进行高斯平滑，消除高频噪声
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)             # 将BGR三通道图像转为单通道灰度图
    # 自动阈值二值化(使用OTSU算法)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 自动计算最佳阈值ret，生成黑白二值图binary（背景0/前景255）
    cv.imshow("binary", binary)
    # 连通组件分析(8连通域)
    # num_labels：连通域数量（含背景），labels：与输入同尺寸的标记矩阵，stats：各连通域统计信息（N×5矩阵，含x,y,width,height,area），centers：各连通域质心坐标
    num_labels, labels, stats, centers = cv.connectedComponentsWithStats(binary, connectivity=8, ltype=cv.CV_32S)  # connectivity=8：使用8邻域连通规则，ltype=cv.CV_32S：输出标签类型为32位整型
    # 为每个连通域生成随机颜色
    colors = []                                            # 创建名为colors的空列表对象,准备存储RGB元组或其他颜色表示形式
    for i in range(num_labels):
        b = np.random.randint(0, 256)            # 生成随机RGB颜色（0-255范围）
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))                           # 将生成的RGB颜色值添加到颜色列表中
    colors[0] = (0, 0, 0)                                  # 索引0对应背景，强制设为黑色(0,0,0)
    # 例：colors = ['red', 'green']，colors.append('blue')  # 结果：['red', 'green', 'blue']

    # 在原图上绘制标记
    image = np.copy(src)                                   # 创建源图像的副本避免污染原始数据
    for t in range(1, num_labels, 1):                      # 遍历从1开始的连通域标签，遍历连通域标签（从1到num_labels-1），跳过背景标签0
        x, y, w, h, area = stats[t]                        # 提取第t个连通域的统计信息，x, y：外接矩形左上角坐标，w, h：外接矩形的宽度和高度，area：连通域像素面积
        cx, cy = centers[t]                                # 提取第t个连通域的质心坐标。
        # 进行三重可视化标注：质心标记、外接矩形、标签编号
        # 质心标记：绿色实心圆点（半径2像素）
        cv.circle(image, (np.int32(cx), np.int32(cy)), 2, (0, 255, 0), 2, 8, 0)
        # 外接矩形：从预定义列表colors中取第t个颜色
        cv.rectangle(image, (x, y), (x+w, y+h), colors[t], 1, 8, 0)
        # 文本标注：红色标签编号显示在区域左上角
        # "num:" + str(t)：动态生成的文本内容（此处显示带编号的字符串),(x,y)：文本左下角基准坐标（默认坐标系原点在左上角）
        cv.putText(image, "num:" + str(t), (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1)
        print("label index %d, area of the label : %d"%(t, area))       # 控制台输出当前连通域的索引和面积。
    cv.imshow("colored labels", image)                         # 显示标注后的图像，窗口标题为"colored labels"。
   # cv.imwrite("D:/labels.png", image)                                 # 图像数据保存
    # 显示检测到的连通域总数（排除背景区域）
    print("total rice : ", num_labels - 1)                 # num_labels：通过cv.connectedComponentsWithStats()返回的标签总数（包含背景标签0）
                                                           # num_labels - 1：实际目标数量（扣除背景）

input = cv.imread(PictureAddress)                          # 读取图像文件
connected_components_stats_demo(input)                     # 调用connected_components_stats_demo() 函数

cv.waitKey(0)                                              # 等待按键
cv.destroyAllWindows()                                     # 关闭所有窗口