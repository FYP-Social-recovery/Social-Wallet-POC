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

    publicKeyHolderFour="0x799fe4A6cb83c817ada12258fb3B3864Fb2B5027"
    privateKeyHolderFour="7e67ba86219723f80c27e55d90c34eab27afe92d092da6eb4c05b3bbd49914c4"

    publicKeyHolderFive="0xdDCED81E6D27C0C4EAEf81485661c81AC979399C"
    privateKeyHolderFive="874a1cef37dee7bf7494da0c77dc2dc942ffca517be583408a639da347f961d4"

    publicKeyHolderSix="0xc1dc99853409Cdf40F0CD1657749aA601B9827Df"
    privateKeyHolderSix="3fdec33da5e0e37bff512e6234c0ab0f38710161057afcf9123a74deba75b236"

    publicKeyHolderSeven="0x799fe4A6cb83c817ada12258fb3B3864Fb2B5027"
    privateKeyHolderSeven="7e67ba86219723f80c27e55d90c34eab27afe92d092da6eb4c05b3bbd49914c4"

    publicKeyHolderEight="0xdDCED81E6D27C0C4EAEf81485661c81AC979399C"
    privateKeyHolderEight="874a1cef37dee7bf7494da0c77dc2dc942ffca517be583408a639da347f961d4"

    publicKeyHolderNine="0xc1dc99853409Cdf40F0CD1657749aA601B9827Df"
    privateKeyHolderNine="3fdec33da5e0e37bff512e6234c0ab0f38710161057afcf9123a74deba75b236"

    publicKeyHolderTen="0xdDCED81E6D27C0C4EAEf81485661c81AC979399C"
    privateKeyHolderTen="874a1cef37dee7bf7494da0c77dc2dc942ffca517be583408a639da347f961d4"

    publicKeyHolderEleven="0x799fe4A6cb83c817ada12258fb3B3864Fb2B5027"
    privateKeyHolderEleven="7e67ba86219723f80c27e55d90c34eab27afe92d092da6eb4c05b3bbd49914c4"

    publicKeyHolderTwelve="0xc1dc99853409Cdf40F0CD1657749aA601B9827Df"
    privateKeyHolderTwelve="3fdec33da5e0e37bff512e6234c0ab0f38710161057afcf9123a74deba75b236"


    def writeFle(data,time):
        print("Writing ",data,str(time))
        f = open("./evaluation/result.txt", "a")
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
    def deployShareHolderFour():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderFour,privateKeyLocal=Test.privateKeyHolderFour)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Four Deploy",time)
        return contract
    def deployShareHolderFive():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderFive,privateKeyLocal=Test.privateKeyHolderFive)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Five deploy",time)
        return contract
    def deployShareHolderSix():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderSix,privateKeyLocal=Test.privateKeyHolderSix)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Six Deploy",time)
        return contract
    def deployShareHolderSeven():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderSeven,privateKeyLocal=Test.privateKeyHolderSeven)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Seven Deploy",time)
        return contract
    def deployShareHolderEight():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderEight,privateKeyLocal=Test.privateKeyHolderEight)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Eight deploy",time)
        return contract
    def deployShareHolderNine():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderNine,privateKeyLocal=Test.privateKeyHolderNine)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Nine Deploy",time)
        return contract
    def deployShareHolderTen():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderTen,privateKeyLocal=Test.privateKeyHolderTen)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Ten Deploy",time)
        return contract
    def deployShareHolderEleven():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderEleven,privateKeyLocal=Test.privateKeyHolderEleven)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Eleven deploy",time)
        return contract
    def deployShareHolderTwelve():
        start=timer()
        contract =NodeContractController.deploy(publicKeyLocal=Test.publicKeyHolderTwelve,privateKeyLocal=Test.privateKeyHolderTwelve)
        end=timer()
        time=end-start
        Test.writeFle("Share Holder Twelve Deploy",time)
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
    def registerShareHolderFour(contract):
        start=timer()
        NodeContractController.register(userName="Bob", publicKeyLocal=Test.publicKeyHolderFour, privateKeyLocal=Test.privateKeyHolderFour, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Four Register ",time)
        return
    def registerShareHolderFive(contract):
        start=timer()
        NodeContractController.register(userName="Charlie", publicKeyLocal=Test.publicKeyHolderFive, privateKeyLocal=Test.privateKeyHolderFive, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Five Register",time)
        return
    def registerShareHolderSix(contract):
        start=timer()
        NodeContractController.register(userName="David", publicKeyLocal=Test.publicKeyHolderSix, privateKeyLocal=Test.privateKeyHolderSix, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Six register ",time)
        return
    def registerShareHolderSeven(contract):
        start=timer()
        NodeContractController.register(userName="Bob", publicKeyLocal=Test.publicKeyHolderSeven, privateKeyLocal=Test.privateKeyHolderSeven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Seven Register ",time)
        return
    def registerShareHolderEight(contract):
        start=timer()
        NodeContractController.register(userName="Charlie", publicKeyLocal=Test.publicKeyHolderEight, privateKeyLocal=Test.privateKeyHolderEight, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Eight Register",time)
        return
    def registerShareHolderNine(contract):
        start=timer()
        NodeContractController.register(userName="David", publicKeyLocal=Test.publicKeyHolderNine, privateKeyLocal=Test.privateKeyHolderNine, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Nine register ",time)
        return
    def registerShareHolderTen(contract):
        start=timer()
        NodeContractController.register(userName="Bob", publicKeyLocal=Test.publicKeyHolderTen, privateKeyLocal=Test.privateKeyHolderTen, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Ten Register ",time)
        return
    def registerShareHolderEleven(contract):
        start=timer()
        NodeContractController.register(userName="Charlie", publicKeyLocal=Test.publicKeyHolderEleven, privateKeyLocal=Test.privateKeyHolderEleven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Eleven Register",time)
        return
    def registerShareHolderTwelve(contract):
        start=timer()
        NodeContractController.register(userName="David", publicKeyLocal=Test.publicKeyHolderTwelve, privateKeyLocal=Test.privateKeyHolderTwelve, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Twelve register ",time)
        return
    def registerThirdParty(contract):
        start=timer()
        NodeContractController.register(userName="Eve", publicKeyLocal=Test.publicKeyThirdParty, privateKeyLocal=Test.privateKeyThirdParty, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Third Party Register ",time)
        return
    def addTempShareHolders(contract,count):
        start=timer()
        li=[Test.publicKeyHolderOne,Test.publicKeyHolderTwo,Test.publicKeyHolderThree,Test.publicKeyHolderFour,Test.publicKeyHolderFive,Test.publicKeyHolderSix,Test.publicKeyHolderSeven,Test.publicKeyHolderEight,Test.publicKeyHolderNine,Test.publicKeyHolderTen,Test.publicKeyHolderEleven,Test.publicKeyHolderTwelve]
        for i in range(0,count):
            NodeContractController.addTemporaryShareHolder(share_holder=li[i], publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
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
    def acceptBeAHolderRequestBySHFour(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderFour, privateKeyLocal=Test.privateKeyHolderFour, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Accept the holder Request By Share Holder Four ",time)
        return
    def acceptBeAHolderRequestBySHFive(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderFive, privateKeyLocal=Test.privateKeyHolderFive, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Five",time)
        return
    def acceptBeAHolderRequestBySHSix(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderSix, privateKeyLocal=Test.privateKeyHolderSix, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Six",time)
        return
    def acceptBeAHolderRequestBySHSeven(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderSeven, privateKeyLocal=Test.privateKeyHolderSeven, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Accept the holder Request By Share Holder Seven ",time)
        return
    def acceptBeAHolderRequestBySHEight(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderEight, privateKeyLocal=Test.privateKeyHolderEight, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Eight",time)
        return
    def acceptBeAHolderRequestBySHNine(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderNine, privateKeyLocal=Test.privateKeyHolderNine, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Nine",time)
        return
    def acceptBeAHolderRequestBySHTen(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTen, privateKeyLocal=Test.privateKeyHolderTen, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Accept the holder Request By Share Holder Ten ",time)
        return
    def acceptBeAHolderRequestBySHEleven(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderEleven, privateKeyLocal=Test.privateKeyHolderEleven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Eleven",time)
        return
    def acceptBeAHolderRequestBySHTwelve(contract):
        start=timer()
        NodeContractController.acceptInvitation(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTwelve, privateKeyLocal=Test.privateKeyHolderTwelve, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Accept The holder request by share Holder Twelve",time)
        return
    def refreshState(contract):
        start=timer()
        NodeContractController.getMyState(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Refresh The state",time)
        return
    def addMyShares(contract,count):
        li=[]
        for i in range(0,count):
            li.append(str(i))
         
        start=timer()
        NodeContractController.addMyShares(publicKeyLocal=Test.publicKeySecretOwner, privateKeyLocal=Test.privateKeySecretOwner, nodeContractAddressLocal=contract,shares=li)
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
    def releaseSecretBySHFour(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderFour, privateKeyLocal=Test.privateKeyHolderFour, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Four",time)
        return
    def releaseSecretBySHFive(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderFive, privateKeyLocal=Test.privateKeyHolderFive, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Five",time)
        return
    def releaseSecretBySHSix(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderSix, privateKeyLocal=Test.privateKeyHolderSix, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Six",time)
        return
    def releaseSecretBySHSeven(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderSeven, privateKeyLocal=Test.privateKeyHolderSeven, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Seven",time)
        return
    def releaseSecretBySHEight(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderEight, privateKeyLocal=Test.privateKeyHolderEight, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Eight",time)
        return
    def releaseSecretBySHNine(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderNine, privateKeyLocal=Test.privateKeyHolderNine, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Nine",time)
        return
    def releaseSecretBySHTen(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTen, privateKeyLocal=Test.privateKeyHolderTen, nodeContractAddressLocal=contract)
        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Ten",time)
        return
    def releaseSecretBySHEleven(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderEleven, privateKeyLocal=Test.privateKeyHolderEleven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder Eleven",time)
        return
    def releaseSecretBySHTwelve(contract):
        start=timer()
        NodeContractController.releaseShare(address=Test.publicKeySecretOwner,publicKeyLocal=Test.publicKeyHolderTwelve, privateKeyLocal=Test.privateKeyHolderTwelve, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Release the share By share holder twelve",time)
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



def threeHolders():
    Test.deployPublicContract()
    secretOwnerContract=Test.deploySecretOwner()
    shareHolderOneContract=Test.deployShareHolderOne()
    shareHolderTwoContract=Test.deployShareHolderTwo()
    shareHolderThreeContract=Test.deployShareHolderThree()
    thirdPartyContract=Test.deployThirdParty()

    # secretOwnerContract="0x58809886077E1844Ca9905E0c522871b0aec417f"
    # shareHolderOneContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderTwoContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderThreeContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # thirdPartyContract="0x6700d66e6c443E62e006fFedf165ce631B082fE6"

    Test.registerSecretOwner(secretOwnerContract)
    Test.registerShareHolderOne(shareHolderOneContract)
    Test.registerShareHolderTwo(shareHolderTwoContract)
    Test.registerShareHolderThree(shareHolderThreeContract)
    Test.registerThirdParty(thirdPartyContract)

    Test.addTempShareHolders(secretOwnerContract,3)
    Test.addMyShares(secretOwnerContract,3)
    Test.makeHolderRequests(secretOwnerContract)

    Test.acceptBeAHolderRequestBySHOne(shareHolderOneContract)
    Test.acceptBeAHolderRequestBySHTwo(shareHolderTwoContract)
    Test.acceptBeAHolderRequestBySHThree(shareHolderThreeContract)

    Test.refreshState(secretOwnerContract)
    Test.distribute(secretOwnerContract)

    Test.thirdPartyRequestShares(thirdPartyContract)
    Test.releaseSecretBySHOne(shareHolderOneContract)
    Test.releaseSecretBySHTwo(shareHolderTwoContract)
    Test.releaseSecretBySHThree(shareHolderThreeContract)
    shares=Test.getReleasedShares(thirdPartyContract)
    vault=Test.getVaultHash(thirdPartyContract)
    print(shares)
    print(vault)
    return

def sixHolders():
    Test.deployPublicContract()
    secretOwnerContract=Test.deploySecretOwner()

    shareHolderOneContract=Test.deployShareHolderOne()
    shareHolderTwoContract=Test.deployShareHolderTwo()
    shareHolderThreeContract=Test.deployShareHolderThree()

    shareHolderFourContract=Test.deployShareHolderFour()
    shareHolderFiveContract=Test.deployShareHolderFive()
    shareHolderSixContract=Test.deployShareHolderSix()



    thirdPartyContract=Test.deployThirdParty()

    # secretOwnerContract="0x58809886077E1844Ca9905E0c522871b0aec417f"
    # shareHolderOneContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderTwoContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderThreeContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # thirdPartyContract="0x6700d66e6c443E62e006fFedf165ce631B082fE6"

    Test.registerSecretOwner(secretOwnerContract)

    Test.registerShareHolderOne(shareHolderOneContract)
    Test.registerShareHolderTwo(shareHolderTwoContract)
    Test.registerShareHolderThree(shareHolderThreeContract)

    Test.registerShareHolderFour(shareHolderFourContract)
    Test.registerShareHolderFive(shareHolderFiveContract)
    Test.registerShareHolderSix(shareHolderSixContract)

    Test.registerThirdParty(thirdPartyContract)

    Test.addTempShareHolders(secretOwnerContract,6)
    Test.addMyShares(secretOwnerContract,6)
    Test.makeHolderRequests(secretOwnerContract)

    Test.acceptBeAHolderRequestBySHOne(shareHolderOneContract)
    Test.acceptBeAHolderRequestBySHTwo(shareHolderTwoContract)
    Test.acceptBeAHolderRequestBySHThree(shareHolderThreeContract)

    Test.acceptBeAHolderRequestBySHFour(shareHolderFourContract)
    Test.acceptBeAHolderRequestBySHFive(shareHolderFiveContract)
    Test.acceptBeAHolderRequestBySHSix(shareHolderSixContract)

    Test.refreshState(secretOwnerContract)
    Test.distribute(secretOwnerContract)

    Test.thirdPartyRequestShares(thirdPartyContract)
    Test.releaseSecretBySHOne(shareHolderOneContract)
    Test.releaseSecretBySHTwo(shareHolderTwoContract)
    Test.releaseSecretBySHThree(shareHolderThreeContract)
    Test.releaseSecretBySHFour(shareHolderFourContract)
    Test.releaseSecretBySHFive(shareHolderFiveContract)
    Test.releaseSecretBySHSix(shareHolderSixContract)
    shares=Test.getReleasedShares(thirdPartyContract)
    vault=Test.getVaultHash(thirdPartyContract)
    print(shares)
    print(vault)
    return

def nineHolders():
    Test.deployPublicContract()
    secretOwnerContract=Test.deploySecretOwner()

    shareHolderOneContract=Test.deployShareHolderOne()
    shareHolderTwoContract=Test.deployShareHolderTwo()
    shareHolderThreeContract=Test.deployShareHolderThree()

    shareHolderFourContract=Test.deployShareHolderFour()
    shareHolderFiveContract=Test.deployShareHolderFive()
    shareHolderSixContract=Test.deployShareHolderSix()

    shareHolderSevenContract=Test.deployShareHolderSeven()
    shareHolderEightContract=Test.deployShareHolderEight()
    shareHolderNineContract=Test.deployShareHolderNine()


    thirdPartyContract=Test.deployThirdParty()

    # secretOwnerContract="0x58809886077E1844Ca9905E0c522871b0aec417f"
    # shareHolderOneContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderTwoContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderThreeContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # thirdPartyContract="0x6700d66e6c443E62e006fFedf165ce631B082fE6"

    Test.registerSecretOwner(secretOwnerContract)

    Test.registerShareHolderOne(shareHolderOneContract)
    Test.registerShareHolderTwo(shareHolderTwoContract)
    Test.registerShareHolderThree(shareHolderThreeContract)

    Test.registerShareHolderFour(shareHolderFourContract)
    Test.registerShareHolderFive(shareHolderFiveContract)
    Test.registerShareHolderSix(shareHolderSixContract)

    Test.registerShareHolderSeven(shareHolderSevenContract)
    Test.registerShareHolderEight(shareHolderEightContract)
    Test.registerShareHolderNine(shareHolderNineContract)


    Test.registerThirdParty(thirdPartyContract)

    Test.addTempShareHolders(secretOwnerContract,9)
    Test.addMyShares(secretOwnerContract,9)
    Test.makeHolderRequests(secretOwnerContract)

    Test.acceptBeAHolderRequestBySHOne(shareHolderOneContract)
    Test.acceptBeAHolderRequestBySHTwo(shareHolderTwoContract)
    Test.acceptBeAHolderRequestBySHThree(shareHolderThreeContract)

    Test.acceptBeAHolderRequestBySHFour(shareHolderFourContract)
    Test.acceptBeAHolderRequestBySHFive(shareHolderFiveContract)
    Test.acceptBeAHolderRequestBySHSix(shareHolderSixContract)

    Test.acceptBeAHolderRequestBySHSeven(shareHolderSevenContract)
    Test.acceptBeAHolderRequestBySHEight(shareHolderEightContract)
    Test.acceptBeAHolderRequestBySHNine(shareHolderNineContract)

    Test.refreshState(secretOwnerContract)
    Test.distribute(secretOwnerContract)

    Test.thirdPartyRequestShares(thirdPartyContract)
    Test.releaseSecretBySHOne(shareHolderOneContract)
    Test.releaseSecretBySHTwo(shareHolderTwoContract)
    Test.releaseSecretBySHThree(shareHolderThreeContract)
    Test.releaseSecretBySHFour(shareHolderFourContract)
    Test.releaseSecretBySHFive(shareHolderFiveContract)
    Test.releaseSecretBySHSix(shareHolderSixContract)
    Test.releaseSecretBySHSeven(shareHolderSevenContract)
    Test.releaseSecretBySHEight(shareHolderEightContract)
    Test.releaseSecretBySHNine(shareHolderNineContract)
    shares=Test.getReleasedShares(thirdPartyContract)
    vault=Test.getVaultHash(thirdPartyContract)
    print(shares)
    print(vault)
    return
def twelveHolders():
    Test.deployPublicContract()
    secretOwnerContract=Test.deploySecretOwner()

    shareHolderOneContract=Test.deployShareHolderOne()
    shareHolderTwoContract=Test.deployShareHolderTwo()
    shareHolderThreeContract=Test.deployShareHolderThree()

    shareHolderFourContract=Test.deployShareHolderFour()
    shareHolderFiveContract=Test.deployShareHolderFive()
    shareHolderSixContract=Test.deployShareHolderSix()

    shareHolderSevenContract=Test.deployShareHolderSeven()
    shareHolderEightContract=Test.deployShareHolderEight()
    shareHolderNineContract=Test.deployShareHolderNine()

    shareHolderSevenContract=Test.deployShareHolderSeven()
    shareHolderEightContract=Test.deployShareHolderEight()
    shareHolderNineContract=Test.deployShareHolderNine()

    shareHolderTenContract=Test.deployShareHolderTen()
    shareHolderElevenContract=Test.deployShareHolderEleven()
    shareHolderTwelveContract=Test.deployShareHolderTwelve()

    thirdPartyContract=Test.deployThirdParty()

    # secretOwnerContract="0x58809886077E1844Ca9905E0c522871b0aec417f"
    # shareHolderOneContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderTwoContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderThreeContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # thirdPartyContract="0x6700d66e6c443E62e006fFedf165ce631B082fE6"

    Test.registerSecretOwner(secretOwnerContract)

    Test.registerShareHolderOne(shareHolderOneContract)
    Test.registerShareHolderTwo(shareHolderTwoContract)
    Test.registerShareHolderThree(shareHolderThreeContract)

    Test.registerShareHolderFour(shareHolderFourContract)
    Test.registerShareHolderFive(shareHolderFiveContract)
    Test.registerShareHolderSix(shareHolderSixContract)

    Test.registerShareHolderSeven(shareHolderSevenContract)
    Test.registerShareHolderEight(shareHolderEightContract)
    Test.registerShareHolderNine(shareHolderNineContract)

    Test.registerShareHolderTen(shareHolderTenContract)
    Test.registerShareHolderEleven(shareHolderElevenContract)
    Test.registerShareHolderTwelve(shareHolderTwelveContract)

    Test.registerThirdParty(thirdPartyContract)

    Test.addTempShareHolders(secretOwnerContract,12)
    Test.addMyShares(secretOwnerContract,12)
    Test.makeHolderRequests(secretOwnerContract)

    Test.acceptBeAHolderRequestBySHOne(shareHolderOneContract)
    Test.acceptBeAHolderRequestBySHTwo(shareHolderTwoContract)
    Test.acceptBeAHolderRequestBySHThree(shareHolderThreeContract)

    Test.acceptBeAHolderRequestBySHFour(shareHolderFourContract)
    Test.acceptBeAHolderRequestBySHFive(shareHolderFiveContract)
    Test.acceptBeAHolderRequestBySHSix(shareHolderSixContract)

    Test.acceptBeAHolderRequestBySHSeven(shareHolderSevenContract)
    Test.acceptBeAHolderRequestBySHEight(shareHolderEightContract)
    Test.acceptBeAHolderRequestBySHNine(shareHolderNineContract)

    Test.acceptBeAHolderRequestBySHTen(shareHolderTenContract)
    Test.acceptBeAHolderRequestBySHEleven(shareHolderElevenContract)
    Test.acceptBeAHolderRequestBySHTwelve(shareHolderTwelveContract)
    Test.refreshState(secretOwnerContract)
    Test.distribute(secretOwnerContract)

    Test.thirdPartyRequestShares(thirdPartyContract)
    Test.releaseSecretBySHOne(shareHolderOneContract)
    Test.releaseSecretBySHTwo(shareHolderTwoContract)
    Test.releaseSecretBySHThree(shareHolderThreeContract)
    Test.releaseSecretBySHFour(shareHolderFourContract)
    Test.releaseSecretBySHFive(shareHolderFiveContract)
    Test.releaseSecretBySHSix(shareHolderSixContract)
    Test.releaseSecretBySHSeven(shareHolderSevenContract)
    Test.releaseSecretBySHEight(shareHolderEightContract)
    Test.releaseSecretBySHNine(shareHolderNineContract)
    Test.releaseSecretBySHTen(shareHolderTenContract)
    Test.releaseSecretBySHEleven(shareHolderElevenContract)
    Test.releaseSecretBySHTwelve(shareHolderTwelveContract)
    shares=Test.getReleasedShares(thirdPartyContract)
    vault=Test.getVaultHash(thirdPartyContract)
    print(shares)
    print(vault)
    return