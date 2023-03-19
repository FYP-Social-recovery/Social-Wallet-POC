from web3 import Web3
from solcx import compile_standard, install_solc
import json 

class PublicContractModel:
    # defaultPrivateAddress="2c3d8f882cd9737a228c292c2c5e21d3aec076b022743907107738b62d6e913c"
    # defaultPublicAddress="0x82e76bfC3c320872e3EAe1e7905d30d7dF9871C4"
    defaultContractAddress="0x4D44b83BDf61DCE0BAac6a81C6FC1c1b34726E53"

    publicContractABI='[ { "inputs": [ { "internalType": "address", "name": "requseterAddress", "type": "address" }, { "internalType": "address", "name": "secretOwnerAddress", "type": "address" } ], "name": "deleteShareRequest", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestAcceptedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" } ], "name": "getRequestRejectedHoldersList", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" } ], "name": "makeARequestToBeAShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "requesterAddress", "type": "address" }, { "internalType": "string", "name": "tempOtp", "type": "string" } ], "name": "makeARequestToGetShares", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "holder", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "makeSharesAccessibleToTheHolders", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "myContractAddress", "type": "address" } ], "name": "register", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "string", "name": "sharedString", "type": "string" } ], "name": "releaseTheSecret", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "removeFromHolderRequestList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "shareHolder", "type": "address" }, { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "bool", "name": "acceptance", "type": "bool" } ], "name": "respondToBeShareHolder", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "secretOwner", "type": "address" }, { "internalType": "address", "name": "shareHolder", "type": "address" } ], "name": "updateOwnersAcceptedToReleaseList", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "checkRequestsByShareholder", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "checkRequestsForTheSeceret", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "getContractAddressByName", "outputs": [ { "components": [ { "internalType": "address", "name": "publicAddress", "type": "address" }, { "internalType": "address", "name": "contractAddress", "type": "address" } ], "internalType": "struct PublicContract.SampleNode", "name": "", "type": "tuple" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "publicAddress", "type": "address" } ], "name": "getContractAddressByPublicAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInAcceptedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "ownerAddress", "type": "address" } ], "name": "getSecretHolderAddressesCountInRejectedHoldersList", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "holderAddress", "type": "address" } ], "name": "getSecretOwnerAddressesCountInHolderRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "secretOwners", "type": "address[]" } ], "name": "getSecretOwnerAddressesCountInSecretRequests", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "isExists", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "string", "name": "tempOtp", "type": "string" } ], "name": "makeARequestToGetVaultHash", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" } ]'
    
    #w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/8L-St1WDAiIktazEqEolQfntGghuPR94"))
    #w3 = Web3(Web3.HTTPProvider("https://goerli-rollup.arbitrum.io/rpc"))
    w3 = Web3(Web3.HTTPProvider("https://arb-goerli.g.alchemy.com/v2/kmaQkTzL0jVfzpP6t9J1R04Y0hr9GGJE"))

#establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        c = PublicContractModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c

 # deploy the node smart contract
    def deployPublicContract():
        publicContractPrivateAddress="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"
        publicContractPublicAddress="0x20543FD8D854d500121215Abc542531987f6bc2e"
        # publicContractPrivateAddress="df18cf870137180f32fcfbd1da5df9b209427fadd82f3b7e8be3de714cdd980b"
        # publicContractPublicAddress="0xD0687c7Ce118c622e7351CDaA0a919315cA5E464"

        with open(r"contract/compiled_code.json","r") as file:
            compiled_sol = json.loads(file.read())
           
        # get bytecode
        bytecode = compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["metadata"])["output"]["abi"]
        PublicContractModel.publicContractABI=abi

        # For connecting to ganache
        #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        #w3 = Web3(Web3.HTTPProvider("https://goerli-rollup.arbitrum.io/rpc"))
        w3 = Web3(Web3.HTTPProvider("https://arb-goerli.g.alchemy.com/v2/kmaQkTzL0jVfzpP6t9J1R04Y0hr9GGJE"))
        chain_id=421613
        #chain_id = 5
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
        print("Gas",transaction_receipt["gasUsed"]/10000000000)
        print(f"Done! Public Contract deployed to {transaction_receipt.contractAddress}")
        #setting my contract address to deployed address  
        return 
    
    #get a contract address if already registered
    def getContractAddressFromPublicKey(owner_addr,private_addr):
        c= PublicContractModel.connection(PublicContractModel.publicContractABI,PublicContractModel.defaultContractAddress,owner_addr,private_addr)
        print(owner_addr,"Checking contracts for ",PublicContractModel.defaultContractAddress)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        contract = c.caller({"from": owner_addr, "nonce": nonce}).getContractAddressByPublicAddress(owner_addr)
       
        print("Contract retrieved")
        print("Contract:", contract)
        return contract
#check the username is exists 
    def checkUserNameExist(userName,owner_addr,private_addr):
        c= PublicContractModel.connection(PublicContractModel.publicContractABI,PublicContractModel.defaultContractAddress,owner_addr,private_addr)
        print(owner_addr,"checking user name validity for ",PublicContractModel.defaultContractAddress)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        result = c.caller({"from": owner_addr,"nonce":nonce}).isExists(userName)
        print("UserName  checked")
        print("Value:", result)
        return result
#PublicContractModel.deployPublicContract()
#PublicContractModel.getContractAddressFromPublicKey(owner_addr=PublicContractModel.defaultPublicAddress,private_addr=PublicContractModel.defaultPrivateAddress)