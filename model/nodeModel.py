#imports 
from web3 import Web3
from solcx import compile_standard, install_solc

#c = w3.eth.contract(address=myContractAddress, abi=myABI)
# publicContractAddress=""
class NodeModel:
    #node constants 
    myPrivateAddress=""
    myPublicAddress=""
    myContractAddress=""
    myABI=""
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

    # deploy the node smart contract
    def deploy(publicAddress,privateAddress):
        NodeModel.myPrivateAddress=privateAddress
        NodeModel.myPublicAddress=publicAddress
        # location for the contracts 
        with open(r"F:\Sadaru Kavisha\Semester 7\Fyp\Final Project\Social-Wallet-POC\contract\Node.sol","r") as file:
            node_file = file.read()

        with open(r"F:\Sadaru Kavisha\Semester 7\Fyp\Final Project\Social-Wallet-POC\contract\PublicContract.sol","r") as file:
            public_contract_file = file.read()

        import json  # to save the output in a JSON file
        install_solc("0.8.0")

        compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "Node.sol": {"content": node_file},
                    "PublicContract.sol":{"content":public_contract_file}
                },
                "settings": {
                    "outputSelection": {
                        "*": {
                            # output needed to interact with and deploy contract
                            "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                        }
                    }
                },
            },
            solc_version="0.8.17",
        )
        # print(compiled_sol)     #compiled solidity file 
        with open("compiled_code.json", "w") as file:
            json.dump(compiled_sol, file)


        # get bytecode
        bytecode = compiled_sol["contracts"]["Node.sol"]["Node"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["Node.sol"]
                        ["Node"]["metadata"])["output"]["abi"]
        NodeModel.myABI=abi

        # For connecting to ganache
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        chain_id = 1337
        address = publicAddress
        # leaving the private key like this is very insecure if you are working on real world project
        private_key = privateAddress
        # Create the contract in Python
        ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
        # Get the number of latest transaction
        nonce = w3.eth.getTransactionCount(address)


        # build transaction
        transaction = ContactList.constructor().buildTransaction(
            {
                "chainId": chain_id,
                "gasPrice": w3.eth.gas_price,
                "from": address,
                "nonce": nonce,
            }
        )
        # Sign the transaction
        sign_transaction = w3.eth.account.sign_transaction(
            transaction, private_key=private_key)
        print("Deploying Contract!")
        # Send the transaction
        transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        # Wait for the transaction to be mined, and get the transaction receipt
        print("Waiting for transaction to finish...")
        transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
        print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")

        #setting my contract address to deployed address  
        NodeModel.myContractAddress=transaction_receipt.contractAddress
        return 
    
    #establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        NodeModel.myABI=abi
        NodeModel.myContractAddress=contract_addr
        NodeModel.myPublicAddress=owner_addr
        NodeModel.myPrivateAddress=p_key
        #abi = "[ { \"inputs\": [ { \"internalType\": \"uint256[]\", \"name\": \"share_value\", \"type\": \"uint256[]\" } ], \"name\": \"add_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [], \"name\": \"give_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [ { \"internalType\": \"address\", \"name\": \"to\", \"type\": \"address\" } ], \"name\": \"set_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [ { \"internalType\": \"string\", \"name\": \"value_str\", \"type\": \"string\" } ], \"name\": \"store_hash\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"constructor\" }, { \"inputs\": [], \"name\": \"get\", \"outputs\": [ { \"internalType\": \"uint256[]\", \"name\": \"\", \"type\": \"uint256[]\" } ], \"stateMutability\": \"view\", \"type\": \"function\" }, { \"inputs\": [], \"name\": \"return_hash\", \"outputs\": [ { \"internalType\": \"string\", \"name\": \"\", \"type\": \"string\" } ], \"stateMutability\": \"view\", \"type\": \"function\" } ]"
        # contract_addr='0x2e169D7e39789D1a0d47EeD58A140D78A1D9B39d'
        # owner_addr='0x3Efdd722056D61C7A77619e2D556927a5467D30D'
        # p_key='a0809ede87de80864e3aaad330d8ae0129a454c9c16000003e1ddc80df960cf3'
        c = NodeModel.w3.eth.contract(address=NodeModel.myContractAddress, abi=NodeModel.myABI)
        return c

    def registerToPublicContract(userName):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,NodeModel.myPublicAddress,NodeModel.myPrivateAddress)

        nonce = NodeModel.w3.eth.getTransactionCount(NodeModel.myPublicAddress)
        store_contact = c.functions.registerToPublicContract(userName).buildTransaction({"from": NodeModel.myPublicAddress, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(store_contact, private_key=NodeModel.myPrivateAddress)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("Successfully registered to the public contract",transaction_receipt)
        return



    #sending the shares to the smart contract
    def send_shares_smartContact(shares):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,NodeModel.myPublicAddress,NodeModel.myPrivateAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(NodeModel.myPublicAddress)
        store_contact = c.functions.add_share(shares).buildTransaction({"from": NodeModel.myPublicAddress, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact =NodeModel. w3.eth.account.sign_transaction(store_contact, private_key=NodeModel.myPrivateAddress)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("shares send to the smart contract")

    #set the hash value in the smart contract
    def set_hash(hash_str):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,NodeModel.myPublicAddress,NodeModel.myPrivateAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(NodeModel.myPublicAddress)
        store_contact = c.functions.store_hash(hash_str).buildTransaction({"from": NodeModel.myPublicAddress, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(store_contact, private_key=NodeModel.myPrivateAddress)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("Hash send to the smart contract")

    #request shares from the smart contract
    def get_shares():
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,NodeModel.myPublicAddress,NodeModel.myPrivateAddress)
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


        

        


