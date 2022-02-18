import solc as solc
import solcx
from web3 import Web3, HTTPProvider, eth
import os
from solcx import compile_source


w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/1fc68c46033b44299103faef4618b10d'))

w3.eth.account = "0xfd1F3BF4f8349b197a6583694418C947D6BE1BC1"
closedKey = "08a07910fbbbe50c0222b91c078627257db9b44b46cba52916e53f98ebde05c4"

# Скомпилровать контракт
source = open("TestContract.sol").read()
compiled_sol = compile_source(source, output_values=["abi", "bin"])

# Получить интерфейс скомпилированного контракта
contract_id, contract_interface = compiled_sol.popitem()

# Создать экземпляр контракта
TestContract = w3.eth.contract(
    abi=contract_interface["abi"],
    bytecode=contract_interface["bin"]
)

# Создать объект транзакции
transaction = {
    # эти три поля обязательны - остальные можно прописать по желанию,
    # либо они примут значения по умолчанию
    'from': w3.eth.account,
    'nonce': w3.eth.getTransactionCount(w3.eth.account),
    'chainId': 3
}
deploy_transaction = TestContract.constructor("Gosh", 2003).buildTransaction(transaction)

# Подписываем транзакцию
sign_txt = eth.Account.sign_transaction(deploy_transaction, private_key=closedKey)

# Отправляем транзакцию в сеть и сохраняем её хеш
transaction_hash = w3.eth.send_raw_transaction(sign_txt.rawTransaction)

# Ждём выполнение транзакции
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

# Выводим результат выполнения транзакции
print(transaction_receipt)