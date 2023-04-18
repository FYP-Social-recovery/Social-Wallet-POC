from controller.nodeController import NodeContractController
from controller.publicContractController import PublicContractController
from timeit import default_timer as timer

from eth_account import Account
from web3 import Web3, HTTPProvider
from eth_account.messages import encode_defunct                                                                                                                                        




class Test:
    publicKeyPublicContract="0x20543FD8D854d500121215Abc542531987f6bc2e"
    privateKeyPublicContract="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"

    publicKeySecretOwner="0x1c36c98DC9b260564F17817241fED3BBA1402059"
    privateKeySecretOwner="ec754553254fd6b9bcfa929e27d378b648b4ac8adf926b0663e41e13c03c174d"

    publicKeyThirdParty="0x4A04D4fB008dceAA7Ff212f296Cd9F82874cEAff"
    privateKeyThirdParty="a0dc1ea77cb68f16abb1671b44048c6a9f7822676d841f4a9908a5a981871fce"

    publicKeyHolderOne="0x799fe4A6cb83c817ada12258fb3B3864Fb2B5027"
    privateKeyHolderOne="7e67ba86219723f80c27e55d90c34eab27afe92d092da6eb4c05b3bbd49914c4"

    publicKeyHolderTwo="0xdDCED81E6D27C0C4EAEf81485661c81AC979399C"
    privateKeyHolderTwo="874a1cef37dee7bf7494da0c77dc2dc942ffca517be583408a639da347f961d4"

    publicKeyHolderThree="0xc1dc99853409Cdf40F0CD1657749aA601B9827Df"
    privateKeyHolderThree="3fdec33da5e0e37bff512e6234c0ab0f38710161057afcf9123a74deba75b236"

    def writeFle(data,time):
        print("Writing ",data,str(time))
        f = open("./test/result.txt", "a")
        f.write(data+str(time)+"\n")
        f.close()
        return

    def deployPublicContract():
        start=timer()
        contract =PublicContractController.deploy()
        end=timer()
        time=end-start
        Test.writeFle("Public Contract Deploy",time)
        return
    def deploySecretOwner():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeySecretOwner,privateKeyLocal=Test.privateKeySecretOwner)
        end=timer()
        time=end-start
        Test.writeFle("Secret Owner Deploy",time)
        return contract
    def deployShareHolderOne():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderOne,privateKeyLocal=Test.privateKeyHolderOne)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder One Deploy",time)
        return contract
    def deployShareHolderTwo():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderTwo,privateKeyLocal=Test.privateKeyHolderTwo)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Two deploy",time)
        return contract
    def deployShareHolderThree():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderThree,privateKeyLocal=Test.privateKeyHolderThree)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Three Deploy",time)
        return contract
    def deployThirdParty():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyThirdParty,privateKeyLocal=Test.privateKeyThirdParty)
        end=timer()
        time=end-start
        Test.writeFle("Third Party Deploy",time)
        return contract
    def registerSecretOwner(contract):
        start=timer()
        NodeContractController.register(userName="Alice", publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Secret Owner Register",time)
        return
    def registerShareHolderOne(contract):
        start=timer()
        NodeContractController.register(userName="Bob", publicKeyLocal=Test.publicKeyHolderOne, privateKeyLocal=Test.privateKeyHolderOne, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder One Register ",time)
        return
    def registerShareHolderTwo(contract):
        start=timer()
        NodeContractController.register(userName="Charlie", publicKeyLocal=Test.publicKeyHolderTwo, privateKeyLocal=Test.privateKeyHolderTwo, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Two Register",time)
        return
    def registerShareHolderThree(contract):
        start=timer()
        NodeContractController.register(userName="David", publicKeyLocal=Test.publicKeyHolderThree, privateKeyLocal=Test.privateKeyHolderThree, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Three register ",time)
        return
    def registerThirdParty(contract):
        start=timer()
        NodeContractController.register(userName="Eve", publicKeyLocal=Test.publicKeyThirdParty, privateKeyLocal=Test.privateKeyThirdParty, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Third Party Register ",time)
        return
    def addTempShareHolders(contract):
        start=timer()
        li=[Test.publicKeyHolderOne,Test.publicKeyHolderTwo,Test.publicKeyHolderThree]
        for i in li:
            NodeContractController.addTemporaryShareHolder(share_holder=i, publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Add temporary Share Holders ",time)
        return
    def makeHolderRequests(contract):
        start=timer()
        NodeContractController.makeHolderRequests(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Make Be a shareHolder requests  ",time)
        return
    def acceptBeAHolderRequestBySHOne(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderOne, privateKeyLocal=Test.privateKeyHolderOne, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Accept the holder Request By Share Holder One ",time)
        return
    def acceptBeAHolderRequestBySHTwo(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTwo, privateKeyLocal=Test.privateKeyHolderTwo, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder two",time)
        return
    def acceptBeAHolderRequestBySHThree(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderThree, privateKeyLocal=Test.privateKeyHolderThree, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Three",time)
        return
    def refreshState(contract):
        start=timer()
        NodeContractController.getMyState(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Refresh The state",time)
        return
    def addMyShares(contract):
        start=timer()
        NodeContractController.addMyShares(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract,shares=["1","2","3"])
        end=timer()
        time=end-start
        Test.writeFle("Adding My shares  ",time)
        return
    def distribute(contract):
        start=timer()
        NodeContractController.distribute(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract,email="1234",vault="TestvaultHash")
        end=timer()
        time=end-start
        Test.writeFle("Distribute the shares ",time)
        return
    def thirdPartyRequestShares(contract):
        start=timer()
        private_key = '0xcda0b1525e27c3087802e752923069957a3d745d65635516e644d7ba03da2752'

        account = Account.privateKeyToAccount(private_key) 
        message_text = '1234'
        message = encode_defunct(text=message_text)  
        web3 = Web3(HTTPProvider('https://arb-goerli.g.alchemy.com/v2/kmaQkTzL0jVfzpP6t9J1R04Y0hr9GGJE'))      
        signed_message = web3.eth.account.sign_message(message, private_key=account.privateKey)
        NodeContractController.requestShares(publicKeyLocal=Test.publicKeyThirdParty, privateKeyLocal=Test.privateKeyThirdParty, nodeContractAddressLocal=contract, userName="Alice",generated_signed_otp=signed_message,entered_signed_otp=signed_message)
        end=timer()
        time=end-start
        Test.writeFle("Third Party request the shares ",time)
        return
    def releaseSecretBySHOne(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderOne, privateKeyLocal=Test.privateKeyHolderOne, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder one",time)
        return
    def releaseSecretBySHTwo(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTwo, privateKeyLocal=Test.privateKeyHolderTwo, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder two",time)
        return
    def releaseSecretBySHThree(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderThree, privateKeyLocal=Test.privateKeyHolderThree, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder three",time)
        return
    def getReleasedShares(contract):
        start=timer()
        shares =NodeContractController.getReceivedShares(publicKeyLocal=Test.publicKeyThirdParty, privateKeyLocal=Test.privateKeyThirdParty, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Third Party get the released shares",time)
        return shares
    def getVaultHash(contract):
        start=timer()
        private_key = '0xcda0b1525e27c3087802e752923069957a3d745d65635516e644d7ba03da2752'

        account = Account.privateKeyToAccount(private_key) 
        message_text = '1234'
        message = encode_defunct(text=message_text) 
        web3 = Web3(HTTPProvider('https://arb-goerli.g.alchemy.com/v2/kmaQkTzL0jVfzpP6t9J1R04Y0hr9GGJE'))        
        signed_message = web3.eth.account.sign_message(message, private_key=account.privateKey)
        vault=NodeContractController.getVaultHash(publicKeyLocal=Test.publicKeyThirdParty, privateKeyLocal=Test.privateKeyThirdParty, nodeContractAddressLocal=contract,userName="Alice",generated_signed_otp=signed_message,entered_signed_otp=signed_message)
        end=timer()
        time=end-start
        Test.writeFle("Third Party get vault Hash",time)
        return vault


#Test.deployPublicContract()
#secretOwnerContract=Test.deploySecretOwner()
#shareHolderOneContract=Test.deployShareHolderOne()
#shareHolderTwoContract=Test.deployShareHolderTwo()
#shareHolderThreeContract=Test.deployShareHolderThree()
#thirdPartyContract=Test.deployThirdParty()

secretOwnerContract="0x58809886077E1844Ca9905E0c522871b0aec417f"
shareHolderOneContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
shareHolderTwoContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
shareHolderThreeContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
thirdPartyContract="0x6700d66e6c443E62e006fFedf165ce631B082fE6"

# Test.registerSecretOwner(secretOwnerContract)
# Test.registerShareHolderOne(shareHolderOneContract)
# Test.registerShareHolderTwo(shareHolderTwoContract)
# Test.registerShareHolderThree(shareHolderThreeContract)
# Test.registerThirdParty(thirdPartyContract)

# Test.addTempShareHolders(secretOwnerContract)
# Test.addMyShares(secretOwnerContract)
# Test.makeHolderRequests(secretOwnerContract)

# Test.acceptBeAHolderRequestBySHOne(shareHolderOneContract)
# Test.acceptBeAHolderRequestBySHTwo(shareHolderTwoContract)
# Test.acceptBeAHolderRequestBySHThree(shareHolderThreeContract)

# Test.refreshState(secretOwnerContract)
#Test.distribute(secretOwnerContract)

# Test.thirdPartyRequestShares(thirdPartyContract)
# Test.releaseSecretBySHOne(shareHolderOneContract)
# Test.releaseSecretBySHTwo(shareHolderTwoContract)
# Test.releaseSecretBySHThree(shareHolderThreeContract)
# shares=Test.getReleasedShares(thirdPartyContract)
# vault=Test.getVaultHash(thirdPartyContract)
# print(shares)
# print(vault)
