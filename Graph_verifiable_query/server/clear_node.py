from py2neo import Graph, Node, Relationship

### 删除所有的节点和关系
#gragh = Graph('bolt://localhost:7687', auth = ('neo4j', '12345678'))

gragh = Graph('bolt://172.19.8.25:7687/', auth = ('neo4j', '141001'))
gragh.run('MATCH (n) DETACH DELETE n;')
print('clear!')


# gragh = Graph('bolt://localhost:7687', auth = ('neo4j', '12345678'))
# gragh.run('MATCH (n) WHERE ID(n) >= 1 AND ID(n) <= 10000 DETACH DELETE n;')
# print('clear!')


# match (n) optional match (n)-[r]-() delete n,r