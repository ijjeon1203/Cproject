class ICD_MSG:
    def __init__(self) -> None:
        self.recv = bytes()
        self.send = bytes()
        self.size = 0


class ICD_JAM(ICD_MSG): #11, 12, 13, 14
    def __init__(self, _id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02]))
        #self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x00, 0x22, 0x01, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x00, 0x22, 0x01, 0x00, 0x00, 0x00,
                                                0x00]))
        self.size = len(self.recv)
    
    
class ICD_SPO(ICD_MSG): #30, 31, 32
    def __init__(self, _id:int) -> None:
        super().__init__()
        self.recv = (bytes([0x3C, 0X49, 0X42, 0X49, 0X54, 0X2C]) + (_id + 0x0F).to_bytes(1) + bytes([0x2C]) + (_id + 0x0F).to_bytes(1) + (_id + 0x0F).to_bytes(1) + bytes([0x3E]))
        #self.send = (bytes([0x3C, 0x49, 0x42, 0x49, 0x54, 0x2C]) + (_id + 0x0F).to_bytes(1) + bytes([0x2C, 0x30, 0x30, 0x3E]))
        self.send = (bytes([0x3C, 0x49, 0x42, 0x49, 0x54, 0x2C]) + (_id + 0x0F).to_bytes(1) + bytes(
            [0x2C, 0xFF, 0x30, 0x3E]))

        self.size = len(self.recv)
    
    
class ICD_RC(ICD_MSG): #31, 32, 33, 34, 35
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x01, 0x00, 0x09, 0x00, 0x00, 0x00, 0x00, \
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.size = len(self.recv)
    
    
class ICD_RCACM(ICD_MSG): #41, 42, 43, 44, 45
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x07, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x07, 0x00, 0x03, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00]))
        self.size = len(self.recv)
    
    
class ICD_LnPACM(ICD_MSG): #46, 47, 48, 49
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x07, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x07, 0x00, 0x03, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00]))
        self.size = len(self.recv)
    
    
class ICD_RSD(ICD_MSG): #51
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x60, 0x00, 0x01, 0x00, 0x00, 0x00, 0x03]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x63, 0x00, 0x13, 0x00, 0x00, 0x00, 0x03,\
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,\
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.size = len(self.recv)
    
    
class ICD_MTGEI(ICD_MSG): #61
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x03, 0x02, 0x0A, 0x00, 0x00, 0x00, 0x01,\
                     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.size = len(self.recv)
    
    
class ICD_FMS(ICD_MSG): #81
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xE1]) + (_id).to_bytes(1) + bytes([0x02, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xE1, 0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0xF8, 0xFF]))
        self.size = len(self.recv)
    
    
class ICD_GNT(ICD_MSG): #91
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = bytes([0x01, 0x03, 0x5F, 0xE1, 0x00, 0x10, 0x06, 0x24])
        self.send = ((0).to_bytes(103) + bytes([0x49, 0xD3]))
                     
        self.size = len(self.recv)
    
    
class ICD_ACEQ(ICD_MSG): #A1, A2
    def __init__(self,_id:int) -> None:
        super().__init__()
        self.recv = (bytes([0xD1]) + (_id).to_bytes(1) + bytes([0x04, 0x01, 0x00, 0x00, 0x00, 0x00]))
        self.send = ((_id).to_bytes(1) + bytes([0xD1, 0x04, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.size = len(self.recv)
    
    