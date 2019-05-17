import base64
from pyDes import *

class MyDESCrypt:
    key = chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11) + chr(11)
    iv = chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22) + chr(22)

    def __init__(self, key='', iv=''):
        if len(key) > 0:
            self.key = key
        if len(iv) > 0:
            self.iv = iv

    def encrypt(self, str):
        k = des(self.key, ECB, self.iv, pad=None, padmode=PAD_PKCS5)

        EncryptStr = k.encrypt(str)

        return base64.b64encode(EncryptStr)  # 转base64编码返回

    def decrypt(self, str):
        k = des(self.key, ECB, self.iv, pad=None, padmode=PAD_PKCS5)
        strr = base64.b64decode(str)
        DecryptStr = k.decrypt(strr)

        return DecryptStr  # 转base64编码返回
