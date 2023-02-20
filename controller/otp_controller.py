import hashlib
import string
from random import choice

class OTPController:
    def _init_(self) -> None:
        pass
    
    def random_OTP(self):
        chars = string.digits
        random_str = ''.join(choice(chars) for _ in range(4))
        return random_str


    def convert_Hash(self,str_val):
        message = str_val.encode()
        return ("SHA-256:", hashlib.sha256(message).hexdigest())

    def generateOTPHash(self):
        random_val=self.random_OTP()
        hash_val=self.convert_Hash(random_val)
        rtn=str(hash_val[1])
        return random_val,rtn