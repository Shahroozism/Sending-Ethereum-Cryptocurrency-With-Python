import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/9549dc6e7edb45469d57d8d8d5c78ef8"
web3 = Web3(Web3.HTTPProvider(infura_url))


abi = json.loads()

#BNB Abi

abi = json.loads()

#BNB Address
address = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"

contract = web3.eth.contract(address=address,abi=abi)

totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply,'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())


#random BNB holder

balance = contract.functions.balanceOf('').call()
print(web3.fromWei(balance, 'ether'))