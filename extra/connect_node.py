from web3 import Web3, HTTPProvider, eth
import os

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/1fc68c46033b44299103faef4618b10d'))
w3.eth.account = "0xfd1F3BF4f8349b197a6583694418C947D6BE1BC1"


false = False
true = True

ABI = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"addPupilEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"editPupilEvent","type":"event"},{"inputs":[{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"name":"addPupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"},{"internalType":"bool","name":"_blackList","type":"bool"}],"name":"deletePupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllPupils","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllPupilsAddress","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"}],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pupilsCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]

my_contract = w3.eth.contract(
    # Адрес контракте в сети
    address = '0xb1FD213410D463a8362333c5d0630105b7E20DA9',
    abi = ABI
)

transaction = my_contract.functions.addPupil("MOYA KOMANDA", "George", "4").buildTransaction({
    'chainId': 3, # идентификатор сети(mainnet, ropsten, goerli и так далее) 3 - ropsten
    'gas': 300000, # лимит газа
    'gasPrice': w3.eth.gasPrice, # конвертация газа в wei(тариф)
    'nonce': w3.eth.getTransactionCount(w3.eth.account), # соль для транзакции
    'value': 0 # какое количество денег мы передаем
})
# Ваш закрытый ключ для подписании транзакции
closedKey = "08a07910fbbbe50c0222b91c078627257db9b44b46cba52916e53f98ebde05c4"
# Подписываем транзакцию
sign_txt = eth.Account.sign_transaction(transaction, closedKey)
# Выполняем транзакцию и сохраняем её хэш
transaction_hash = w3.eth.sendRawTransaction(sign_txt.rawTransaction)
# получить атрибуты транзакции
transaction_attribute = w3.eth.get_transaction(transaction_hash)
# вывести атрибуты транзакции
print(transaction_attribute)
