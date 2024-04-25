from eth_hash.auto import keccak
import rlp
from web3 import Web3
import csv
import time

def hash_transaction(tx):
    tx_list = [
        int(row[9]),
        int(row[8]),
        int(row[7]),
        bytes.fromhex(row[5][2:]),
        int(row[6]),
        bytes.fromhex(row[10][2:]),  # 将 HexBytes 对象转换为十六进制字符串，然后转换为字节串
        int(row[12]),
        bytes.fromhex(row[13][2:]),  # 将 HexBytes 对象转换为十六进制字符串，然后转换为字节串
        bytes.fromhex(row[14][2:])  # 将 HexBytes 对象转换为十六进制字符串，然后转换为字节串
    ]
    # print("Transaction list:")
    # for i, item in enumerate(tx_list):
    #     print(f"Element {i}: {item}")
    # print(tx_list)
    encoded_tx = rlp.encode(tx_list)
    return keccak(encoded_tx)
time1 =time.time()
for _ in range(1):
    with open('E:\\code\\jiaoben\\py333new\\ethereum_transactions.csv', encoding='utf-8', newline='') as cs:
        reader = csv.reader(cs)
        next(reader)
        # line_number = 1
        for row in reader:
            if row:
                # print(line_number)
                # line_number=line_number+1
                # print(row[9],row[8],row[7],row[5],row[6],row[10],row[12],row[13],row[14])
                # print(row[2])
                if row[5] != '' and row[6] != '' and row[5] != row[6]:
                    tx_hash = hash_transaction(row)
                    # print('算的 ' + tx_hash.hex())
                    if '0x'+str(tx_hash.hex()) == row[2]:
                        print('yes')

time2 =time.time()
time=time2-time1
print(time)

