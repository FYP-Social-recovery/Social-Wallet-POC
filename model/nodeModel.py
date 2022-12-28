#imports 
from web3 import Web3
from solcx import compile_standard, install_solc

#c = w3.eth.contract(address=myContractAddress, abi=myABI)
# publicContractAddress=""
class NodeModel:
    #node constants 
    myPrivateAddress="8dbfc464a00316c6adf2b09775c12f0e23b570bd51a6babbc5214386dde3911b"
    myPublicAddress="0x4dAD3EDcA924D144464E623DBd158D23e66B4575"
    myContractAddress="0xa8356aBA19f43B4875F8380274d163D125dB7554"
    myABI='[ { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "acceptInvitation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string[]", "name": "myShares", "type": "string[]" } ], "name": "addMyShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "shareHolder", "type": "address" } ], "name": "addTemporaryShareHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "distribute", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "makeShareHoldersListToDistribute", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "makingHolderRequests", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "registerToPublicContract", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "rejectInvitation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwnerAddress", "type": "address" } ], "name": "releaseSecret", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "remove", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "shareHolder", "type": "address" } ], "name": "removeShareHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "repayGasFee", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "requestSharesFromHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "share", "type": "string" } ], "name": "saveToRegeneratedShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "takeTheSecretFromTheOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "checkRequestsForBeAHolder", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "checkRequestsForShare", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMyShares", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getShareHolders", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "isRegistered", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "myContractAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "regenerate", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "regeneratedShares", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "requestedShareHolders", "outputs": [ { "internalType": "address payable", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "secretOwners", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "shareHolders", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "shareHoldersMap", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "shares", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "sharesMap", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "userName", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" } ]'
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
        abi = json.loads(compiled_sol["contracts"]["Node.sol"]["Node"]["metadata"])["output"]["abi"]
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
        # NodeModel.myABI=abi
        # NodeModel.myContractAddress=contract_addr
        # NodeModel.myPublicAddress=owner_addr
        # NodeModel.myPrivateAddress=p_key

        #abi = "[ { \"inputs\": [ { \"internalType\": \"uint256[]\", \"name\": \"share_value\", \"type\": \"uint256[]\" } ], \"name\": \"add_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [], \"name\": \"give_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [ { \"internalType\": \"address\", \"name\": \"to\", \"type\": \"address\" } ], \"name\": \"set_share\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [ { \"internalType\": \"string\", \"name\": \"value_str\", \"type\": \"string\" } ], \"name\": \"store_hash\", \"outputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"function\" }, { \"inputs\": [], \"stateMutability\": \"nonpayable\", \"type\": \"constructor\" }, { \"inputs\": [], \"name\": \"get\", \"outputs\": [ { \"internalType\": \"uint256[]\", \"name\": \"\", \"type\": \"uint256[]\" } ], \"stateMutability\": \"view\", \"type\": \"function\" }, { \"inputs\": [], \"name\": \"return_hash\", \"outputs\": [ { \"internalType\": \"string\", \"name\": \"\", \"type\": \"string\" } ], \"stateMutability\": \"view\", \"type\": \"function\" } ]"
        # contract_addr='0x2e169D7e39789D1a0d47EeD58A140D78A1D9B39d'
        # owner_addr='0x3Efdd722056D61C7A77619e2D556927a5467D30D'
        # p_key='a0809ede87de80864e3aaad330d8ae0129a454c9c16000003e1ddc80df960cf3'
        c = NodeModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c

    def registerToPublicContract(userName,owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Registering for ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        store_contact = c.functions.registerToPublicContract(userName).buildTransaction({"from": owner_addr, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(store_contact, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("Successfully registered to the public contract!!")
        return
#Share holder's role ----------------------------------------------------------------------

    def checkRequestsForBeAHolder(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Requests for ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.checkRequestsForBeAHolder().buildTransaction({"from": owner_addr, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        OwnersList = transaction_receipt["contractAddress"]
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("OwnersList:", OwnersList)
        return OwnersList
     

    def acceptInvitation(owner_addr,private_addr,share_owner):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Accepting Request ",share_owner)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.acceptInvitation(share_owner).buildTransaction({"from": owner_addr, "gasPrice": NodeModel.w3.eth.gas_price, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  accepted",status)
        
        return status
     


        

        


