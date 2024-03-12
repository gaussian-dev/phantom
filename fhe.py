from __future__ import annotations
from numpy import uint32 as u32
from numpy import uint8 as u8


class FHEBool:
    def __init__(self, v: bool):
        self.v = v
    
    def AND(self, rhs: FHEBool):
        return FHEBool(self.v and rhs.v)

    def OR(self, rhs: FHEBool):
        return FHEBool(self.v or rhs.v)

    def NOT(self):
        return FHEBool(not self.v)

    def __str__(self):
        o = "FHEbool(" + str(self.v) + ")"
        return o
    
    @staticmethod
    def trivial(v: bool):
        return FHEBool(v)

class FHEUint32:
    def __init__(self, v: u32):
        self.v = v

    def __add__(self, rhs: FHEUint32):
        v = self.v + rhs.v
        return FHEUint32(v)

    def __sub__(self, rhs: FHEUint32) -> FHEUint32:
        v = self.v - rhs.v
        return FHEUint32(v)
    
    def __mul__(self, rhs: FHEUint32) -> FHEUint32:
        v = self.v * rhs.v
        return FHEUint32(v)
    
    def __mul__(self, rhs: FHEBool) -> FHEUint32:
        '''
        Zeros self based on whether rhs is true/false
        '''
        if rhs.v is True:
            return self
        else:
            return FHEUint32(0)

    def __lt__(self, other) -> FHEBool:
        return FHEBool(self.v < other.v)

    def __le__(self, other) -> FHEBool:
        return FHEBool(self.v <= other.v)

    def __eq__(self, other) -> FHEBool:
        return FHEBool(self.v == other.v)

    def __ne__(self, other) -> FHEBool:
        return FHEBool(self.v != other.v)

    def __gt__(self, other) -> FHEBool:
        return FHEBool(self.v > other.v)

    def __ge__(self, other) -> FHEBool:
        return FHEBool(self.v >= other.v)

    def __str__(self):
        o = "FHEUint32(" + str(self.v) + ")"
        return o
    
    def min(self, other: FHEUint32)-> FHEBool:
        if self.v < other.v:
            return self
        else:
            return other

    def max(self, other: FHEUint32)-> FHEBool:
        if self.v > other.v:
            return self
        else:
            return other

    @staticmethod
    def trivial(v: u32) -> FHEUint32:
        return FHEUint32(v)
    

class FHEUint8:
    def __init__(self, v: u8):
        self.v = v

    def __add__(self, rhs: FHEUint32) -> FHEUint32:
        v = self.v + rhs.v
        return FHEUint32(v)

    def __sub__(self, rhs: FHEUint32) -> FHEUint32:
        v = self.v - rhs.v
        return FHEUint32(v)
    
    def __mul__(self, rhs: FHEUint32) -> FHEUint32:
        v = self.v * rhs.v
        return FHEUint32(v)

    def __mul__(self, rhs: FHEBool) -> FHEBool:
        '''
        Zeros self based on whether rhs is true/false
        '''
        if rhs.v is True:
            return self
        else:
            return FHEUint8(0)

    def __le__(self, other) -> FHEBool:
        return FHEBool(self.v <= other.v)

    def __eq__(self, other) -> FHEBool:
        return FHEBool(self.v == other.v)

    def __ne__(self, other) -> FHEBool:
        return FHEBool(self.v != other.v)

    def __gt__(self, other) -> FHEBool:
        return FHEBool(self.v > other.v)

    def __ge__(self, other) -> FHEBool:
        return FHEBool(self.v >= other.v)

    def __str__(self):
        o = "FHEUint8(" + str(self.v) + ")"
        return o

    @staticmethod
    def trivial(v: u8) -> FHEUint8:
        return FHEUint8(v)

class CollectivePublicKey(): 
    def __init__(self):
        pass

    def encryptU32(self, v: u32) -> FHEUint32:
        return FHEUint32(v)

    def encryptU8(self, v: u8) -> FHEUint8:
        return FHEUint8(v)

    def encryptBool(self, v: bool) -> FHEBool:
        return FHEBool(v)

def KeyGen() -> CollectivePublicKey: 
    '''
    Imagine multiple parties x0, x1, x2, ..., xn. They participate in 1 round MPC protocol to collective generate the public key
    '''
    return CollectivePublicKey()

def CollectiveDecrypt(ct):
    '''
    Parties run ciphertext dependent single round MPC to decrypt ciphertext `ct`
    '''
    return ct.v
