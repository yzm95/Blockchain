import networkx as nx
import csv

def find_n_hop_neighbors_with_attrs_at_distance(graph, start_node, n, attr1, attr_value1, attr2, attr_value2):
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
            edge_attrs = graph.edges[node, neighbor]
            attr1_value = edge_attrs.get(attr1)
            attr2_value = edge_attrs.get(attr2)
            if attr1_value is not None and attr2_value is not None and attr1_value < attr_value1 and attr2_value < attr_value2:
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
attr1 = 'attr1'  # 属性1名称
attr_value1 = 10  # 属性1值
attr2 = 'attr2'  # 属性2名称
attr_value2 = 20  # 属性2值
neighbors = find_n_hop_neighbors_with_attrs_at_distance(G, start_node, n, attr1, attr_value1, attr2, attr_value2)
print(neighbors)

