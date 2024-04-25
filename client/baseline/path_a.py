import networkx as nx
import time
import csv

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
            if neighbor not in path:
                new_paths = find_all_n_length_paths_with_attr_lt(graph, neighbor, n, attr, attr_value, path)
                for new_path in new_paths:
                    paths.append(new_path)
    return paths

time1 = time.time()
G = nx.DiGraph()
with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
    reader = csv.reader(cs)
    next(reader)
    for row in reader:
        if row and row[5] != '' and row[6] != '' and row[5] != row[6]:
            edge_data = {f'Attribute_{i}': row[i] for i in range(len(row)) if i not in [5, 6]}
            G.add_edge(row[5], row[6], **edge_data)

time2 = time.time()
print("创建图的时间:", time2 - time1)

start_node = '0xa7efae728d2936e78bda97dc267687568dd593f3'  # 起始节点
n = 5  # 想要查找的路径长度
attr = 'Attribute_3'  # 属性名称
attr_value = '11001001'  # 属性值
if start_node not in G:
    print("起始节点不存在于图中。")
else:
    paths = find_all_n_length_paths_with_attr_lt(G, start_node, n, attr, attr_value)
    for path in paths:
        edge_attrs = []
        for i in range(len(path) - 1):
            edge_attr = G.edges[path[i], path[i+1]]
            edge_attrs.append(edge_attr)
        print("路径:", path)
        print("边属性:", edge_attrs)

time3 = time.time()
print("查找路径的时间:", time3 - time2)
