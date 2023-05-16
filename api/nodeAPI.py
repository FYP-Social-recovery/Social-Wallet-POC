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
@app.route('/public-contract/deploy',methods=['GET'])
def deployPublicContract():
    PublicContractController.deploy()
    return {"Deploy":"True"},200

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