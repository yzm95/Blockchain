
import csv

# 原始CSV文件名
# input_filename = "C:\\Users\\87778\\Desktop\\blocks.csv"
input_filename = "E:\\code\\jiaoben\\py111\\15000B.csv"

# 修改后的CSV文件名
new_filename = "block.csv"

# 要保留的列索引
columns_to_keep = [0,1,12,16]

# 打开原始CSV文件
with open(input_filename, encoding='utf-8', newline='') as infile:
    # 读取CSV文件
    reader = csv.reader(infile)
    # 获取头部行
    header = next(reader)
    # 修改头部行
    header[0] = "blo:ID"
    # header[1]="name"
    # header[12] = header[12]+":string"
    # header[16] = header[16]+":string"


    # 获取保留列的标题
    new_header = [header[i] for i in columns_to_keep]
    # 添加新的头部列
    new_header.append(":LABEL")

    # 打开修改后的CSV文件
    with open(new_filename, 'w', encoding='utf-8', newline='') as outfile:
        # 创建CSV写入对象
        writer = csv.writer(outfile)
        # 写入修改后的头部行
        writer.writerow(new_header)

        # 复制非空行并为每行添加 ":LABEL" 列
        for row in reader:
            if any(row):
                # 获取保留列的数据
                new_row = [row[i] for i in columns_to_keep]
                # 添加新的列数据
                new_row.append("block")
                writer.writerow(new_row)

print(f"文件名已修改为'{new_filename}'")
