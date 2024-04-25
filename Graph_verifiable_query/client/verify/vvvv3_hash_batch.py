import networkx as nx
import time
import csv
import hashlib


def hash_fun(attrs):
    return hashlib.sha256(str(attrs).encode()).hexdigest()

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

def find_all_n_length_paths_with_attr_lt(graph, start_node, n, path=None):
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
        # edge_attr = graph.edges[start_node, neighbor]
            # if neighbor not in path:
        new_paths = find_all_n_length_paths_with_attr_lt(graph, neighbor, n, path)
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

l1 = 500

# 加载图数据
ttt = 0
ttt2 = 0
with open("E:\\code\\jiaoben\\baseline\\output_sim1000.txt", "r") as file1:
    # 逐行读取并输出每一行

    for line_number1, line in enumerate(file1, start=1):
        # print(line_number1)
        if line_number1 <= l1:
            start_node = line.strip()  # 起始节点
            n =5# 想要查找的路径长度
            n = n + 1
            if start_node not in G:
                print("起始节点不存在于图中。")
            else:
                paths = find_all_n_length_paths_with_attr_lt(G, start_node, n)
                t2 = time.time()
                visited_edges = set()
                Gh = nx.DiGraph()
                for path in paths:
                    for i in range(len(path) - 1):
                        edge_attr = G.edges[path[i], path[i + 1]]
                        edge_attr_tuple = (edge_attr['Attribute_3'], edge_attr['Attribute_4'])
                        if edge_attr_tuple in visited_edges:
                            # print('访问过了')
                            continue
                        else:
                            # print('没访问')
                            visited_edges.add(edge_attr_tuple)
                            attr_hash = hashlib.sha256(str(edge_attr).encode()).hexdigest()
                            source = path[i]
                            target = path[i + 1]
                            if Gh.has_edge(source, target):
                                combined_attrs = G[source][target].get('hash', '') + attr_hash
                                Gh[source][target]['hash'] = hashlib.sha256(combined_attrs.encode()).hexdigest()
                            else:
                                Gh.add_edge(source, target, hash=attr_hash)
                t3 = time.time()
                nx.write_gml(Gh, "1.gml")
                t4 = time.time()
                G1 = nx.read_gml("1.gml")
                if Gh == G1:
                    print('yes')
                t5=time.time()
                t=t5-t4+t3-t2
                ttt = ttt + t


        if line_number1 % 100 == 0:
            print( ttt, "seconds")
        if line_number1 > l1:
            break



print("Execution time:", ttt/500, "seconds")
# for source, target, attrs in Gh.edges(data=True):
#     print(f"边: {source} -> {target}, 哈希属性: {attrs.get('hash', '')}")


