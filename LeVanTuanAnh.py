#đề bài
#đọc 1 file văn bản gồm nhiều dòng, ghi ra màn hình theo thứ tự ngược lại của các dòng
#vd
# nam quốc sơn hà
# nam đế cư
# thành
# nam đế cư
# nam quốc sơn hà

# Đọc tệp văn bản và lưu nội dung vào một danh sách
file_path = 'ten_file.txt'  # Thay đổi đường dẫn tệp văn bản tại đây
with open(file_path, 'r') as file:
    lines = file.readlines()

# In các dòng trong danh sách theo thứ tự ngược lại
for line in reversed(lines):
    print(line.strip())  # Xóa các ký tự trắng không cần thiết ở đầu và cuối dòng# Đọc tệp văn bản và lưu nội dung vào một danh sách
file_path = 'ten_file.txt'  # Thay đổi đường dẫn tệp văn bản tại đây
with open(file_path, 'r') as file:
    lines = file.readlines()

# In các dòng trong danh sách theo thứ tự ngược lại
for line in reversed(lines):
    print(line.strip())  # Xóa các ký tự trắng không cần thiết ở đầu và cuối dòng