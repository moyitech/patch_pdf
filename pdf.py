import os
import PyPDF2

def remove_pdf_passwords():
    # 获取当前工作目录
    input_dir = os.getcwd()
    output_dir = os.path.join(input_dir, 'output')

    # 创建输出目录，如果不存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                # 打开PDF文件
                with open(input_path, 'rb') as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)

                    # 检查是否有密码
                    if reader.is_encrypted:
                        # 尝试解密PDF文件
                        try:
                            reader.decrypt('')  # 使用空密码尝试解密
                        except Exception as e:
                            print(f"无法解密文件 {filename}: {e}")
                            continue

                    # 创建一个新的PDF写入器
                    writer = PyPDF2.PdfWriter()

                    # 将所有页面添加到新的PDF文件中
                    for page in reader.pages:
                        writer.add_page(page)

                    # 保存去除密码的PDF文件
                    with open(output_path, 'wb') as output_file:
                        writer.write(output_file)

                    print(f"已去除密码并保存文件: {output_path}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

# 运行程序
remove_pdf_passwords()

