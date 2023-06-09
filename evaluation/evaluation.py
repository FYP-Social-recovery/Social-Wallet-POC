from controller.nodeController import NodeContractController
from controller.publicContractController import PublicContractController
from timeit import default_timer as timer

from eth_account import Account
from web3 import Web3, HTTPProvider
from eth_account.messages import encode_defunct                                                                                                                                        




class Test:
    publicKeyPublicContract="0x2F547E73aB2D578F92328ADBA7f6DEb8aAD02aa9"
    privateKeyPublicContract="0fb2d8b9f63f925112d1158f13248a96f73f025a765666e1264da14006b339ed"

    publicKeySecretOwner="0x2F547E73aB2D578F92328ADBA7f6DEb8aAD02aa9"
    privateKeySecretOwner="0fb2d8b9f63f925112d1158f13248a96f73f025a765666e1264da14006b339ed"

    publicKeyThirdParty="0x2F547E73aB2D578F92328ADBA7f6DEb8aAD02aa9"
    privateKeyThirdParty="0fb2d8b9f63f925112d1158f13248a96f73f025a765666e1264da14006b339ed"

    publicKeyHolderOne="0xF4d86E60b3fA7f1fD4AD2b41205D52b57Ce68905"
    privateKeyHolderOne="635692a5b8c388a50c4d2c4987426a7c7b7cc9fa1815aed74e52d192244aad1a"

    publicKeyHolderTwo="0xA21831e3493CfAaA6f23b0efBa00B5F47A59bb34"
    privateKeyHolderTwo="7a032b39be8f54d44000fe9f7f8bb157f06a37ef1b08c6bed91d209a3202cf61"

    publicKeyHolderThree="0x3B413d6f4b7d69E05707Db0E29bE01BcFB774F85"
    privateKeyHolderThree="9e0b07d20ad817db8705c10db5323b4a74dda1b07c32f931e140b5c5ef2d9a85"

    publicKeyHolderFour="0x635fA2a24282B5a157401592f39356866643125C"
    privateKeyHolderFour="17f5a80058fa4b52f6d73a339f03aaf4d0959435a31a31946061a6ecb4049e9b"

    publicKeyHolderFive="0x8DFA4358CE13dB53c466D6eABDC40439B8950d0c"
    privateKeyHolderFive="ffc73e77bef189de26c48729532ca156e15a68d65c857689392eb3090a9d5a03"

    publicKeyHolderSix="0x5F683F6c267085FF7d36D33db17dD4e42E9357C0"
    privateKeyHolderSix="a0b48f8fa21b0c23d9f2fd6454f228c021e74da5b01a57e465944015d84cd9cf"

    publicKeyHolderSeven="0xE9631EBEfb9A49c8cA4245F2b776ad2824eEDbBF"
    privateKeyHolderSeven="050f52af3003a5224bb196bd292ea5782e48c67c398bdb9ec3a719406d973506"

    publicKeyHolderEight="0x239Dd98C5C29FD035D84c9e96a8ed745fC9ED221"
    privateKeyHolderEight="1b944979262dd32b85f8f821e46f7f5f34488bc6cdf4495e9f2478e105ac14f9"

    publicKeyHolderNine="0xff272227758400790b6C68A5e5cfF85eCDc45c41"
    privateKeyHolderNine="aad9028d7e80c2150fe3d457706f400a47719f0d20e6aa82216088123b6559eb"

# --------------------------------------------------------------------------------------------

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
        NodeContractController.register(userName="Bob 1", publicKeyLocal=Test.publicKeyHolderFour, privateKeyLocal=Test.privateKeyHolderFour, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Four Register ",time)
        return
    def registerShareHolderFive(contract):
        start=timer()
        NodeContractController.register(userName="Charlie 1", publicKeyLocal=Test.publicKeyHolderFive, privateKeyLocal=Test.privateKeyHolderFive, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Five Register",time)
        return
    def registerShareHolderSix(contract):
        start=timer()
        NodeContractController.register(userName="David 1", publicKeyLocal=Test.publicKeyHolderSix, privateKeyLocal=Test.privateKeyHolderSix, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Six register ",time)
        return
    def registerShareHolderSeven(contract):
        start=timer()
        NodeContractController.register(userName="Bob 2", publicKeyLocal=Test.publicKeyHolderSeven, privateKeyLocal=Test.privateKeyHolderSeven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Seven Register ",time)
        return
    def registerShareHolderEight(contract):
        start=timer()
        NodeContractController.register(userName="Charlie 2", publicKeyLocal=Test.publicKeyHolderEight, privateKeyLocal=Test.privateKeyHolderEight, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Eight Register",time)
        return
    def registerShareHolderNine(contract):
        start=timer()
        NodeContractController.register(userName="David 2", publicKeyLocal=Test.publicKeyHolderNine, privateKeyLocal=Test.privateKeyHolderNine, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share Holder Nine register ",time)
        return
    def registerShareHolderTen(contract):
        start=timer()
        NodeContractController.register(userName="Bob 3", publicKeyLocal=Test.publicKeyHolderTen, privateKeyLocal=Test.privateKeyHolderTen, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Ten Register ",time)
        return
    def registerShareHolderEleven(contract):
        start=timer()
        NodeContractController.register(userName="Charlie 3", publicKeyLocal=Test.publicKeyHolderEleven, privateKeyLocal=Test.privateKeyHolderEleven, nodeContractAddressLocal=contract)

        end=timer()
        time=end-start
        Test.writeFle("Share holder Eleven Register",time)
        return
    def registerShareHolderTwelve(contract):
        start=timer()
        NodeContractController.register(userName="David 3", publicKeyLocal=Test.publicKeyHolderTwelve, privateKeyLocal=Test.privateKeyHolderTwelve, nodeContractAddressLocal=contract)

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
    # Test.deployPublicContract()
    # secretOwnerContract=Test.deploySecretOwner()
    # shareHolderOneContract=Test.deployShareHolderOne()
    # shareHolderTwoContract=Test.deployShareHolderTwo()
    # shareHolderThreeContract=Test.deployShareHolderThree()
    # thirdPartyContract=Test.deployThirdParty()

    secretOwnerContract="0x89910b7BD652aA67231633F8750d3dc60B854847"
    shareHolderOneContract="0xcFfAc21C427a8B3252Dd76E837c77179642eaD97"
    shareHolderTwoContract="0x84c45eA721e84108574b45E4d142F9585224F2fF"
    shareHolderThreeContract="0x694ab6D02CB44D9D57e7CF1BA66752d74d5D3E83"
    thirdPartyContract="0x89910b7BD652aA67231633F8750d3dc60B854847"

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

# threeHolders()

def sixHolders():
    # Test.deployPublicContract()
    # secretOwnerContract=Test.deploySecretOwner()

    # shareHolderOneContract=Test.deployShareHolderOne()
    # shareHolderTwoContract=Test.deployShareHolderTwo()
    # shareHolderThreeContract=Test.deployShareHolderThree()

    # shareHolderFourContract=Test.deployShareHolderFour()
    # shareHolderFiveContract=Test.deployShareHolderFive()
    # shareHolderSixContract=Test.deployShareHolderSix()



    # thirdPartyContract=Test.deployThirdParty()

    secretOwnerContract="0x073726879D28Daea12E1c56Ddd82D025b0Ab7BCe"
    shareHolderOneContract="0x2E82679fA57AEa2e345788533D44d804C7262Ee7"
    shareHolderTwoContract="0x33c818103523b97cBfEc6c6316936AcAbd39e1e2"
    shareHolderThreeContract="0xB5bD42AA65BfA0986855a1C9953552139556A925"
    shareHolderFourContract="0xd2441cf289D3E01753313e81B4016877Be4e0a52"
    shareHolderFiveContract="0xF7cF45aB6D41fc87298C88C1b17Fde2B70EE2eEa"
    shareHolderSixContract="0x2E43Cee07BB41C2BC137798674B9694204a47a7D"
    thirdPartyContract="0x073726879D28Daea12E1c56Ddd82D025b0Ab7BCe"

    # Test.registerSecretOwner(secretOwnerContract)

    # Test.registerShareHolderOne(shareHolderOneContract)
    # Test.registerShareHolderTwo(shareHolderTwoContract)
    # Test.registerShareHolderThree(shareHolderThreeContract)

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

# sixHolders()

def nineHolders():
    # Test.deployPublicContract()
    # secretOwnerContract=Test.deploySecretOwner()

    # shareHolderOneContract=Test.deployShareHolderOne()
    # shareHolderTwoContract=Test.deployShareHolderTwo()
    # shareHolderThreeContract=Test.deployShareHolderThree()

    # shareHolderFourContract=Test.deployShareHolderFour()
    # shareHolderFiveContract=Test.deployShareHolderFive()
    # shareHolderSixContract=Test.deployShareHolderSix()

    # shareHolderSevenContract=Test.deployShareHolderSeven()
    # shareHolderEightContract=Test.deployShareHolderEight()
    # shareHolderNineContract=Test.deployShareHolderNine()


    # thirdPartyContract=Test.deployThirdParty()

    secretOwnerContract="0x9979c1aCEDc13Ae3d0626BA34b5982719AE77E38"
    shareHolderOneContract="0x3e6E31C96644a797E8c18284FA5EbB0A4cd1c094"
    shareHolderTwoContract="0xfCa46E3573F94Ada643762382049c76C6126F62D"
    shareHolderThreeContract="0x7D8d1952b6F12C077708A4978699A0B7bF764B21"
    shareHolderFourContract="0xA414fa41C4356128A53fB9FEf79bf9e28Fb757e9"
    shareHolderFiveContract="0x8ed14103bB3C0E032937FFe2f96843CeCa325094"
    shareHolderSixContract="0x30A1EE4cAd077f6982D0726044CA524f7b816c01"
    shareHolderSevenContract="0xAE505F8F8f28371BB05c350BEf0B8612243a063B"
    shareHolderEightContract="0x4438FF1c3f4Fc422cC4Ec57D776357544ee05146"
    shareHolderNineContract="0x1eDb1DF7D383b0241Fb12bcB0eD85D72fE3431aB"
    thirdPartyContract="0x9979c1aCEDc13Ae3d0626BA34b5982719AE77E38"

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

nineHolders()

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
    # shareHolderFourContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderFiveContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderSixContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # shareHolderSevenContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderEightContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderNineContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
    # shareHolderTenContract="0x2b8Ef5ad3ed9550DC0C9f3f72ca2236750A1B3Ad"
    # shareHolderElevenContract="0x1c9E76C892285F759e94c234BC987De1d1581Cf2"
    # shareHolderTwelveContract="0x805A29eF483595a6FAe0C08F7629ac0011C6e705"
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