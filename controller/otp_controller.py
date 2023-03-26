
import hashlib
import string
import random 
import math
from model.nodeModel import NodeContractModel

class OTPController:
    # first few primes
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103,
                        107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179,
                        181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283, 293,
                        307, 311, 313, 317, 331, 337, 347, 349]

    def _init_(self) -> None:
        pass
    
    def nBitRandom(self,n):
        return random.randrange(2**(n-1)+1, 2**n - 1)
    
    def getLowLevelPrime(self,n):
        while True:
            # large random number
            pcandidate = self.nBitRandom(n)

            # Test divisibility with the gievn prime list
            for divisor in self.__class__.first_primes_list:
                if pcandidate % divisor == 0 and divisor**2 <= pcandidate:
                    break
            else:
                return pcandidate
    #rabin miller primarlity test
    def isMillerRabinPassed(self,mrcandidate):
        maxDivisionsByTwo = 0
        ecandidate = mrcandidate-1
        while ecandidate % 2 == 0:
            ecandidate >>= 1
            maxDivisionsByTwo += 1
        assert (2**maxDivisionsByTwo * ecandidate == mrcandidate-1)

        def trialComposite(round_tester):
            if pow(round_tester, ecandidate, mrcandidate) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ecandidate, mrcandidate) == mrcandidate-1:
                    return False
            return True

        # number of trials here
        numberOfRabinTrials = 30
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrcandidate)
            if trialComposite(round_tester):
                return False
        return True
    
    def largePrime(self):
        while True:
            n = 512
            prime_candidate = self.getLowLevelPrime(n)
            if not self.isMillerRabinPassed(prime_candidate):
                continue
            else:
                return prime_candidate
                break



    def random_OTP(self):
        p=self.largePrime()
        random.seed(p)
        random_int=int(random.random()*10000)
        random_str=str(random_int)

        return random_str


    def convert_Hash(self,str_val):
        message = str_val.encode()
        return ("SHA-256:", hashlib.sha256(message).hexdigest())

    def generateOTPHash(self):
        random_val=self.random_OTP()
        hash_val=self.convert_Hash(random_val)
        rtn=str(hash_val[1])
        return random_val,rtn
    
    def generateSignedOTP(self):
        OTP_str=self.random_OTP()
        signed_message=self.add_sign(OTP_str)
        return OTP_str,signed_message
    
    def add_sign(self,msg_str):
        signed_message=NodeContractModel.sign_message(msg_str)
        return signed_message


"""
otp_client=OTPController()
print(otp_client.random_OTP())


#smart contract
function generatePin() public {
        uint pin = uint(keccak256(abi.encodePacked(block.timestamp))) % 10000;
        pinHash = keccak256(abi.encodePacked(pin));
        
    }
function encryptMessage(address _recipient, bytes memory _message) public view returns (bytes memory) {
        // Get the recipient's public key
        bytes32 publicKey = getPublicKey(_recipient);

        // Encrypt the message using the recipient's public key
        bytes memory encryptedMessage = Crypto.publicEncrypt(_message, publicKey);

        return encryptedMessage;
    }


from eth_account import Account
from web3 import Web3, HTTPProvider
import json
from eth_account.messages import encode_defunct
# Connect to an Ethereum node
web3 = Web3(HTTPProvider('HTTP://127.0.0.1:7545'))
def to_32byte_hex(val):
  return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

with open('/home/tharinda98/Documents/FYP/POC/Social-Wallet-POC/controller/test.json', 'r') as f:
    abi = json.load(f)

# Load the Ethereum account from a private key
private_key = '0xcda0b1525e27c3087802e752923069957a3d745d65635516e644d7ba03da2752'
account = Account.privateKeyToAccount(private_key)
contract_address = '0xdeC674f0af285F75D7B0351284cEEcA8d689B0D0'
# Define the message to sign
message_text = 'Hello, world!'


message = encode_defunct(text=message_text)
# Sign the message using the account
signed_message = web3.eth.account.sign_message(message, private_key=account.privateKey)
print(type(signed_message))
# Get the signature components
msghash=Web3.toHex(signed_message.messageHash)
v, r, s = signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)

contract = web3.eth.contract(address=contract_address, abi=abi)
# Call the verifySignature function on the contract
result = contract.functions.ecr(msghash, v, r, s).call()

# Print the verification result
print(result)
"""