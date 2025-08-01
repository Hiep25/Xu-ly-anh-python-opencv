import numpy as np
import cv2

# Kích thước bàn cờ
board_size = 8  # 8x8 ô
square_size = 50  # Kích thước mỗi ô là 50x50 pixel

# Tạo một ảnh trắng có kích thước đủ để chứa bàn cờ
board = np.ones((board_size * square_size, board_size * square_size), dtype=np.uint8) * 255

# Vẽ các ô đen
for row in range(board_size):
    for col in range(board_size):
        # Kiểm tra nếu hàng và cột đều chẵn hoặc lẻ, ô sẽ được tô đen
        if (row + col) % 2 == 0:
            top_left = (row * square_size, col * square_size)
            bottom_right = ((row + 1) * square_size, (col + 1) * square_size)
            cv2.rectangle(board, top_left, bottom_right, 0, -1)  # Màu đen (0)

# Hiển thị bàn cờ
cv2.imshow('Chessboard', board)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh bàn cờ
cv2.imwrite('luuanh/banco.png', board)
