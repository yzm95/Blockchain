import csv
from web3 import Web3
import time

# 连接到以太坊节点
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/f9d3e9199a624558b362677847e18f36'))

# 设置要查询的区块高度范围
start_block = 11000101
end_block = 11000200

# 创建 CSV 文件并写入表头
with open('ethereum_transactions1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Block Number', 'Block Hash', 'Transaction Hash', 'Transaction Index', 'From', 'To', 'Value (Wei)', 'Gas', 'Gas Price', 'Nonce', 'Input Data', 'Type', 'V', 'R', 'S'])
    start_time=time.time()
    # 循环遍历每个区块，获取其中的交易
    for block_number in range(start_block, end_block + 1):
        print(block_number)
        block = web3.eth.get_block(block_number)
        if block:
            transactions = block['transactions']
            for tx_hash in transactions:
                # wo_time = time.time()
                # tim = wo_time - start_time
                # print("Execution time:", tim, "seconds")
                tx = web3.eth.get_transaction(tx_hash)
                writer.writerow([
                    block_number,
                    block['hash'].hex(),
                    tx_hash.hex(),
                    tx['transactionIndex'],
                    tx['from'],
                    tx['to'],
                    tx['value'],
                    tx['gas'],
                    tx['gasPrice'],
                    tx['nonce'],
                    tx['input'].hex(),
                    tx['type'],
                    tx['v'],
                    tx['r'].hex(),
                    tx['s'].hex()
                ])


print("数据已写入 ethereum_transactions.csv 文件。")

wo_time = time.time()
tim = wo_time - start_time
print("Execution time:", tim, "seconds")
