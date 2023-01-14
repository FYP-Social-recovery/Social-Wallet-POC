#imports 
from web3 import Web3
from solcx import compile_standard, install_solc
import json 
#c = w3.eth.contract(address=myContractAddress, abi=myABI)
# publicContractAddress=""
class NodeModel:
    #node constants 
    myPrivateAddress="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"
    myPublicAddress="0x20543FD8D854d500121215Abc542531987f6bc2e"
    myContractAddress="0x1B3b0D351016cFE455b95D7EE747b1948A6b170b"
    publicContractABI='[ { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "acceptedShareHolderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "checkRequestsByShareholder", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "checkRequestsForTheSeceret", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "getContractAddressByName", "outputs": [ { "components": [ { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "contractAddress", "type": "address" } ], "internalType": "struct PublicContract.SampleNode", "name": "", "type": "tuple" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "publicAddress", "type": "address" } ], "name": "getContractAddressByPublicAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestAcceptedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestRejectedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInAcceptedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInRejectedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "getSecretOwnerAddressesCountInHolderRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "getSecretOwnerAddressesCountInSecretRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "holderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "isExists", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" } ], "name": "makeARequestToBeAShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "requesterAddress", "type": "address" } ], "name": "makeARequestToGetShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "makeSharesAccessibleToTheHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "myAddressToContractAddressMap", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "myContractAddress", "type": "address" } ], "name": "register", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "rejectedShareHolderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "releaseTheSecret", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "removeFromHolderRequestList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "shareHolder", "type": "address" }, { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "bool", "name": "acceptance", "type": "bool" } ], "name": "respondToBeShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" } ], "name": "sampleNodesMap", "outputs": [ { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "contractAddress", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "secretRequests", "outputs": [ { "internalType": "address", "name": "requesterAddress", "type": "address" }, { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "stateMutability": "view", "type": "function" } ]'
    myABI='[ { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "acceptInvitation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string[]", "name": "myShares", "type": "string[]" } ], "name": "addMyShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "shareHolder", "type": "address" } ], "name": "addTemporaryShareHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "checkAcceptance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "checkRequestsForBeAHolder", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "checkRequestsForShare", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "distribute", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getMyShares", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMyState", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getRejectedShareHolders", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getRequestedShareHolders", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getShareHolders", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "isRegistered", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "tempUserName", "type": "string" } ], "name": "isUserNameExist", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "makeShareHoldersListToDistribute", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "makingHolderRequests", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "myContractAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "myState", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "regenerate", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "regeneratedShares", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "registerToPublicContract", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "rejectInvitation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "rejectedShareHolders", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwnerAddress", "type": "address" } ], "name": "releaseSecret", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "remove", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "shareHolder", "type": "address" } ], "name": "removeShareHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "requestSharesFromHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "requestedShareHolders", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "share", "type": "string" } ], "name": "saveToRegeneratedShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "secretOwners", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "shareHolders", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "shareHoldersMap", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "shares", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "sharesMap", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "takeTheSecretFromTheOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "userName", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" } ]'
    #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/8L-St1WDAiIktazEqEolQfntGghuPR94"))
    


 # deploy the node smart contract
    def deployPublicContract():
        publicContractPrivateAddress="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"
        publicContractPublicAddress="0x20543FD8D854d500121215Abc542531987f6bc2e"

        with open(r"contract/compiled_code.json","r") as file:
            compiled_sol = json.loads(file.read())
           
        # get bytecode
        bytecode = compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["metadata"])["output"]["abi"]
        NodeModel.publicContractABI=abi

        # For connecting to ganache
        #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/8L-St1WDAiIktazEqEolQfntGghuPR94"))
        chain_id = 5
        #chain_id =1337
        address = publicContractPublicAddress
        # leaving the private key like this is very insecure if you are working on real world project
        private_key = publicContractPrivateAddress
        # Create the contract in Python
        ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
        # Get the number of latest transaction
        nonce = w3.eth.getTransactionCount(address)


        # build transaction
        transaction = ContactList.constructor().buildTransaction(
            {
                "chainId": chain_id,
                #"gasPrice": w3.eth.gas_price,
                "from": address,
                "nonce": nonce,
            }
        )
        # Sign the transaction
        sign_transaction = w3.eth.account.sign_transaction(
            transaction, private_key=private_key)
        print("Deploying public Contract !")
        # Send the transaction
        transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        # Wait for the transaction to be mined, and get the transaction receipt
        print("Waiting for transaction to finish...")
        transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
        print(f"Done! Public Contract deployed to {transaction_receipt.contractAddress}")
        #setting my contract address to deployed address  
        return 
    # deploy the node smart contract
    def deploy(publicAddress,privateAddress):
        NodeModel.myPrivateAddress=privateAddress
        NodeModel.myPublicAddress=publicAddress

        with open(r"contract/compiled_code.json","r") as file:
            compiled_sol = json.loads(file.read())

        # get bytecode
        bytecode = compiled_sol["contracts"]["Node.sol"]["Node"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["Node.sol"]["Node"]["metadata"])["output"]["abi"]
        NodeModel.myABI=abi

        # For connecting to ganache
        #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/8L-St1WDAiIktazEqEolQfntGghuPR94"))
        chain_id = 5
        #chain_id =1337
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
                #"gasPrice": w3.eth.gas_price,
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
        return transaction_receipt.contractAddress
    
    #establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        c = NodeModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c
#check the username is exists 
    def checkUserNameExist(userName,owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking user name validity for ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        result = c.caller({"from": owner_addr,"nonce":nonce}).isUserNameExist(userName)
        print("UserName  checked")
        print("Value:", result)
        return result
#register to the public contract
    def registerToPublicContract(userName,owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Registering for ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        store_contact = c.functions.registerToPublicContract(userName).buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(store_contact, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("Successfully registered to the public contract!!")
        return
#Share holder's role ----------------------------------------------------------------------

#check the requests for be a holder 
    def checkRequestsForBeAHolder(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Requests for ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        ownersList = c.caller({"from": owner_addr, "nonce": nonce}).checkRequestsForBeAHolder()
       
        print("Addresses retrieved")
        print("OwnersList:", ownersList)
        return ownersList
     
#accept the holder request
    def acceptInvitation(owner_addr,private_addr,share_owner):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Accepting Request ",share_owner)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.acceptInvitation(share_owner).buildTransaction({"from": owner_addr, "nonce": nonce})
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
     


# reject the holder request 
    def rejectInvitation(owner_addr,private_addr,share_owner):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Rejecting Request ",share_owner)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.rejectInvitation(share_owner).buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  rejected",status)
        
        return status

#check the share requests from me
    def checkRequestsForShare(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Share requests ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        ownersList = c.caller({"from": owner_addr, "nonce": nonce}).checkRequestsForShare()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("OwnersList:", ownersList)
        return ownersList
     
# release the secret
    def releaseSecret(owner_addr,private_addr,share_owner):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Releasing the secret of  ",share_owner)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.releaseSecret(share_owner).buildTransaction({"from": owner_addr,  "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  released",status)
        
        return status

#secret owner's role ----------------------------------------------------------------------------

# add a temporary share holder
    def addTemporaryShareHolder(owner_addr,private_addr,share_holder):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Adding as a share holder  ",share_holder)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.addTemporaryShareHolders(share_holder).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples

        print("Successfully  added",status)
        
        return status
#remove a temporary share holder
    def removeTemporaryShareHolder(owner_addr,private_addr,share_holder):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Removing as a share holder  ",share_holder)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.removeShareHolders(share_holder).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  removed",status)
        
        return status
# Make holder requests
    def makeHolderRequests(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Requesting from the Temporary holders  ")
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.makingHolderRequests().buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  requested from the temporary holders",status)
        
        return status
# add my shares
    def addMyShares(owner_addr,private_addr,shares):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Adding shares  ",shares)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.addMyShares(shares).buildTransaction({"from": owner_addr,  "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  added shares",status)
        
        return status
#Get my shares 
    def getMyShares(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Getting my shares  ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.caller({"from": owner_addr,"nonce": nonce}).getMyShares()
        #generate a list of tuples
        print("My shares  retrieved",returnVal)
        return returnVal

#get requested share holders list
    def getRequestedShareHolders(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getRequestedShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("Requested holdersList:", holdersList)
        return holdersList
#get My share holders who accepted the invitation
    def getMyShareHolders(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("accepted holdersList:", holdersList)
        return holdersList
#get rejected share holders
    def getRejectedShareHolders(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getRejectedShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("Rejected holdersList:", holdersList)
        return holdersList
#refresh the share holders status
    def refreshShareHoldersLists(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Refreshing statue of Share holders ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.makeShareHoldersListToDistribute().buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Refreshed Status")
        print("Accepted status:", status)
        return status
    
#Get the acceptance of the shareholders 
    def distributeShares(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Distributing the shares ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.distribute().buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)

        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Shares distributed:", status)
        return status
     
 #Request shares from holders 
    def requestShares(owner_addr,private_addr,user_name):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Requesting the shares ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.requestSharesFromHolders(user_name).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeModel.w3.eth.wait_for_transaction_receipt(send_store_contact)

        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Shares requested:", status)
        return status
     
#Get received shares 
    def getReceivedShares(owner_addr,private_addr):
        c= NodeModel.connection(NodeModel.myABI,NodeModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Getting received shares  ",NodeModel.myContractAddress)
        nonce = NodeModel.w3.eth.getTransactionCount(owner_addr)
        sharesList = c.caller({"from": owner_addr, "nonce": nonce}).regenerate()
       
        print("Received shares  retrieved")
        print("Shares List:", sharesList)
        return sharesList

 


#NodeModel.deployPublicContract()
#NodeModel.refreshShareHoldersLists(owner_addr=NodeModel.myPublicAddress,private_addr=NodeModel.myPrivateAddress)