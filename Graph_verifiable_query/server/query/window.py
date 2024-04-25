import time
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship


# 记录开始时间
start_time = time.time()

# 运行查询并将结果存储在列表中
graph = Graph('bolt://172.19.8.25:7687/', auth=('neo4j', '141001'))
result = graph.run(
    'MATCH (sourceNode)-[r1:node_tx_node]->(Node1) WHERE r1.block_number < \'11000501\' RETURN r1')
records = list(result)




# 定义批量写入的大小
batch_size = 1000
batch = []

# 批量写入函数
def write_batch_to_file(batch):
    with open('res.txt', 'a') as file:
        for record in batch:
            file.write(str(record) + '\n')

# 遍历结果记录列表
for i, record in enumerate(records):
    batch.append(record)
    # 如果达到批量写入的大小或者已经是最后一条记录，则写入文件
    if len(batch) == batch_size or i == len(records) - 1:
        write_batch_to_file(batch)
        batch = []

# 记录结束时间
end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time
print("执行时间:", execution_time, "秒")