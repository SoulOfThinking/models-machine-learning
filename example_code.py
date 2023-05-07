import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('Fourier.jpg')
plt.subplot(331), plt.imshow(img), plt.title('picture')

# 根据公式转成灰度图
img = 0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]

# 显示灰度图
plt.subplot(332), plt.imshow(img, 'gray'), plt.title('picture_gray')

# 进行傅立叶变换，并显示结果
fft2 = np.fft.fft2(img)
plt.subplot(333), plt.imshow(np.abs(fft2), 'gray'), plt.title('fft2')

# 将图像变换的原点移动到频域矩形的中心，并显示效果
shift2center = np.fft.fftshift(fft2)
plt.subplot(334), plt.imshow(np.abs(shift2center), 'gray'), plt.title('shift2center')

# 对傅立叶变换的结果进行对数变换，并显示效果
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(335), plt.imshow(log_fft2, 'gray'), plt.title('log_fft2')

# 对中心化后的结果进行对数变换，并显示结果
log_shift2center = np.log(1 + np.abs(shift2center))
plt.subplot(336), plt.imshow(log_shift2center, 'gray'), plt.title('log_shift2center')
# plt.show()
plt.savefig('output_test.jpg')