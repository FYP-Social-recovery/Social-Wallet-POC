from model.nodeModel import NodeModel

# nodeObject =nodeModel.NodeModel()
publicKey="0x4dAD3EDcA924D144464E623DBd158D23e66B4575"
privateKey="8dbfc464a00316c6adf2b09775c12f0e23b570bd51a6babbc5214386dde3911b"

class NodeController:
    def deploy():
        NodeModel.deploy(publicKey,privateKey)
        return

    def register(userName):
        NodeModel.registerToPublicContract(userName,owner_addr=publicKey,private_addr=privateKey)
        return

    #share holder Role  
    def checkRequestsForBeAHolder():
        addresses=NodeModel.checkRequestsForBeAHolder(owner_addr=publicKey,private_addr=privateKey)
        return addresses

    def acceptInvitation(address):
        status=NodeModel.acceptInvitation(owner_addr=publicKey,private_addr=privateKey,share_owner=address)
        return status
    def rejectInvitation(address):
        status=NodeModel.rejectInvitation(owner_addr=publicKey,private_addr=privateKey,share_owner=address)
        return status
        
    def checkRequestsForShare():
        ownersList=NodeModel.checkRequestsForShare(owner_addr=publicKey,private_addr=privateKey)
        return ownersList

    def releaseShare(address):
        status=NodeModel.releaseSecret(owner_addr=publicKey,private_addr=privateKey,share_owner=address)
        return status


    #secret owner's role 
    def addTemporaryShareHolder(address):
        status =NodeModel.addTemporaryShareHolder(owner_addr=publicKey,private_addr=privateKey,share_holder=address)
        return status

    def removeTemporaryShareHolder(address):
        status =NodeModel.removeTemporaryShareHolder(owner_addr=publicKey,private_addr=privateKey,share_holder=address)
        return status

    def requestForTheHolders():
        status =NodeModel.makeHolderRequests(owner_addr=publicKey,private_addr=privateKey)
        return status

    def addMyShares(shares):
        status =NodeModel.addMyShares(owner_addr=publicKey,private_addr=privateKey,shares=shares)
        return status

    def getMyShares():
        shares =NodeModel.getMyShares(owner_addr=publicKey,private_addr=privateKey)
        return shares
    def getShareHolders():
        shareHolders =NodeModel.getMyShareHolders(owner_addr=publicKey,private_addr=privateKey)
        return shareHolders

    def getAcceptedShareHoldersList():
        shareHolders =NodeModel.getAcceptedShareHoldersList(owner_addr=publicKey,private_addr=privateKey)
        return shareHolders

    def distribute():
        status =NodeModel.distributeShares(owner_addr=publicKey,private_addr=privateKey)
        return status
        

    def requestShares(userName):
        status =NodeModel.requestShares(owner_addr=publicKey,private_addr=privateKey,user_name=userName)
        return status
        
    def getReceivedShares():
        shares =NodeModel.getReceivedShares(owner_addr=publicKey,private_addr=privateKey)
        return shares

    def checkUserExists(userName):
        val=NodeModel.checkUserNameExist(userName)
        return val
#deploy()
#register("Bob")
#checkRequestsForBeAHolder()
#addTemporaryShareHolder("0x09D962CA1caAf625964FB88aEAb0C3657e985d67")
#removeTemporaryShareHolder("0x1F8558989122D1ecF159Ab5855dBEAe88345360f")
#addMyShares(["share1","share2","share3"])
#getMyShares()
#getShareHolders()
#getAcceptedShareHoldersList()
#distribute()
#requestShares("Bob")
#getReceivedShares()
#checkRequestsForBeAHolder()
#acceptInvitation("0x305eC56922EDcF716F12C7a5c5961147933C0c41")