import cv2
import numpy as np

# Đọc ảnh grayscale
image = cv2.imread('img/3.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng ngưỡng để tạo ảnh nhị phân
# Ở đây, ngưỡng là 127; tất cả các giá trị lớn hơn 127 sẽ trở thành 255 (trắng), nhỏ hơn sẽ trở thành 0 (đen)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Tạo một mặt nạ từ ảnh nhị phân
mask = binary_image

# Sử dụng mặt nạ để tách đối tượng từ ảnh gốc
extracted_object = cv2.bitwise_and(image, image, mask=mask)

# Hiển thị kết quả
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Extracted Object', extracted_object)

cv2.waitKey(0)
cv2.destroyAllWindows()