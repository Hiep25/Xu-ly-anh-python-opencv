import cv2
import numpy as np

# Tạo một mảng số nguyên 8 bit (0-255) với các giá trị từ 0 đến 90000
img_arr = np.arange(0, 90000, 1, np.uint8)
img = np.reshape(img_arr, (300, 300))
height, width = img.shape

# Tô toàn bộ hình ảnh màu trắng
img[:, :] = 255

# Vẽ chữ "G"

# Tạo đoạn dọc bên trái
img[50:250, 50:100] = 0

# Tạo đoạn ngang trên cùng
img[50:90, 100:210] = 0

# Tạo đoạn ngang dưới cùng
img[210:250, 100:210] = 0

# Tạo đoạn dọc bên phải từ giữa trở xuống
img[130:250, 160:210] = 0

# Tạo đoạn ngang giữa để đóng nét chữ "G"
img[130:170, 130:200] = 0

# Lưu hình ảnh kết quả
cv2.imwrite('result_G.png', img)
cv2.imshow("cuong",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
