
import cv2

# Tải hình ảnh
image = cv2.imread('img/5.jpg', cv2.IMREAD_GRAYSCALE)

# Đảo ngược màu sắc bằng cách trừ các giá trị pixel từ 255
inverted_image = 255 - image

# Lưu hoặc hiển thị kết quả
cv2.imwrite('inverted_image.jpg', inverted_image)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()