from web3 import Web3
from solcx import compile_standard, install_solc
import json 
from View.state import GlobalState

class PublicContractModel:    
    w3 = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))

#establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        c = PublicContractModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c

 # deploy the node smart contract
    def deployPublicContract():

        ## Windows - ../contract/compiled_code.json
        ## Linux - contract/compiled_code.json
        with open(r"contract/compiled_code.json","r") as file:
            compiled_sol = json.loads(file.read())
           
        # get bytecode
        bytecode = compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["PublicContract.sol"]["PublicContract"]["metadata"])["output"]["abi"]
        GlobalState.PUBLIC_CONTRACT_ABI=abi

        w3 = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))

        chain_id = GlobalState.CHAIN_ID
        
        address = GlobalState.PUBLIC_CONTRACT_OWNER_PUBLIC_KEY
        # leaving the private key like this is very insecure if you are working on real world project
        private_key = GlobalState.PUBLIC_CONTRACT_OWNER_PRIVATE_KEY
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
        print("Gas",transaction_receipt["gasUsed"])
        print(f"Done! Public Contract deployed to {transaction_receipt.contractAddress}")
        #setting my contract address to deployed address  
        return 
    
    #get a contract address if already registered
    def getContractAddressFromPublicKey(owner_addr,private_addr):
        c= PublicContractModel.connection(GlobalState.PUBLIC_CONTRACT_ABI,GlobalState.PUBLIC_CONTRACT_ADDRESS,owner_addr,private_addr)
        print(owner_addr,"Checking contracts for ",GlobalState.PUBLIC_CONTRACT_ADDRESS)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        contract = c.caller({"from": owner_addr, "nonce": nonce}).getContractAddressByPublicAddress(owner_addr)
       
        print("Contract retrieved")
        print("Contract:", contract)
        return contract
#check the username is exists 
    def checkUserNameExist(userName,owner_addr,private_addr):
        c= PublicContractModel.connection(GlobalState.PUBLIC_CONTRACT_ABI,GlobalState.PUBLIC_CONTRACT_ADDRESS,owner_addr,private_addr)
        print(owner_addr,"checking user name validity for ",GlobalState.PUBLIC_CONTRACT_ADDRESS)
        nonce = PublicContractModel.w3.eth.getTransactionCount(owner_addr)
        result = c.caller({"from": owner_addr,"nonce":nonce}).isExists(userName)
        print("UserName  checked")
        print("Value:", result)
        return result
# PublicContractModel.deployPublicContract()
#PublicContractModel.getContractAddressFromPublicKey(owner_addr=PublicContractModel.defaultPublicAddress,private_addr=PublicContractModel.defaultPrivateAddress)