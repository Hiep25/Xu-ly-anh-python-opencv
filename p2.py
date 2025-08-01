import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
image = cv2.imread('img/xuong.jpg', cv2.IMREAD_GRAYSCALE)

# Bước 1: Áp dụng Laplacian Filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Bước 2: Áp dụng Sobel Filter để phát hiện cạnh
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # phát hiện cạnh theo trục x
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)  # phát hiện cạnh theo trục y
sobel_combined = cv2.magnitude(sobelx, sobely)

# Bước 3: Làm sắc nét ảnh bằng cách trừ ảnh gốc và Laplacian
sharpened_image = cv2.subtract(image, cv2.convertScaleAbs(laplacian))

# Bước 4: Làm mượt ảnh bằng bộ lọc trung bình
smoothed_image = cv2.blur(sharpened_image, (5, 5))

# Bước 5: Áp dụng Power-law Transformation (Gamma Correction)
gamma = 0.5
corrected_image = np.array(255 * (smoothed_image / 255) ** gamma, dtype='uint8')

# So sánh ảnh ban đầu và ảnh đã qua xử lý
titles = ['Original Image', 'Laplacian Filter', 'Sobel Combined', 'Sharpened Image', 'Smoothed Image', 'Gamma Corrected']
images = [image, cv2.convertScaleAbs(laplacian), sobel_combined, sharpened_image, smoothed_image, corrected_image]

# Hiển thị các ảnh để so sánh
plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
