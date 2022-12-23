from web3 import Web3
from solcx import compile_source
import solcx

compiled_sol =solcx.compile_files('Node.sol',output_values=['abi', 'bin'])
# Solidity source code
# compiled_sol = compile_source(    '''
# ...     pragma solidity >0.5.0;
# ...
# ...     contract Greeter {
# ...         string public greeting;
# ...
# ...         constructor() public {
# ...             greeting = 'Hello';
# ...         }
# ...
# ...         function setGreeting(string memory _greeting) public {
# ...             greeting = _greeting;
# ...         }
# ...
# ...         function greet() view public returns (string memory) {
# ...             return greeting;
# ...         }
# ...     }
# ...     ''',
# ...     output_values=['abi', 'bin']
# ... )

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)

greeter.functions.getMyShares().call()


tx_hash = greeter.functions.addMyShares(["share","share2"]).transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
greeter.functions.getMyShares().call()













#Tharinda's 
import web3
w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:7545'))
abi = '[ 	{ 		"inputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"name": "acceptedShareHolderRequests", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "shareHolder", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "holderAddress", 				"type": "address" 			} 		], 		"name": "checkRequestsByShareholder", 		"outputs": [ 			{ 				"internalType": "address[]", 				"name": "", 				"type": "address[]" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address[]", 				"name": "secretOwners", 				"type": "address[]" 			} 		], 		"name": "checkRequestsForTheSeceret", 		"outputs": [ 			{ 				"internalType": "address[]", 				"name": "", 				"type": "address[]" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			} 		], 		"name": "getContractAddressByName", 		"outputs": [ 			{ 				"components": [ 					{ 						"internalType": "address", 						"name": "publicAddress", 						"type": "address" 					}, 					{ 						"internalType": "address", 						"name": "contractAddress", 						"type": "address" 					} 				], 				"internalType": "struct PublicContract.SampleNode", 				"name": "", 				"type": "tuple" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "publicAddress", 				"type": "address" 			} 		], 		"name": "getContractAddressByPublicAddress", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			} 		], 		"name": "getRequestAcceptedHoldersList", 		"outputs": [ 			{ 				"internalType": "address[]", 				"name": "", 				"type": "address[]" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "ownerAddress", 				"type": "address" 			} 		], 		"name": "getSecretHolderAddressesCountInAcceptedHoldersList", 		"outputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "holderAddress", 				"type": "address" 			} 		], 		"name": "getSecretOwnerAddressesCountInHolderRequests", 		"outputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address[]", 				"name": "secretOwners", 				"type": "address[]" 			} 		], 		"name": "getSecretOwnerAddressesCountInSecretRequests", 		"outputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"name": "holderRequests", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "shareHolder", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			} 		], 		"name": "isExists", 		"outputs": [ 			{ 				"internalType": "bool", 				"name": "", 				"type": "bool" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "holder", 				"type": "address" 			} 		], 		"name": "makeARequestToBeAShareHolder", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			}, 			{ 				"internalType": "address", 				"name": "requesterAddress", 				"type": "address" 			} 		], 		"name": "makeARequestToGetShares", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "holder", 				"type": "address" 			}, 			{ 				"internalType": "string", 				"name": "sharedString", 				"type": "string" 			} 		], 		"name": "makeSharesAccessibleToTheHolders", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "", 				"type": "address" 			} 		], 		"name": "myAddressToContractAddressMap", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			} 		], 		"name": "regenerateSecret", 		"outputs": [ 			{ 				"internalType": "string[]", 				"name": "", 				"type": "string[]" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			}, 			{ 				"internalType": "address", 				"name": "publicAddress", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "myContractAddress", 				"type": "address" 			} 		], 		"name": "register", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"name": "rejectedShareHolderRequests", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "shareHolder", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "string", 				"name": "sharedString", 				"type": "string" 			} 		], 		"name": "releaseTheSecret", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "uint256", 				"name": "index", 				"type": "uint256" 			} 		], 		"name": "removeFromHolderRequestList", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "address", 				"name": "shareHolder", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "secretOwner", 				"type": "address" 			}, 			{ 				"internalType": "bool", 				"name": "acceptance", 				"type": "bool" 			} 		], 		"name": "respondToBeShareHolder", 		"outputs": [], 		"stateMutability": "nonpayable", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "string", 				"name": "", 				"type": "string" 			} 		], 		"name": "sampleNodesMap", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "publicAddress", 				"type": "address" 			}, 			{ 				"internalType": "address", 				"name": "contractAddress", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	}, 	{ 		"inputs": [ 			{ 				"internalType": "uint256", 				"name": "", 				"type": "uint256" 			} 		], 		"name": "secretRequests", 		"outputs": [ 			{ 				"internalType": "address", 				"name": "requesterAddress", 				"type": "address" 			}, 			{ 				"internalType": "string", 				"name": "name", 				"type": "string" 			}, 			{ 				"internalType": "address", 				"name": "ownerAddress", 				"type": "address" 			} 		], 		"stateMutability": "view", 		"type": "function" 	} ]'
contract_addr='0x9546d0D10300c566B5Ce0cd77d07A60DA95C34B8'
owner_addr='0x18Ee3313a8240Eb59c43e99C5C5d8477d19dFa40'
p_key='ff5052dc2b1a0e96852dbf73947fee5ded5e452b3d273aa0b96df94abd7060a0'
c = w3.eth.contract(address=contract_addr, abi=abi)

#sending the shares to the smart contract
def send_shares_smartContact(shares):
    nonce = w3.eth.getTransactionCount(owner_addr)
    store_contact = c.functions.add_share(shares).buildTransaction({"from": owner_addr, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    # Sign the transaction
    sign_store_contact = w3.eth.account.sign_transaction(store_contact, private_key=p_key)
    # Send the transaction
    send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
    print("shares send to the smart contract")

#set the hash value in the smart contract
def set_hash(hash_str):
    nonce = w3.eth.getTransactionCount(owner_addr)
    store_contact = c.functions.store_hash(hash_str).buildTransaction({"from": owner_addr, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    # Sign the transaction
    sign_store_contact = w3.eth.account.sign_transaction(store_contact, private_key=p_key)
    # Send the transaction
    send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
    print("Hash send to the smart contract")

#request shares from the smart contract
def get_shares():
    rtn = c.caller().get()
    share_list = rtn
    collected_shares = []
    #generate a list of tuples
    for i in range(0, len(share_list)-1, 2):
        temp_tuple = tuple((share_list[i], share_list[i+1]))
        collected_shares.append(temp_tuple)
    print("shares retrieved")
    print("collected_shares:", collected_shares)
    return collected_shares

