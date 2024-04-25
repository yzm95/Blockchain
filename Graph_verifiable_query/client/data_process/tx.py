import pandas as pd

# 读取CSV文件
# df = pd.read_csv('C:\\Users\\87778\\Desktop\\transactions.csv')
df = pd.read_csv('E:\\code\\jiaoben\\py111\\15000.csv')
# 组合第4列和第5列的数据为新列
df['TX:ID'] = df.iloc[:, 3].astype(str) + '_' + df.iloc[:, 4].astype(str)

# 保留ID列和:LABEL列
df = df[['TX:ID']]

# 添加新列:LABEL，数据内容为"tx"
df[':LABEL'] = 'tx'

# 保存到新文件
df.to_csv('tx.csv', index=False)
