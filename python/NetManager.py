import subprocess
import socket
import time
import threading as th
import ICD as icd
from threading import Lock
from PyQt5.QtWidgets import QWidget


class NetManger(th.Thread):
    def __init__(self, app:QWidget):
        super().__init__(daemon=True)
        
        self.app = app
        
        self.lock = Lock()
        
        self.ip_addr = ''
        self.ip = self.ip_addr.split('.')
        self.ip_class = [0, 0, 0, 0]
                
        self.port = 0
        
        self.type = 'Unknown'
        self.socket = None
        self.client_socket = None
        
        self.net_operation = False
        self.socket_open = False
        self.socket_connected = False
        
        self.str_status = ''
        
        self.rx = 0
        self.tx = 0
        
        self.icd = None
        
    
    def setNet(self, _ip:str, _port:int) -> None:
        self.ip_addr = _ip
        self.port = _port
        
        
    def setICD(self, _icd) -> None:
        self.icd = _icd
    
    
    def checkNet(self) -> str:
        if self.ip_addr.count('.') != 3:
            return 'Check IP Address xxx.xxx.xxx.xxx'
        
        self.ip = self.ip_addr.split('.')
        classes = [
            'A',
            'B',
            'C',
            'D'
        ]
        for i in range(4):
            if self.ip[i] == '':
                return 'Check {} Class'.format(classes[i])
        
        self.ip_class = [int(self.ip[0]), int(self.ip[1]), int(self.ip[2]), int(self.ip[3])]
        
        for ip in self.ip_class:
            if ip < 0 or ip > 255:
                return 'Invalid IP Address, Check Range(0~255) each class'
            
        if self.port <= 0:
            return 'Invalid Port Num, Check Port'
        
        return ''
    
    
    def run(self) -> None:
        self.socket_open = True
        while self.socket_open:
            if self.net_operation:
                if self.socket_connected == False:
                    self.add_ip_alias()
                if self.type == 'TCP':
                    self.start_TCP()
                else:
                    self.start_UDP()
            else:
                self.lock.acquire()
                continue
        self.socket_open = False
        
        
    def kill(self) -> None:
        if th.currentThread().is_alive():
            self.socket_open = False
            self.net_operation = False
            self.remove_ip_alias()
            self.lock.release()
    
    
    def start_UDP(self) -> None:
        if self.socket_connected == False:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            for _ in range(10):
                try:
                    self.socket.bind((self.ip_addr, self.port))
                except socket.error:
                    time.sleep(1)
                    continue
                break
            else:
                self.str_status = 'Run Program as Adminator'
                self.socket_connected = False
                self.app.update()
                return
                
            self.socket_connected = True
            self.str_status = 'Connected'
            self.app.update()
        try:
            while self.net_operation:
                data, client_address = self.socket.recvfrom(1024)
                
                if len(data) > 0:
                    if len(data) == self.icd.size:
                        for i in range(self.icd.size):
                            if data[i] != self.icd.recv[i]:
                                self.rx = 2
                                self.str_status = 'Received Wrong ICD Req'
                                break
                        
                        if self.rx != 2:
                            self.rx = 1
                            if self.socket.sendto(self.icd.send, client_address) == len(self.icd.send):
                                self.tx = 1
                            else:
                                self.tx = 2
                    else:
                        self.rx = 0
                        self.tx = 0
                        self.str_status = 'Received Unexpected MSG'
                else:
                    self.rx = 2
                    self.tx = 1
                    self.str_status = 'Wrong Msg from Client...'
                self.app.update()
        except socket.error as e:
            if e.errno == 10053:
                self.str_status = 'Disconnected'
            elif e.errno == 10049:
                self.str_status = 'Run Program as Adminator'
            elif e.errno == 10054:
                return
            self.rx = 0
            self.tx = 0
            self.socket_connected = False
            self.app.update()
        self.stop_Socket()
    
    
    def start_TCP(self) -> None:
        if self.socket_connected == False:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            for _ in range(10):
                try:
                    self.socket.bind((self.ip_addr, self.port))
                except socket.error:
                    time.sleep(1)
                    continue
                break
            else:
                self.str_status = 'Run Program as Adminator'
                self.socket_connected = False
                self.app.update()
                return
                
            self.socket_connected = True
            self.str_status = 'Connected'
            self.app.update()
        try:
            self.socket.listen(5)
            self.client_socket, client_address = self.socket.accept()
            while self.net_operation:
                data = self.client_socket.recv(1024)
                
                if len(data) > 0:
                    if len(data) == self.icd.size:
                        for i in range(self.icd.size):
                            if data[i] != self.icd.recv[i]:
                                self.rx = 2
                                self.str_status = 'Received Wrong ICD Req'
                                break
                        
                        if self.rx != 2:
                            self.rx = 1
                            if self.client_socket.send(self.icd.send) == len(self.icd.send):
                                self.tx = 1
                            else:
                                self.tx = 2
                    else:
                        self.rx = 0
                        self.tx = 0
                        self.str_status = 'Received Unexpected MSG'
                else:
                    self.rx = 2
                    self.tx = 1
                    self.str_status = 'Waiting Client...'
                    self.app.update()
                    self.client_socket, client_address = self.socket.accept()
                    self.rx = 1
                    self.tx = 1
                    self.str_status = 'Connected New Client'
                self.app.update()
        except socket.error as e:
            if e.errno == 10053:
                self.str_status = 'Disconnected'
            elif e.errno == 10049:
                self.str_status = 'Run Program as Adminator'
            elif e.errno == 10054:
                return
            self.rx = 0
            self.tx = 0
            self.socket_connected = False
            self.app.update()
        self.stop_Socket()
                
    
    def start_Socket(self) -> None:
        self.net_operation = True
        self.lock.release()
                
    
    def stop_Socket(self) -> None:
        if self.socket != None:
            self.socket.close()
            self.socket = None
        if self.client_socket != None:
            self.client_socket.close()
            self.client_socket = None
        self.net_operation = False
        self.socket_connected = False
            

    def add_ip_alias(self):
        if len(self.ip_addr.split('.')) > 1:
            command = f'netsh interface ip add address 이더넷 {self.ip_addr} 255.255.0.0'
            result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
            
            if result.returncode == 0:
                print(f"Successfully added {self.ip_addr} to 이더넷")
            else:
                print(f"Failed to add {self.ip_addr} to 이더넷")
            
            
    def remove_ip_alias(self):
        if len(self.ip_addr.split('.')) > 1:
            command = f'netsh interface ip delete address "이더넷" {self.ip_addr}'
            result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
            
            if result.returncode == 0:
                print(f"Successfully removed {self.ip_addr} from 이더넷")
            else:
                print(f"Failed to remove {self.ip_addr} from 이더넷")
        
    