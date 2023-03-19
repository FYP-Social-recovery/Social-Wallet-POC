#imports 
from web3 import Web3
from solcx import compile_standard, install_solc
import json 
from View.state import GlobalState

class NodeContractModel:
    w3 = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))
    

    # deploy the node smart contract
    def deploy(publicAddress,privateAddress):
        # NodeContractModel.defaultPrivateAddress=privateAddress
        # NodeContractModel.defaultPublicAddress=publicAddress
        
        # with open(r"contract/compiled_code.json","r") as file: # for windows
        with open("../contract/compiled_code.json","r") as file: # for ubuntu
            compiled_sol = json.loads(file.read())

        # get bytecode
        bytecode = compiled_sol["contracts"]["Node.sol"]["Node"]["evm"]["bytecode"]["object"]
        # get abi
        abi = json.loads(compiled_sol["contracts"]["Node.sol"]["Node"]["metadata"])["output"]["abi"]
        GlobalState.NODE_CONTRACT_ABI=abi

        w3 = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))

        chain_id = GlobalState.CHAIN_ID
        
        address = publicAddress
        # leaving the private key like this is very insecure if you are working on real world project
        private_key = privateAddress
        # Create the contract in Python
        ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
        # Get the number of latest transaction
        nonce = w3.eth.getTransactionCount(address)


        # build transaction
        transaction = ContactList.constructor(GlobalState.PUBLIC_CONTRACT_ADDRESS).buildTransaction(
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
        GlobalState.NODE_CONTRACT_ADDRESS=transaction_receipt.contractAddress
        return transaction_receipt.contractAddress
    
    #establish the connection to call the smart contract functions 
    def connection(abi,contract_addr,owner_addr,p_key):
        c = NodeContractModel.w3.eth.contract(address=contract_addr, abi=abi)
        return c
#check the username is exists 
    def checkUserNameExist(userName,owner_addr,private_addr):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,GlobalState.NODE_CONTRACT_ADDRESS,owner_addr,private_addr)
        print(owner_addr,"checking user name validity for ",GlobalState.NODE_CONTRACT_ADDRESS)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        result = c.caller({"from": owner_addr,"nonce":nonce}).isUserNameExist(userName)
        print("UserName  checked")
        print("Value:", result)
        return result
#register to the public contract
    def registerToPublicContract(userName,owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Registering for ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        store_contact = c.functions.registerToPublicContract(userName).buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(store_contact, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        print("Successfully registered to the public contract!!")
        return
#Share holder's role ----------------------------------------------------------------------

#check the requests for be a holder 
    def checkRequestsForBeAHolder(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"checking Requests for ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        ownersList = c.caller({"from": owner_addr, "nonce": nonce}).checkRequestsForBeAHolder()
       
        print("Addresses retrieved")
        print("OwnersList:", ownersList)
        return ownersList
     
#accept the holder request
    def acceptInvitation(owner_addr,private_addr,share_owner,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Accepting Request ",share_owner)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.acceptInvitation(share_owner).buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  accepted",status)
        
        return status
     


# reject the holder request 
    def rejectInvitation(owner_addr,private_addr,share_owner,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Rejecting Request ",share_owner)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.rejectInvitation(share_owner).buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  rejected",status)
        
        return status

#check the share requests from me
    def checkRequestsForShare(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"checking Share requests ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        ownersList = c.caller({"from": owner_addr, "nonce": nonce}).checkRequestsForShare()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("OwnersList:", ownersList)
        return ownersList
     
# release the secret
    def releaseSecret(owner_addr,private_addr,share_owner,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Releasing the secret of  ",share_owner)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.releaseSecret(share_owner).buildTransaction({"from": owner_addr,  "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  released",status)
        
        return status

#secret owner's role ----------------------------------------------------------------------------

# add a temporary share holder
    def addTemporaryShareHolder(owner_addr,private_addr,share_holder,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Adding as a share holder  ",share_holder)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.addTemporaryShareHolders(share_holder).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples

        print("Successfully  added",status)
        
        return status
#remove a temporary share holder
    def removeTemporaryShareHolder(owner_addr,private_addr,share_holder,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Removing as a share holder  ",share_holder)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.removeShareHolders(share_holder).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  removed",status)
        
        return status
# Make holder requests
    def makeHolderRequests(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Requesting from the Temporary holders  ")
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.makingHolderRequests().buildTransaction({"from": owner_addr, "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  requested from the temporary holders",status)
        
        return status
# add my shares
    def addMyShares(owner_addr,private_addr,shares,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Adding shares  ",shares)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.addMyShares(shares).buildTransaction({"from": owner_addr,  "nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Successfully  added shares",status)
        
        return status
#Get my shares 
    def getMyShares(owner_addr,private_addr):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,GlobalState.NODE_CONTRACT_ADDRESS,owner_addr,private_addr)
        print(owner_addr,"Getting my shares  ",GlobalState.NODE_CONTRACT_ADDRESS)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.caller({"from": owner_addr,"nonce": nonce}).getMyShares()
        #generate a list of tuples
        print("My shares  retrieved",returnVal)
        return returnVal

#get requested share holders list
    def getRequestedShareHolders(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getRequestedShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("Requested holdersList:", holdersList)
        return holdersList
#get My share holders who accepted the invitation
    def getMyShareHolders(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("accepted holdersList:", holdersList)
        return holdersList
#get rejected share holders
    def getRejectedShareHolders(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"checking Share holders ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        holdersList = c.caller({"from": owner_addr, "nonce": nonce}).getRejectedShareHolders()
        #generate a list of tuples
       
        print("Addresses retrieved")
        print("Rejected holdersList:", holdersList)
        return holdersList
#refresh the share holders status
    def refreshShareHoldersLists(owner_addr,private_addr, nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Refreshing statue of Share holders ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.refreshHolderLists().buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Refreshed Holder Status")
        print("Accepted status:", status)
        return status

#refresh the share holders status
    def refreshStatus(owner_addr,private_addr, nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Refreshing status  ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.refreshState().buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)
        # returnVal = c.caller().checkRequestsForBeAHolder()
        # ownerAddressList = returnVal
        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Refreshed Status")
        print("Accepted status:", status)
        return status
#Get the acceptance of the shareholders 
    def distributeShares(owner_addr,private_addr, nodeContractAddressLocal,otp,vault):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Distributing the shares ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        #todo test the function 
        returnVal = c.functions.distribute(otp,vault).buildTransaction({"from": owner_addr, "nonce": nonce, "gasPrice": NodeContractModel.w3.eth.gas_price,})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)

        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Shares distributed:", status)
        return status
    
 #Request shares from holders 
    def requestShares(owner_addr,private_addr,user_name,otp, nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Requesting the shares ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        returnVal = c.functions.requestSharesFromHolders(user_name,otp).buildTransaction({"from": owner_addr,"nonce": nonce})
        # Sign the transaction
        sign_store_contact = NodeContractModel.w3.eth.account.sign_transaction(returnVal, private_key=private_addr)
        # Send the transaction
        send_store_contact = NodeContractModel.w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = NodeContractModel.w3.eth.wait_for_transaction_receipt(send_store_contact)

        status = transaction_receipt["status"]
        #generate a list of tuples
       
        print("Shares requested:", status)
        return status
     
#request vault hash by the third party 
    def requestVaultHash(owner_addr,private_addr,user_name,otp,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Requesting and getting vault hash  ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        vaultHash = c.caller({"from": owner_addr, "nonce": nonce}).requestVaultHashOfSecretOwner(user_name,otp)
       
        print("Vault hash  retrieved")
        print("vault hash:", vaultHash)
        return vaultHash

     
#Get received shares 
    def getReceivedShares(owner_addr,private_addr,nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Getting received shares  ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        sharesList = c.caller({"from": owner_addr, "nonce": nonce}).regenerate()
       
        print("Received shares  retrieved")
        print("Shares List:", sharesList)
        return sharesList

#get my state 
    def getMyState(owner_addr,private_addr, nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Getting my status  ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        myState = c.caller({"from": owner_addr, "nonce": nonce}).getMyState()
       
        print("My state  retrieved")
        print("State:", myState)
        return myState

#get contract address using public address 
    def getContractAddressOfPrivateAddress(owner_addr,private_addr):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,GlobalState.NODE_CONTRACT_ADDRESS,owner_addr,private_addr)
        print(owner_addr,"Getting my Contract Address  ",GlobalState.NODE_CONTRACT_ADDRESS)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        contractAddress = c.caller({"from": owner_addr, "nonce": nonce}).getContractAddressOfPublicAddress(owner_addr)
       
        print("My Contract Address  retrieved")
        print("Contract Address:", contractAddress)
        return contractAddress

#get contract address using public address 
    def getUserName(owner_addr,private_addr, nodeContractAddressLocal):
        c= NodeContractModel.connection(GlobalState.NODE_CONTRACT_ABI,nodeContractAddressLocal,owner_addr,private_addr)
        print(owner_addr,"Getting my userName  ",nodeContractAddressLocal)
        nonce = NodeContractModel.w3.eth.getTransactionCount(owner_addr)
        userName = c.caller({"from": owner_addr, "nonce": nonce}).getUserName()
       
        print("My user name  retrieved")
        print("Contract Address:", userName)
        return userName

