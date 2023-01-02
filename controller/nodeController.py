from model.nodeModel import NodeModel

# nodeObject =nodeModel.NodeModel()
publicKey="0x4dAD3EDcA924D144464E623DBd158D23e66B4575"
privateKey="8dbfc464a00316c6adf2b09775c12f0e23b570bd51a6babbc5214386dde3911b"

class NodeController:
    def __init__(self) -> None:
        self.NodeModel = NodeModel()
    def deploy(self):
        self.NodeModel.deploy(publicKey,privateKey)
        return

    def register(self,userName):
        self.NodeModel.registerToPublicContract(
            userName, owner_addr=publicKey, private_addr=privateKey)
        return

    #share holder Role  
    def checkRequestsForBeAHolder(self):
        addresses=self.NodeModel.checkRequestsForBeAHolder(owner_addr=publicKey,private_addr=privateKey)
        return addresses

    def acceptInvitation(self,address):
        status=self.NodeModel.acceptInvitation(owner_addr=publicKey,private_addr=privateKey,share_owner=address)
        return status
    def rejectInvitation(self,address):
        status=self.NodeModel.rejectInvitation(owner_addr=publicKey,private_addr=privateKey,share_owner=address)
        return status
        
    def checkRequestsForShare(self):
        ownersList = self.NodeModel.checkRequestsForShare(
            owner_addr=publicKey, private_addr=privateKey)
        return ownersList

    def releaseShare(self,address):
        status = self.NodeModel.releaseSecret(
            owner_addr=publicKey, private_addr=privateKey, share_owner=address)
        return status


    #secret owner's role 
    def addTemporaryShareHolder(self,address):
        status =self.NodeModel.addTemporaryShareHolder(owner_addr=publicKey,private_addr=privateKey,share_holder=address)
        return status

    def removeTemporaryShareHolder(self,address):
        status =self.NodeModel.removeTemporaryShareHolder(owner_addr=publicKey,private_addr=privateKey,share_holder=address)
        return status

    def requestForTheHolders(self):
        status = self.NodeModel.makeHolderRequests(
            owner_addr=publicKey, private_addr=privateKey)
        return status

    def addMyShares(self,shares):
        status =self.NodeModel.addMyShares(owner_addr=publicKey,private_addr=privateKey,shares=shares)
        return status

    def getMyShares(self):
        shares =self.NodeModel.getMyShares(owner_addr=publicKey,private_addr=privateKey)
        return shares

    def getShareHolders(self):
        shareHolders = self.NodeModel.getMyShareHolders(
            owner_addr=publicKey, private_addr=privateKey)
        return shareHolders

    def getAcceptedShareHoldersList(self):
        shareHolders = self.NodeModel.getAcceptedShareHoldersList(
            owner_addr=publicKey, private_addr=privateKey)
        return shareHolders

    def distribute(self):
        status =self.NodeModel.distributeShares(owner_addr=publicKey,private_addr=privateKey)
        return status
        
    def requestShares(self,userName):
        status = self.NodeModel.requestShares(
            owner_addr=publicKey, private_addr=privateKey, user_name=userName)
        return status
        
    def getReceivedShares(self,):
        shares =self.NodeModel.getReceivedShares(owner_addr=publicKey,private_addr=privateKey)
        return shares
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