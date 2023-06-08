from flask import Flask, redirect, url_for, request

from controller.publicContractController import PublicContractController
from controller.otp_controller import OTPController
from controller.nodeController import NodeContractController

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/test', methods=['POST'])
def test():
    #data = request.get_json()  # retrieve the data sent in the request
    print(request.form['name'])
    return {"Name":request.form["name"]},200
   # return {'message': f'Test successful! Received data: {data["name"]}'}, 200

#started POC API
#public contract  APIs

#public-contract/deploy - done

@app.route('/public-contract/deploy',methods=['GET'])
def deployPublicContract():
    PublicContractController.deploy()
    return {"Deploy":"True"},200

@app.route('/public-contract/check-user-exists',methods=['GET'])
def checkUserExists():
    res=PublicContractController.checkUserExists()
    return {"result":res},200


@app.route('/public-contract/get-contract-by-public-key',methods=['GET'])
def getContractAddressByPublicKey():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    contractAddress=PublicContractController.getContractAddressByPublicAddress(publicKeyLocal=publicKey,privateKeyLocal=privateKey)
    return {"contractAddress":contractAddress},200

#Node contract APIs

#/node-contract/deploy
#/node-contract/register
#node-contract/be-holder-requests
#node=-contract/accept-invitation
#node-contract/reject-invitation
#node-contract/share-requests
#node-contract/release-share
#node-contract/add-temp-shareholder
#node-contract/make-holder-requests
#node-contract/add-shares
#node-contract/share-holders
#node-contract/requested-share-holders
#node-contract/rejected-share-holders
#node-contract/distribute
#node-contract/request-shares
#node-contract/vault-hash
#node-contract/received-shares
#node-contract/check-user-exists
#node-contract/my-state
#node-contract/holder-status
#node-contract/contract-address-by-public-address
#node-contract/user-name
#node-contract/email-by-user-name


#fingerprint APIs

#fvss APIs

#otp APIs 

@app.route('/node-contract/deploy', methods=['GET'])
def nodeDeploy():
    contractAddress=NodeContractController.deploy()
    return {"contractAddress":contractAddress},200

@app.route('/node-contract/register', methods=['POST'])
def nodeRegister():
    userName=request.form['userName']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    NodeContractController.register(userName=userName,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {},200

@app.route('/node-contract/be-holder-requests', methods=['GET'])
def getHolderRequests():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    requests=NodeContractController.checkRequestsForBeAHolder(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"beHolderRequests":requests},200

@app.route('/node-contract/accept-invitation', methods=['POST'])
def acceptInvitation():
    address=request.form['address']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.acceptInvitation(address==address,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"acceptance":status},200

@app.route('/node-contract/reject-invitation', methods=['POST'])
def rejectInvitation():
    address=request.form['address']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.rejectInvitation(address=address,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"acceptance":status},200

@app.route('/node-contract/share-requests', methods=['GET'])
def getShareRequests():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    shareRequests=NodeContractController.checkRequestsForShare(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"shareRequests":shareRequests},200

@app.route('/node-contract/release-share', methods=['POST'])
def releaseShare():
    address=request.form['address']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.releaseShare(address=address,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/add-temp-share-holder', methods=['POST'])
def addTempShareHolder():
    shareHolder=request.form['shareHolder']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.addTemporaryShareHolder(share_holder=shareHolder,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/make-shareholder-requests', methods=['POST'])
def makeShareHolderRequests():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.makeHolderRequests(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/add-shares', methods=['POST'])
def addShares():
    shares=request.form['shares']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.addMyShares(shares=shares,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/share-holders', methods=['GET'])
def getShareHolders():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    shareHolders=NodeContractController.getShareHolders(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"shareHolders":shareHolders},200

@app.route('/node-contract/requested-shareholders', methods=['GET'])
def getRequestedShareHolders():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    requestedShareHolders=NodeContractController.getRequestedShareHolders(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"requestedShareHolders":requestedShareHolders},200

@app.route('/node-contract/rejected-share-holders', methods=['GET'])
def getRejectedShareHolders():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    rejectedShareHolders=NodeContractController.getRejectedShareHolders(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"rejectedShareHolders":rejectedShareHolders},200

@app.route('/node-contract/distribute', methods=['POST'])
def distribute():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.distribute(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/request-shares', methods=['POST'])
def requestShares():
    userName=request.form['userName']
    generatedSignedOTP=request.form['generatedSignedOTP']
    enteredSignedOTP=request.form['enteredSignedOTP']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    status=NodeContractController.requestShares(generated_signed_otp=generatedSignedOTP,entered_signed_otp=enteredSignedOTP, userName=userName,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"status":status},200

@app.route('/node-contract/vault-hash', methods=['GET'])
def getVaultHash():
    userName=request.form['userName']
    generatedSignedOTP=request.form['generatedSignedOTP']
    enteredSignedOTP=request.form['enteredSignedOTP']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    vaultHash=NodeContractController.getVaultHash(generated_signed_otp=generatedSignedOTP,entered_signed_otp=enteredSignedOTP, userName=userName,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"vaultHash":vaultHash},200

@app.route('/node-contract/received-shares', methods=['GET'])
def getReceivedShares():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    shares=NodeContractController.getReceivedShares(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"shares":shares},200

@app.route('/node-contract/check-user-exists', methods=['GET'])
def checkUserExists():
    userName=request.form['userName']
    status=NodeContractController.checkUserExists(userName=userName)
    return {"status":status},200

@app.route('/node-contract/my-state', methods=['GET'])
def getMyState():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    state=NodeContractController.getMyState(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"state":state},200

@app.route('/node-contract/holder-status', methods=['GET'])
def getHolderStatus():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    holderStatus=NodeContractController.getHolderStatus(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"holderStatus":holderStatus},200

# @app.route('/node-contract/contract-address-by-public-address', methods=['GET'])
# def getContractAddressByPublicAddress():
#     userName=request.form['userName']
#     generatedSignedOTP=request.form['generatedSignedOTP']
#     enteredSignedOTP=request.form['enteredSignedOTP']
#     publicKey=request.form['publicKey']
#     privateKey=request.form['privateKey']
#     nodeContract=request.form['nodeContract']
#     status=NodeContractController.getContractAddressOfPublicAddress(generated_signed_otp=generatedSignedOTP,entered_signed_otp=enteredSignedOTP, userName=userName,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
#     return {"status":status},200


@app.route('/node-contract/user-name', methods=['GET'])
def getUserName():
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    userName=NodeContractController.getUserName(publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"userName":userName},200

@app.route('/node-contract/email-by-user-name', methods=['GET'])
def getEmail():
    userName=request.form['userName']
    publicKey=request.form['publicKey']
    privateKey=request.form['privateKey']
    nodeContract=request.form['nodeContract']
    email=NodeContractController.getEmailByUserName(userName=userName,publicKeyLocal=publicKey,privateKeyLocal=privateKey,nodeContractAddressLocal=nodeContract)
    return {"email":email},200

@app.route('/public-contract/get-contract-address', methods=['GET'])
def getContractAddress():
    publicKeyLocal = request.args.get('publicKeyLocal')
    privateKeyLocal = request.args.get('privateKeyLocal')
    rtn=PublicContractController.getContractAddressByPublicAddress(publicKeyLocal, privateKeyLocal)
    return {"contractAddress": rtn}, 200

@app.route('/public-contract/check-user-exists', methods=['GET'])
def checkUser():
    userName = request.args.get('userName')
    publicKeyLocal = request.args.get('publicKeyLocal')
    privateKeyLocal = request.args.get('privateKeyLocal')
    rtn = PublicContractController.checkUserExists(
        userName, publicKeyLocal, privateKeyLocal)
    return {"val": rtn}, 200


#OTP controller APIs
@app.route('/otp/generate-otp', methods=['GET'])
def generateOTP():
    random_val, rtn = OTPController.generateOTPHash()
    return {"val":random_val,"Hash": rtn}, 200


@app.route('/otp/sign', methods=['GET'])
def signOTP():
    rtn = OTPController.add_sign()
    return {"signed_otp": rtn}, 200

#Node controller APIs
@app.route('/node-controller/deploy', methods=['GET'])
def nodeDeploy():
    rtn = NodeContractController.deploy()
    return {"nodeContractAddress":rtn}, 200

app.run()