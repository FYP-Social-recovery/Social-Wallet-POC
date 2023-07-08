import bip39 
import random
from web3 import Web3
import web3
import binascii





class KeyGenerationController:

    #generate the random value 
    def generateEntropy():
        randomNumber = random.getrandbits(128)
        print("Random number ",randomNumber)
        entropy= KeyGenerationController.bitstring_to_bytes(bin(randomNumber))
        print("Entropy: ",entropy)
        return entropy

    #byte array to hex
    def byte_to_hex(arr):
        li=list(arr)
        res = binascii.hexlify(bytearray(li))
        return res

    #convert functions (bit to byteArray and byteArray to bit) 
    def bitstring_to_bytes(s):
        print(s)
        v = int(s, 2)
        bytes_arr = bytearray()
        while v:
            bytes_arr.append(v & 0xff)
            v >>= 8
        return bytes(bytes_arr[::-1])


    #generate mnemonic words using the entropy
    def generateMnemonic(entropy):
        mnemonic =bip39.encode_bytes(entropy)
        print("mnemonic:",mnemonic)
        return mnemonic

    #generate entropy from mnemonic phase
    def mnemonicToEntropy(mnemonic):
        entropy=bip39.decode_phrase(mnemonic)
        print("Entropy for the mnemonic",entropy)
        return entropy

    #import a Wallet
    def importWalletFromMnemonic(mnemonicString):
        w3 = Web3()
        w3.eth.account.enable_unaudited_hdwallet_features()
        account =  w3.eth.account.from_mnemonic(mnemonicString, account_path="m/44'/60'/0'/0/0")

        temp=KeyGenerationController.byte_to_hex(account.privateKey)
        temp2=str(temp).split("'")
        privateKey=temp2[1]
        publicKey=account.address
        print("Private Key ",privateKey)
        print("Address ",publicKey)
        return privateKey,publicKey
    
    def generateMnemonicForNewAccount():
        entropy=KeyGenerationController.generateEntropy()
        mnemonic=KeyGenerationController.generateMnemonic(entropy)
        return mnemonic

    def generatePrivateKeyUsingEntropy(entropy):
        mnemonic=KeyGenerationController.generateMnemonic(entropy)
        prv,pub=KeyGenerationController.importWalletFromMnemonic(mnemonic)
        return prv,pub

