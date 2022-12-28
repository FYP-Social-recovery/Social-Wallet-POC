from model.nodeModel import NodeModel

# nodeObject =nodeModel.NodeModel()
publicKey="0x4dAD3EDcA924D144464E623DBd158D23e66B4575"
privateKey="8dbfc464a00316c6adf2b09775c12f0e23b570bd51a6babbc5214386dde3911b"
def deploy():
    NodeModel.deploy(publicKey,privateKey)
    return

def register(userName):
    NodeModel.registerToPublicContract(userName,owner_addr=publicKey,private_addr=privateKey)
    return

def checkRequestsForBeAHolder():
    addresses=NodeModel.checkRequestsForBeAHolder(owner_addr=publicKey,private_addr=privateKey)
    return addresses
# deploy()
# register("David")
checkRequestsForBeAHolder()
def acceptInvitation(address):
    return
def rejectInvitation(address):
    return
def checkRequestsForShare():
    return
def releaseShare(address):
    return
def addTemporaryShareHolder(address):
    return

def removeTemporaryShareHolder(address):
    return
def getMyShares():
    return
def getShareHolders():
    return

def getAcceptStatus():
    return
def distribute():
    return



