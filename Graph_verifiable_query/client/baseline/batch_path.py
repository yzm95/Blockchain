import networkx as nx
import time
import csv

# def find_all_n_length_paths_with_attr_lt(graph, start_node, n, attr, attr_value, path=None):
#     if path is None:
#         path = [start_node]
#     else:
#         path = path + [start_node]
#
#     if len(path) == n:
#         return [path]
#
#     if len(path) > n:
#         return []
#
#     paths = []
#     for neighbor in graph.neighbors(start_node):
#         edge_attr = graph.edges[start_node, neighbor]
#         if attr in edge_attr and str(edge_attr[attr]) < str(attr_value):
#             if neighbor not in path:
#                 new_paths = find_all_n_length_paths_with_attr_lt(graph, neighbor, n, attr, attr_value, path)
#                 for new_path in new_paths:
#                     paths.append(new_path)
#     return paths

def find_all_n_length_paths_with_attr_lt(graph, start_node, n, attr, attr_value, path=None):
    if path is None:
        path = [start_node]
    else:
        path = path + [start_node]

    if len(path) == n:
        return [path]

    if len(path) > n:
        return []

    paths = []
    for neighbor in graph.neighbors(start_node):
        edge_attr = graph.edges[start_node, neighbor]
        if attr in edge_attr and str(edge_attr[attr]) < str(attr_value):
            # if neighbor not in path:
                new_paths = find_all_n_length_paths_with_attr_lt(graph, neighbor, n, attr, attr_value, path)
                for new_path in new_paths:
                    paths.append(new_path)
    return paths


t11=time.time()
G = nx.DiGraph()
with open('E:\\code\\jiaoben\\py111\\window1000.csv', encoding='utf-8', newline='') as cs:
# with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
    reader = csv.reader(cs)
    next(reader)
    for row in reader:
        if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
            edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
            G.add_edge(row[5], row[6], **edge_data)
t22=time.time()
print("构建模型:",t22-t11)

l1 = 500

# 加载图数据
start_time = time.time()
with open("E:\\code\\jiaoben\\baseline\\output_sim500.txt", "r") as file1:
    # 逐行读取并输出每一行
    for line_number1, line in enumerate(file1, start=1):
        print(line_number1)
        if line_number1 == 72:
        # if line_number1 <= l1 and line_number1 != 72:
            # G = nx.DiGraph()
            # with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
            #     reader = csv.reader(cs)
            #     next(reader)
            #     for row in reader:
            #         if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
            #             edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
            #             G.add_edge(row[5], row[6], **edge_data)



            start_node = line.strip()  # 起始节点
            n =5 # 想要查找的路径长度
            n = n + 1
            attr = 'Attribute_3'  # 属性名称
            attr_value = '11001001'  # 属性值
            if start_node not in G:
                print("起始节点不存在于图中。")
            else:
                paths = find_all_n_length_paths_with_attr_lt(G, start_node, n, attr, attr_value)
                for path in paths:
                    edge_attrs = []
                    for i in range(len(path) - 1):
                        edge_attr = G.edges[path[i], path[i + 1]]
                        edge_attrs.append(edge_attr)
                    # print("路径:")
                    # print("路径:", path)
                    # print("边属性:", edge_attrs)
        if line_number1 % 100 == 0:
            wo_time = time.time()
            # print("time:", wo_time, "seconds")
            # tim = wo_time - start_time + (t22 - t11) * line_number1
            tim = wo_time - start_time
            print("Execution time:", tim, "seconds")
        if line_number1 > 500:
            break

print("Execution time:",t22-t11, "seconds")
print("Execution time:", wo_time - start_time, "seconds")

