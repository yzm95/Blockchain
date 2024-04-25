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
    reader = csv.reader(cs)
    next(reader)
    for row in reader:
        if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
            edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
            G.add_edge(row[5], row[6], **edge_data)
t22=time.time()
print("构建模型:",t22-t11)

l1 = 1

# 加载图数据
start_time = time.time()
with open("E:\\code\\jiaoben\\baseline\\output_sim1000.txt", "r") as file1:
    # 逐行读取并输出每一行
    for line_number1, line in enumerate(file1, start=1):
        print(line_number1)
        if line_number1 <= l1:
            start_node = line.strip()  # 起始节点
            n = 5 # 想要查找的路径长度
            n = n + 1
            attr = 'Attribute_3'  # 属性名称
            attr_value = '11001001'  # 属性值
            if start_node not in G:
                print("起始节点不存在于图中。")
            else:
                paths = find_all_n_length_paths_with_attr_lt(G, start_node, n, attr, attr_value)
                l = 1
                for path in paths:
                    # edge_attrs = []
                    print(l)
                    l=l+1

                    for i in range(len(path) - 1):
                        edge_attr = G.edges[path[i], path[i + 1]]
                        print(edge_attr)
                        print(edge_attr['Attribute_3'],edge_attr['Attribute_4'])
                        with open('E:\\code\\jiaoben\\py111\\window1000.csv', encoding='utf-8', newline='') as f1:
                            reader = csv.DictReader(f1)
                            for row in reader:
                                if row['block_number'] == edge_attr['Attribute_3'] and row['transaction_index'] == edge_attr['Attribute_4']:
                                    print(row)
                        # edge_attrs.append(edge_attr)
                    # print("路径:", path)
                    # print("边属性:", edge_attrs)
                    # print("边属性:", edge_attrs)
                print(l)
            t2 = time.time()
            p=paths
            if (paths==p):
                print("对比时间:", t2 - start_time)
        if line_number1 % 100 == 0:
            wo_time = time.time()
            # print("time:", wo_time, "seconds")
            tim = wo_time - start_time + (t22 - t11) * line_number1
            print("Execution time:", tim, "seconds")
        if line_number1 > l1:
            break



