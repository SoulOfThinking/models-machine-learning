import cv2
import numpy as np

# DFT
def dft(img): #离散傅里叶变换
    H, W, channel = img.shape   #读取图片尺寸

    # Prepare DFT coefficient 返回来一个给定形状和类型的用0填充的数组np.complex是用复数
    G = np.zeros((H, W, channel), dtype=np.complex)
    # prepare processed index corresponding to original image positions
    x = np.tile(np.arange(W), (H, 1)) #np.arange()给定间隔内返回均匀间隔的值 默认起始值为0，默认步长为1
    #tile(A, reps)重复reps次A得到新的数组   这里是H行1列的np.arange(W)
    # print(x)
    # print(np.arange(W))
    # print((H, 1))
    y = np.arange(H).repeat(W).reshape(H, -1)#repeat()每个元素重复w次 （H, -1) 行数固定，列数需要计算
    #print(y)

    # dft
    for c in range(channel):
        for v in range(H):
            for u in range(W):
                G[v, u, c] = np.sum(img[..., c] * np.exp(-2j * np.pi * (x * u / W + y * v / H))) / np.sqrt(H * W)

    return G

# IDFT
def idft(G):
    # prepare out image
    H, W, channel = G.shape
    out = np.zeros((H, W, channel), dtype=np.float32)

    # prepare processed index corresponding to original image positions
    x = np.tile(np.arange(W), (H, 1))
    y = np.arange(H).repeat(W).reshape(H, -1)

    # idft
    for c in range(channel):
        for v in range(H):
            for u in range(W):
                out[v, u, c] = np.abs(np.sum(G[..., c] * np.exp(2j * np.pi * (x * u / W + y * v / H)))) / np.sqrt(W * H)

    # clipping
    out = np.clip(out, 0, 255)#数据限制在0-255之间
    out = out.astype(np.uint8)#数组类型进行转换，转换成图像类型

    return out


# Read image
img = cv2.imread("Fourier.jpg").astype(np.float32)

# DFT
G = dft(img)

# write poser spectal to image
ps = np.log(1+np.abs(G))
ps = (np.abs(G) / np.abs(G).max() * 255).astype(np.uint8)
cv2.imwrite("out_ps.jpg", ps)

# IDFT
out = idft(G)

# # Save result
cv2.imshow("result", out)
cv2.imwrite("out.jpg", out)
cv2.waitKey(0)
cv2.destroyAllWindows()