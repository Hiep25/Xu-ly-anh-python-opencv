````markdown
 🧠 Dự án Xử lý Ảnh với OpenCV & NumPy (Python)

Đây là các chương trình xử lý ảnh được viết bằng Python sử dụng thư viện OpenCV và NumPy. Mỗi file đại diện cho một kỹ thuật cụ thể — từ thao tác điểm ảnh cơ bản, vẽ hình, tách đối tượng, xoay ảnh thủ công, đến xử lý biên, làm sắc nét và hiệu chỉnh gamma.

Thích hợp cho sinh viên, giảng viên và người học muốn khám phá nền tảng xử lý ảnh số.

---

 📁 Cấu trúc các tập tin

| Tập tin                        | Mô tả chức năng                                                                |
|-------------------------------|----------------------------------------------------------------------------------|
| `Checkered Board.py`          | Vẽ bàn cờ caro 8x8 bằng NumPy và lưu lại hình ảnh                               |
| `Color Correction.py`         | Đảo ngược màu sắc ảnh xám (hiệu ứng âm bản)                                     |
| `Color Separation.py`         | Áp dụng ngưỡng nhị phân và tách đối tượng trong ảnh đen trắng                   |
| `Corner Line.py`              | Vẽ đường xiên vào ảnh bằng thao tác trực tiếp trên mảng pixel                   |
| `Find secret by subtract.py`  | Vẽ chữ cái “G” bằng cách tô điểm ảnh trên nền trắng                             |
| `Gradient.py`                 | Tạo ảnh có gradient chuyển từ trắng sang đen theo chiều dọc                     |
| `Letter B.py`                 | Tạo chữ “B” bằng thao tác trực tiếp trên mảng ảnh                               |
| `p2.py`                       | Xử lý ảnh nâng cao: Laplacian, Sobel, làm sắc nét, làm mượt, hiệu chỉnh gamma   |
| `Rotate Image.py`             | Xoay ảnh grayscale 180 độ bằng thao tác mảng NumPy                              |

---

 🛠️ Yêu cầu cài đặt

- Python 3.x
- Thư viện cần thiết:
  - `opencv-python`
  - `numpy`
  - `matplotlib` *(dành cho `p2.py`)*

Cài đặt bằng pip:
```bash
pip install opencv-python numpy matplotlib
````

---

 ▶️ Cách chạy chương trình

Clone dự án về máy và chạy từng file bằng lệnh:

```bash
git clone https://github.com/ten-cua-ban/image-processing-labs.git
cd image-processing-labs

python Checkered\ Board.py

```

⚠️ Một số file yêu cầu có ảnh trong thư mục `img/`. Hãy đảm bảo ảnh đầu vào đúng đường dẫn.

---

 📸 Kết quả minh họa (tùy chọn)

Color Correction
<img width="1200" height="628" alt="image" src="https://github.com/user-attachments/assets/fbcbc523-8911-4504-b298-16fa55697ae6" />


Corner Line
<img width="1920" height="1280" alt="image" src="https://github.com/user-attachments/assets/9fa1bad7-b348-4733-bba6-f42bbd13165b" />

Find secret by subtract
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/f369d48c-0ca8-41d1-b867-86c1b6b5c54b" />


Gradient
<img width="255" height="255" alt="image" src="https://github.com/user-attachments/assets/cc23d5a8-7915-48f7-86c1-1815f1961872" />


p2
<img width="1915" height="1017" alt="image" src="https://github.com/user-attachments/assets/76930903-93f4-49ca-b1c6-785bed46aa87" />



---

 🎯 Mục tiêu dự án

Dự án được thiết kế phục vụ **học tập và minh họa kiến thức xử lý ảnh cơ bản và nâng cao**. Từng script tập trung vào một mục tiêu rõ ràng, dễ mở rộng hoặc tích hợp vào các bài tập lớn hơn.

---



 🙌 Lời cảm ơn

Cảm ơn cộng đồng Python và các thư viện mã nguồn mở:

* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

---

> 🌟 Nếu bạn thấy dự án hữu ích, hãy để lại ⭐ và chia sẻ với bạn bè!

```

