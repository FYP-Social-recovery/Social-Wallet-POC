from model.publicContractModel import PublicContractModel

# nodeObject =nodeModel.NodeContractModel()
publicKey="0x20543FD8D854d500121215Abc542531987f6bc2e"
privateKey="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655"

class PublicContractController:
    def deploy():
        PublicContractModel.deployPublicContract()
        return
    #pass the public key and private key of the node
    def getContractAddressByPublicAddress(publicKeyLocal, privateKeyLocal):
        contractAddress=PublicContractModel.getContractAddressFromPublicKey(owner_addr=publicKeyLocal,private_addr=privateKeyLocal)
        return contractAddress

    def checkUserExists(userName, publicKeyLocal, privateKeyLocal):
        val=PublicContractModel.checkUserNameExist(userName=userName,owner_addr=publicKeyLocal,private_addr=privateKeyLocal)
        return val

#PublicContractController.getContractAddressByPublicAddress(publicKeyLocal="0x20543FD8D854d500121215Abc542531987f6bc2e",privateKeyLocal="58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655")
#PublicContractController.checkUserExists("Alice")