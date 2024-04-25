import networkx as nx
import csv

def find_n_hop_neighbors_with_attr_at_distance(graph, start_node, n, attr, attr_value):
    if start_node not in graph:
        print(f"The node {start_node} is not in the graph.")
        return set()

    visited = set()
    queue = [(start_node, 0)]

    while queue:
        node, distance = queue.pop(0)
        if distance == n:
            if node != start_node:
                return list(visited)
        if distance > n:
            return list(visited)
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

G = nx.DiGraph()
with open('E:\\code\\jiaoben\\py111\\combined_transaction1.csv', encoding='utf-8', newline='') as cs:
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

start_node = '0xa7efae728d2936e78bda97dc267687568dd593f3'  # 想要查找邻居的节点
n = 5  # 距离
attr = 'Attribute_3'  # 属性名称
attr_value = '11001001'  # 属性值
# attr2 = 'attr2'  # 属性2名称
# attr_value2 = 20  # 属性2值
neighbors = find_n_hop_neighbors_with_attr_at_distance(G, start_node, n, attr, attr_value)
print(neighbors)

