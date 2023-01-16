from web3 import Web3
from solcx import compile_standard, install_solc
import json 

class PublicContractModel:
    myPrivateAddress="2c3d8f882cd9737a228c292c2c5e21d3aec076b022743907107738b62d6e913c"
    myPublicAddress="0x82e76bfC3c320872e3EAe1e7905d30d7dF9871C4"
    myContractAddress="0x21b7180b01dE7f6029cD2bBF196008dD1AcD8d70"
    # TODO - change above 3 variable names to meaningfulll names
    
    publicContractABI='[ { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "acceptedShareHolderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "checkRequestsByShareholder", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "checkRequestsForTheSeceret", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "getContractAddressByName", "outputs": [ { "components": [ { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "contractAddress", "type": "address" } ], "internalType": "struct PublicContract.SampleNode", "name": "", "type": "tuple" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "publicAddress", "type": "address" } ], "name": "getContractAddressByPublicAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestAcceptedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestRejectedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInAcceptedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInRejectedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "getSecretOwnerAddressesCountInHolderRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "getSecretOwnerAddressesCountInSecretRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "holderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "isExists", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" } ], "name": "makeARequestToBeAShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "requesterAddress", "type": "address" } ], "name": "makeARequestToGetShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "makeSharesAccessibleToTheHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "myAddressToContractAddressMap", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "myContractAddress", "type": "address" } ], "name": "register", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "rejectedShareHolderRequests", "outputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "releaseTheSecret", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "removeFromHolderAcceptedList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "removeFromHolderRejectedList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "removeFromHolderRequestList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "shareHolder", "type": "address" }, { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "bool", "name": "acceptance", "type": "bool" } ], "name": "respondToBeShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" } ], "name": "sampleNodesMap", "outputs": [ { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "contractAddress", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "secretRequests", "outputs": [ { "internalType": "address", "name": "requesterAddress", "type": "address" }, { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "stateMutability": "view", "type": "function" } ]'
    
    w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/8L-St1WDAiIktazEqEolQfntGghuPR94"))

#establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        c = PublicContractModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c

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
        PublicContractModel.publicContractABI=abi

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
    
    #get a contract address if already registered
    def getContractAddressFromPublicKey(owner_addr,private_addr):
        c= PublicContractModel.connection(PublicContractModel.publicContractABI,PublicContractModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"Checking contracts for ",PublicContractModel.myContractAddress)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        contract = c.caller({"from": owner_addr, "nonce": nonce}).getContractAddressByPublicAddress(owner_addr)
       
        print("Contract retrieved")
        print("Contract:", contract)
        return contract
#check the username is exists 
    def checkUserNameExist(userName,owner_addr,private_addr):
        c= PublicContractModel.connection(PublicContractModel.publicContractABI,PublicContractModel.myContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking user name validity for ",PublicContractModel.myContractAddress)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        result = c.caller({"from": owner_addr,"nonce":nonce}).isExists(userName)
        print("UserName  checked")
        print("Value:", result)
        return result
#PublicContractModel.deployPublicContract()
#PublicContractModel.getContractAddressFromPublicKey(owner_addr=PublicContractModel.myPublicAddress,private_addr=PublicContractModel.myPrivateAddress)