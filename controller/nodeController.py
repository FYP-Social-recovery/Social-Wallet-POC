from model.nodeModel import NodeContractModel


# nodeObject =nodeModel.NodeContractModel()
publicKey="0x20543FD8D854d500121215Abc542531987f6bc2e"
privateKey="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"

class NodeContractController:
    def deploy(publicKeyLocal, privateKeyLocal):
        contractAddress=NodeContractModel.deploy(publicAddress=publicKeyLocal,privateAddress=privateKeyLocal)
        return contractAddress

    def register(userName, publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        NodeContractModel.registerToPublicContract(userName,owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return

    #share holder Role  
    def checkRequestsForBeAHolder(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        addresses=NodeContractModel.checkRequestsForBeAHolder(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,nodeContractAddressLocal=nodeContractAddressLocal)
        return addresses

    def acceptInvitation(address,publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status=NodeContractModel.acceptInvitation(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,share_owner=address,nodeContractAddressLocal=nodeContractAddressLocal)
        return status
    def rejectInvitation(address,publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status=NodeContractModel.rejectInvitation(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,share_owner=address,nodeContractAddressLocal=nodeContractAddressLocal)
        return status
        
    def checkRequestsForShare(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        ownersList=NodeContractModel.checkRequestsForShare(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return ownersList

    def releaseShare(address,publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status=NodeContractModel.releaseSecret(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,share_owner=address,nodeContractAddressLocal=nodeContractAddressLocal)
        return status


    #secret owner's role 
    def addTemporaryShareHolder(share_holder, publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status =NodeContractModel.addTemporaryShareHolder(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,share_holder=share_holder, nodeContractAddressLocal=nodeContractAddressLocal)
        return status

    def removeTemporaryShareHolder(address):
        status =NodeContractModel.removeTemporaryShareHolder(owner_addr=publicKey,private_addr=privateKey,share_holder=address)
        return status

    def makeHolderRequests(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status =NodeContractModel.makeHolderRequests(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return status

    def addMyShares(shares,publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        status =NodeContractModel.addMyShares(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,shares=shares,nodeContractAddressLocal=nodeContractAddressLocal)
        return status

    def getMyShares():
        shares =NodeContractModel.getMyShares(owner_addr=publicKey,private_addr=privateKey)
        return shares
    def getShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        shareHolders =NodeContractModel.getMyShareHolders(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return shareHolders

    def getRequestedShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        shareHolders =NodeContractModel.getRequestedShareHolders(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return shareHolders
    
    def getRejectedShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        shareHolders =NodeContractModel.getRejectedShareHolders(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return shareHolders

    def distribute(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal,email,vault):
        status =NodeContractModel.distributeShares(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal,email=email,vault=vault)
        return status
        

    def requestShares(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal, userName,generated_signed_otp,entered_signed_otp):
        status =NodeContractModel.requestShares(owner_addr=publicKeyLocal,private_addr=privateKeyLocal,user_name=userName,generated_signed_otp=generated_signed_otp, entered_signed_otp=entered_signed_otp,nodeContractAddressLocal=nodeContractAddressLocal)
        return status
        
    def getVaultHash(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal,userName,generated_signed_otp,entered_signed_otp):
        vaultHash =NodeContractModel.requestVaultHash(owner_addr=publicKey,private_addr=privateKeyLocal,user_name=userName,generated_signed_otp=generated_signed_otp, entered_signed_otp=entered_signed_otp, nodeContractAddressLocal=nodeContractAddressLocal)
        return vaultHash

    def getReceivedShares(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        shares =NodeContractModel.getReceivedShares(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return shares

    def checkUserExists(userName):
        val=NodeContractModel.checkUserNameExist(userName=userName,owner_addr=publicKey,private_addr=privateKey)
        return val
    
    def getMyState(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        NodeContractModel.refreshStatus(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        val=NodeContractModel.getMyState(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return val
    
    def getHolderStatus(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        NodeContractModel.refreshShareHoldersLists(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        temporaryHolders=NodeContractController.getRequestedShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal)
        acceptedHolders=NodeContractController.getShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal)
        rejectedHolders=NodeContractController.getRejectedShareHolders(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal)
        holderLi=[]
        for holder in temporaryHolders:
            if (holder in acceptedHolders):
                holderLi.append([holder,"Accepted"])
            elif(holder in rejectedHolders):
                holderLi.append([holder,"Rejected"])
            else:
                holderLi.append([holder,"Pending"])
        print(holderLi)
        return holderLi

    def getContractAddressOfPublicAddress():
        contractAddress=NodeContractModel.getContractAddressOfPrivateAddress(owner_addr=publicKey,private_addr=privateKey)
        return contractAddress
    
    def getUserName(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal):
        userName=NodeContractModel.getUserName(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal)
        return userName
    
    def getEmailByUserName(publicKeyLocal, privateKeyLocal, nodeContractAddressLocal,userName):
        email=NodeContractModel.getEmailByUserName(owner_addr=publicKeyLocal,private_addr=privateKeyLocal, nodeContractAddressLocal=nodeContractAddressLocal,userName=userName)
        return email
#NodeContractController.deploy(publicKeyLocal= publicKey,privateKeyLocal=privateKey)
#NodeContractController.checkUserExists("Alice")
#NodeContractController.register(publicKeyLocal= publicKey,privateKeyLocal=privateKey,userName= "Alice")
#NodeContractController.checkRequestsForBeAHolder()
#NodeContractController.addTemporaryShareHolder("0x617F2E2fD72FD9D5503197092aC168c91465E7f2")
#removeTemporaryShareHolder("0x1F8558989122D1ecF159Ab5855dBEAe88345360f")
#NodeContractController.addMyShares(["share1","share2","share3"])
#NodeContractController.getMyShares()
#NodeContractController.getShareHolders()
#NodeContractController.getAcceptedShareHoldersList()
#distribute()
#requestShares("Bob")
#getReceivedShares()
#checkRequestsForBeAHolder()
#acceptInvitation("0x305eC56922EDcF716F12C7a5c5961147933C0c41")
#NodeContractController.getHolderStatus()
#NodeContractController.makeHolderRequests()
#NodeContractController.getMyState()
#NodeContractController.makeHolderRequests()
#NodeContractController.getContractAddressOfPublicAddress()