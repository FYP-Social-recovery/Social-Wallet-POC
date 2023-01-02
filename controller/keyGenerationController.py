import bip39 
import random
from coincurve import PrivateKey
from bip44 import Wallet
from bip44.utils import get_eth_addr
from bip32 import BIP32, HARDENED_INDEX
from tkinter import *
from tkinter import ttk
import tkinter as tk

#generate the random value 
class KeyGenerationController:
    def generateEntropy():
        randomNumber = random.getrandbits(128)
        print("Random number ",randomNumber)
        entropy= KeyGenerationController.bitstring_to_bytes(bin(randomNumber))
        print("Entropy: ",entropy)
        return entropy



    #convert functions (bit to byteArray and byteArray to bit) 
    def bitstring_to_bytes(s):
        print(s)
        v = int(s, 2)
        bytes_arr = bytearray()
        while v:
            bytes_arr.append(v & 0xff)
            v >>= 8
        return bytes(bytes_arr[::-1])


    def access_bit(data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1

    def byte_to_bit(seed):
        bitSeed=""
        for i in range(len(seed)*8):
            bitSeed=bitSeed+str(KeyGenerationController.access_bit(seed,i))
        return bitSeed



    #generate mnemonic words 
    def generateMnemonic(entropy):
        mnemonic =bip39.encode_bytes(entropy)
        print("mnemonic:",mnemonic)
        return mnemonic





    #generate 512 bit seed
    def generateBitSeed(mnemonicPhrase,password):
        seed= bip39.phrase_to_seed(mnemonicPhrase,password)
        print("512 bit seed as a byte array: ",seed)
        print("512 bit seed::",KeyGenerationController.byte_to_bit(seed))
        return seed
    # seed= bip39.phrase_to_seed(mnemonic)



    #generate seed using the mnemonic 
    def regenerateEntropy(mnemonic):
        decoded_phrase= bip39.decode_phrase(mnemonic)
        print("regenerated entropy using the mnemonic",decoded_phrase)
        return decoded_phrase




    #create BIP32 object
    def createBIP32(seed):
        bip32 = BIP32.from_seed(seed)
        return bip32


    #create extended private keys and public keys for the default path
    def getExtendedPrivateKEyFromPath(bip32,path="m/44'/0'/0'"):
        extendedPrivateKey=bip32.get_xpriv_from_path(path)
        print("Extended Private Key",extendedPrivateKey)
        return extendedPrivateKey

    def getExtendedPublicKeyFromPath(bip32,path="m/44'/0'/0'"):
        extendedPublicKey= bip32.get_xpub_from_path(path)
        print("Extended Private Key",extendedPublicKey)
        return extendedPublicKey 
    
    #create public keys and the private keys for a given path 
    def getPublicKeyFromPath(bip32,path="m/44'/60'/0'/0/0"):
        publicKey= bip32.get_pubkey_from_path(path)
        print("public key of the given path: ",path,hex(int(KeyGenerationController.byte_to_bit(publicKey),2)))
        publicKeyHex=hex(int(KeyGenerationController.byte_to_bit(publicKey),2))
        return publicKeyHex

    def getPrivateKeyFromPath(bip32,path="m/44'/60'/0'/0/0"):
        privateKey=bip32.get_privkey_from_path(path)
        print("Private key of the given path: ",path,hex(int(KeyGenerationController.byte_to_bit(privateKey),2)))
        privateKeyHex=hex(int(KeyGenerationController.byte_to_bit(privateKey),2))
        return privateKeyHex




    def main(password=""):
        entropy=KeyGenerationController.generateEntropy()
        mnemonic=KeyGenerationController.generateMnemonic(entropy)
        seed=KeyGenerationController.generateBitSeed(mnemonic,password)    
        regeneratedEntropy=KeyGenerationController.regenerateEntropy(mnemonic) #not used for now just for testing
        bip32 =KeyGenerationController.createBIP32(seed)
        xprv=KeyGenerationController.getExtendedPrivateKEyFromPath(bip32,"m/44'/0'/0'")
        xpub=KeyGenerationController.getExtendedPublicKeyFromPath(bip32,"m/44'/0'/0'")
        
        prv1=KeyGenerationController.getPrivateKeyFromPath(bip32,"m/44'/60'/0'/0/0")
        pub1=KeyGenerationController.getPublicKeyFromPath(bip32,"m/44'/60'/0'/0/0")

        prv2=KeyGenerationController.getPrivateKeyFromPath(bip32,"m/44'/0'/0'/1")
        pub2=KeyGenerationController.getPublicKeyFromPath(bip32,"m/44'/0'/0'/1")

        prv3=KeyGenerationController.getPrivateKeyFromPath(bip32,"m/44'/0'/0'/2")
        pub3=KeyGenerationController.getPublicKeyFromPath(bip32,"m/44'/0'/0'/2")

        # prv4=getPrivateKeyFromPath(bip32,"m/44'/60'/0'/0/0")
        # pub4=getPublicKeyFromPath(bip32,"m/44'/60'/0'/0/0")

        return entropy,mnemonic,seed,bip32,xprv,xpub,prv1,pub1,prv2,pub2,prv3,pub3


    #import a Wallet
    def importWalletFromMnemonic(mnemonicString):
        seed=KeyGenerationController.generateBitSeed(mnemonicString,"")
        bip32 =KeyGenerationController.createBIP32(seed)
        privatekey=KeyGenerationController.getPrivateKeyFromPath(bip32,"m/44'/60'/0'/0/0")
        publicKey=KeyGenerationController.getPublicKeyFromPath(bip32,"m/44'/60'/0'/0/0")
        return privatekey,publicKey