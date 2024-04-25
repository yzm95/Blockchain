import pandas as pd
import os

# # # 定义一个空的 DataFrame 用于存储所有数据
combined_data = pd.DataFrame()

# 循环读取并合并所有 CSV 文件
# for i in range(50):
#     filename = f"block3\\blocks{i}.csv"
#     if os.path.exists(filename):  # 检查文件是否存在
#         df = pd.read_csv(filename)  # 读取 CSV 文件
#         #df = df.iloc[0:]  # 删除第一行
#         combined_data = pd.concat([combined_data, df], ignore_index=True)  # 合并到总 DataFrame 中
#
# # 将合并后的数据写入新的 CSV 文件
# combined_data.to_csv("5000B_3.csv", index=False)


# 定义一个空的 DataFrame 用于存储所有数据
# combined_data2 = pd.DataFrame()

# 循环读取并合并所有 CSV 文件
# for i in range(50):
#     filename1 = f"transaction2\\transactions{i}.csv"
#     if os.path.exists(filename1):  # 检查文件是否存在
#         df1 = pd.read_csv(filename1)  # 读取 CSV 文件
#         #df = df.iloc[0:]  # 删除第一行
#         combined_data2 = pd.concat([combined_data2, df1], ignore_index=True)  # 合并到总 DataFrame 中
#
# # 将合并后的数据写入新的 CSV 文件
# combined_data2.to_csv("5000_2.csv", index=False)



# combined_data2 = pd.DataFrame()
#
# # 循环读取并合并所有 CSV 文件
# for i in range(2):
#     filename1 = f"combined_transaction{i}.csv"
#     if os.path.exists(filename1):  # 检查文件是否存在
#         df1 = pd.read_csv(filename1)  # 读取 CSV 文件
#         #df = df.iloc[0:]  # 删除第一行
#         combined_data2 = pd.concat([combined_data2, df1], ignore_index=True)  # 合并到总 DataFrame 中
#
# # 将合并后的数据写入新的 CSV 文件
# combined_data2.to_csv("20000.csv", index=False)

# for i in range(1):
#     filename = f"combined_blocks{i}.csv"
#     if os.path.exists(filename):  # 检查文件是否存在
#         df = pd.read_csv(filename)  # 读取 CSV 文件
#         #df = df.iloc[0:]  # 删除第一行
#         combined_data = pd.concat([combined_data, df], ignore_index=True)  # 合并到总 DataFrame 中
#
# # 将合并后的数据写入新的 CSV 文件
# combined_data.to_csv("10000B.csv", index=False)


# 读取第一个CSV文件
df1 = pd.read_csv("10000B.csv")

# 读取第二个CSV文件
df2 = pd.read_csv("5000B_2.csv")

# 合并两个DataFrame
combined_data = pd.concat([df1, df2], ignore_index=True)

# 将合并后的数据写入新的CSV文件
combined_data.to_csv("15000B.csv", index=False)
