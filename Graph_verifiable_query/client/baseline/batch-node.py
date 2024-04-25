import networkx as nx
import csv
import time
# def find_n_hop_neighbors_with_attr_at_distance(graph, start_node, n, attr, attr_value):
#     if start_node not in graph:
#         print(f"The node {start_node} is not in the graph.")
#         return set()
#
#     visited = set()
#     queue = [(start_node, 0)]
#
#     while queue:
#         node, distance = queue.pop(0)
#         if distance == n:
#             if node != start_node:
#                 return list(visited)
#         if distance > n:
#             return list(visited)
#         visited.add(node)
#         neighbors = list(graph.neighbors(node))
#         for neighbor in neighbors:
#             edge_attr = graph.edges[node, neighbor].get(attr)
#             # print(edge_attr)
#             if edge_attr is not None and edge_attr < attr_value:
#                 # print(edge_attr)
#                 if neighbor not in visited:
#                     queue.append((neighbor, distance + 1))
#
#     return list(visited)

def find_n_hop_neighbors_with_attr_at_distance(graph, start_node, n, attr, attr_value):
    if start_node not in graph:
        print(f"The node {start_node} is not in the graph.")
        return set()

    visited = set()
    queue = [(start_node, 0)]

    while queue:
        node, distance = queue.pop(0)
        if distance == n:
            visited.add(node)  # 包括起始节点
            return list(visited)
        if distance > n:
            return list(visited)
        if distance > 0:  # 排除起始节点
            visited.add(node)
        neighbors = list(graph.neighbors(node))
        for neighbor in neighbors:
            edge_attr = graph.edges[node, neighbor].get(attr)
            if edge_attr is not None and edge_attr < attr_value:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return list(visited)


# 使用示例
# G = nx.read_gml('2.gml')
t11=time.time()
G = nx.DiGraph()
with open('E:\\code\\jiaoben\\py111\\window1000.csv', encoding='utf-8', newline='') as cs:
# with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
    reader = csv.reader(cs)
    next(reader)
    # # noden = 0
    # line_number = 0
    for row in reader:
        if row:
            # line_number += 1
            # print(line_number)

            if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
                edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
                G.add_edge(row[5], row[6], **edge_data)
t22=time.time()
print("构建模型:",t22-t11)
l1 = 500

# 加载图数据
start_time = time.time()
with open("E:\\code\\jiaoben\\baseline\\output_sim1000.txt", "r") as file1:
    # 逐行读取并输出每一行
    for line_number1, line in enumerate(file1, start=1):
        print(line_number1)
        if line_number1 <= l1:
            # G = nx.DiGraph()
            # with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
            #     reader = csv.reader(cs)
            #     next(reader)
            #     # # noden = 0
            #     # line_number = 0
            #     for row in reader:
            #         if row:
            #             # line_number += 1
            #             # print(line_number)
            #
            #             if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
            #                 edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
            #                 G.add_edge(row[5], row[6], **edge_data)
            start_node = line.strip()  # 想要查找邻居的节点
            n = 1# 距离
            attr = 'Attribute_3'  # 属性名称
            attr_value = '11001001'  # 属性值
            # attr2 = 'attr2'  # 属性2名称
            # attr_value2 = 20  # 属性2值
            neighbors = find_n_hop_neighbors_with_attr_at_distance(G, start_node, n, attr, attr_value)
            # print(neighbors)
        if line_number1 % 100 == 0:
            wo_time = time.time()
            # print("time:", wo_time, "seconds")
            tim = wo_time - start_time+(t22-t11)*line_number1
            print("Execution time:", tim, "seconds")
        if line_number1 >500 :
            break
print("Execution time:",t22-t11, "seconds")
print("Execution time:", wo_time - start_time, "seconds")


