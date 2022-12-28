from model.nodeModel import NodeModel

# nodeObject =nodeModel.NodeModel()



def deploy():
    NodeModel.deploy("0x305eC56922EDcF716F12C7a5c5961147933C0c41","2e4d7319aad09af344608bde9dee0aa5a8243f847dc004545927a3488c0f8338")
    return

def register():
    NodeModel.registerToPublicContract("Alice")
    return
deploy()
register()

def checkRequestsForBeAHolder():
    return

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



