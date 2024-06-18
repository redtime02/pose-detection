# from PIL import Image
# import os

# # Đường dẫn tới thư mục chứa dataset
# dataset_path = './dataset'
# output_path = './output'

# # Tạo thư mục output nếu chưa tồn tại
# if not os.path.exists(output_path):
#     os.makedirs(output_path)

# # Các thư mục con
# subdirs = ['left', 'right']

# for subdir in subdirs:
#     # Đường dẫn tới thư mục con
#     subdir_path = os.path.join(dataset_path, subdir)
#     output_subdir_path = os.path.join(output_path, subdir)
    
#     # Tạo thư mục output cho thư mục con nếu chưa tồn tại
#     if not os.path.exists(output_subdir_path):
#         os.makedirs(output_subdir_path)
    
#     # Liệt kê các file trong thư mục con
#     files = os.listdir(subdir_path)
    
#     # Biến đếm để đặt tên file
#     count = 1
    
#     for file in files:
#         # Đường dẫn đầy đủ tới file
#         file_path = os.path.join(subdir_path, file)
        
#         # Mở và chuyển đổi ảnh sang định dạng JPG
#         with Image.open(file_path) as img:
#             # Tạo tên file mới
#             new_file_name = f'{subdir}_image_{count}.jpg'
#             new_file_path = os.path.join(output_subdir_path, new_file_name)
            
#             # Lưu ảnh với định dạng JPG
#             img.convert('RGB').save(new_file_path, 'JPEG')
            
#             # Tăng biến đếm
#             count += 1

# print('Chuyển đổi hoàn tất.')

from PIL import Image
import os

# Đường dẫn tới thư mục chứa dataset
dataset_path = './dataset'
output_path = './output'

# Kích thước mới cho các hình ảnh
new_size = (512, 512)  # Ví dụ: (256, 256)

# Tạo thư mục output nếu chưa tồn tại
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Các thư mục con
subdirs = ['left', 'right']

for subdir in subdirs:
    # Đường dẫn tới thư mục con
    subdir_path = os.path.join(dataset_path, subdir)
    output_subdir_path = os.path.join(output_path, subdir)
    
    # Tạo thư mục output cho thư mục con nếu chưa tồn tại
    if not os.path.exists(output_subdir_path):
        os.makedirs(output_subdir_path)
    
    # Liệt kê các file trong thư mục con
    files = os.listdir(subdir_path)
    
    # Biến đếm để đặt tên file
    count = 1
    
    for file in files:
        # Đường dẫn đầy đủ tới file
        file_path = os.path.join(subdir_path, file)
        
        # Mở và chuyển đổi ảnh sang định dạng JPG
        with Image.open(file_path) as img:
            # Thay đổi kích thước ảnh
            img_resized = img.resize(new_size, Image.LANCZOS)
            
            # Tạo tên file mới
            new_file_name = f'{subdir}_image_{count}.jpg'
            new_file_path = os.path.join(output_subdir_path, new_file_name)
            
            # Lưu ảnh với định dạng JPG
            img_resized.convert('RGB').save(new_file_path, 'JPEG')
            
            # Tăng biến đếm
            count += 1

print('Chuyển đổi và thay đổi kích thước hoàn tất.')