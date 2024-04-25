import csv
from py2neo import Graph, Node, Relationship
import networkx as nx
import numpy as np


### 建立图
gragh = Graph('bolt://172.19.8.25:7687/', auth=('neo4j', '141001'))
with open('/nfs/srv/data2/zmy/data.csv',encoding='utf-8',newline='')as cs:
#with open('C:\\Users\\87778\\Desktop\\data.csv',encoding='utf-8',newline='')as cs:
#with open('C:\\Users\\87778\\transactions.csv', encoding='utf-8', newline='') as cs:
    reader=csv.reader(cs)
    # 循环遍历reader对象，
    noden=0
    for i in reader:
        if i:
            #print(i[5],i[6])
            gragh.run('MERGE (n1:user {name:$a})',a=i[5])
            gragh.run('MERGE (n2:user {name:$a})', a=i[6])
            #只记录关系
            #gragh.run('MATCH (a:user {name:$a}), (b:user {name:$b}) CREATE (a)-[:to1]->(b)',a=i[5],b=i[6])
            #记录关系和交易属性
            #gragh.run('MATCH (a:user {name:$a}), (b:user {name:$b}) CREATE (a)-[:to1 {hash:$w1,block_number:$w2,transaction_index:$w3}]->(b)', w1=i[0], w2=i[3], w3=i[4], a=i[5], b=i[6])
            #记录区块信息
            gragh.run('MATCH (a:user {name:$a}), (b:user {name:$b}) CREATE (a)-[:to1]->(b)',a=i[5], b=i[6])
            gragh.run('MERGE (a:tx {name:$a+$d+$c,hash:$b})', a=i[4], b=i[0],c=i[3],d='_')
            gragh.run('MATCH (a:tx {name:$a}), (b:user {name:$b}) CREATE (a)-[:is_tx]->(b)', a=i[4]+'_'+i[3], b=i[5])
            gragh.run('MATCH (a:tx {name:$a}), (b:user {name:$b}) CREATE (a)-[:is_tx]->(b)', a=i[4]+'_'+i[3], b=i[6])
            gragh.run('MERGE (a:block {name:$a})', a=i[3])
            gragh.run('MATCH (a:block {name:$a}), (b:tx {name:$b}) CREATE (a)-[:is_block]->(b)', a=i[3], b=i[4]+'_'+i[3])

            #记录矩阵
            G_weighted = nx.read_gml("1.gml")

            if i[5] not in G_weighted:
                G_weighted.add_node(i[5],iid=noden)
                noden=noden+1
            if i[6] not in G_weighted:
                G_weighted.add_node(i[6],iid=noden)
                noden =noden+1

            edge_to_check = (i[5], i[6])
            if G_weighted.has_edge(*edge_to_check):
                G_weighted[edge_to_check[0]][edge_to_check[1]]['weight'] += 1
            else:
                G_weighted.add_edge(*edge_to_check, weight=1)
            nx.write_gml(G_weighted, "1.gml")

print('build!')

### 打开文件
#f = open("C:\\Users\\87778\\Desktop\\data.csv",encoding='utf-8')
#lines = f.read()
#print(lines)
#f.close()

### CQL
#gragh = Graph('bolt://localhost:7687', auth = ('neo4j', '12345678'))
#matcher=NodeMatcher(gragh)
#a = Node("hero", name="Clint")  # Node(label, name)
#b = Node("hero", name="Natasha")
#gragh.create(Relationship(b,"belongsto",a))
#gragh.run('MATCH (n:hero{name:\'Natasha\'}) delete n;')


