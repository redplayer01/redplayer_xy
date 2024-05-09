import os
import shutil

def rename_files(root_dir, output_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, _, files in os.walk(root_dir):
            for filename in files:
                try:
                    # 构建旧文件路径和新文件路径
                    old_path = os.path.join(root, filename)
                    
                    # 获取文件名的 UTF-8 编码的 16 进制表示形式
                    new_filename_hex = filename.encode('utf-8').hex()
                    new_path = os.path.join(output_dir, new_filename_hex)
                    
                    # 复制文件到新路径
                    shutil.copy2(old_path, new_path)
                    
                    # 解码新文件名并写入文件名列表
                    decoded_filename = bytes.fromhex(new_filename_hex).decode('utf-8')
                    f.write(new_filename_hex  + '\n')
                    
                    print(f"Original filename: {filename}, New filename: {decoded_filename}, Encode filename: {new_filename_hex}")
                    
                except Exception as e:
                    print(f"Error processing file: {filename} - {e}")

# 指定要处理的目录
root_dir = './source_/'
# 指定保存修改后文件的目录
output_dir = './source/'
# 指定保存新文件名的文件路径
output_file = './list.txt'

# 调用函数重命名文件并保存到另一个目录，并生成文件名列表
rename_files(root_dir, output_dir, output_file)

print("Files renamed and saved successfully!")
