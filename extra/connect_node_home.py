from web3 import Web3, HTTPProvider, eth
import os

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/1fc68c46033b44299103faef4618b10d'))

persons_adress = input()
block_start = input()
block_end = input()

person_trans_list = []

for i in range(block_start, block_end + 1):
    block_trans = w3.eth.get_block(i)['transactions']
    for trans in block_trans:
        trans_info = w3.eth.get_transaction(trans)
        if trans_info['from'] == persons_adress or trans_info['to'] == persons_adress:
            person_trans_list.append(trans_info['hash'])
