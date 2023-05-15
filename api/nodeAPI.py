from flask import Flask, redirect, url_for, request

from controller.publicContractController import PublicContractController
from controller.otp_controller import OTPController
from controller.nodeController import NodeContractController

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/first', methods=['GET'])
def first():
    return {"msg":"Hi"},200

@app.route('/test', methods=['POST'])
def test():
    #data = request.get_json()  # retrieve the data sent in the request
    print(request.form['name'])
    return {"Name":request.form["name"]},200
   # return {'message': f'Test successful! Received data: {data["name"]}'}, 200

#started POC API

#public contract controller APIs
@app.route('/public-contract/deploy',methods=['GET'])
def deployPublicContract():
    PublicContractController.deploy()
    return {"Deploy":"True"},200

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