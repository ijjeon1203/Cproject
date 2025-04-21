from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import NetManager as nmg

class WWidget(QWidget):
    bgColor = '#C0C0C0'
    def __init__(self, parent=None, _title:str='', _ip:str='192.168.20.', _port:str='50'):
        super().__init__(parent)
        
        self.NetMg = nmg.NetManger(self)
        
        if _title[:-1] != 'RSD':
            self.NetMg.type = 'TCP'
        else:
            self.NetMg.type = 'UDP'
        
        self.NetMg.start()
        
        self.setFixedSize(1200, 50)
        self.setStyleSheet('background-color: {};'.format(self.bgColor))

        # QLabel, QLineEdit, QPushButton을 원하는 위치에 추가
        self.lb_title = QLabel(f"{_title}", self)
        self.lb_title.setGeometry(10, 10, 70, 30)
        
        self.lb_ip = QLabel('IP Addr', self)
        self.lb_ip.setGeometry(100, 10, 50, 30)

        self.edit_ip = QLineEdit(_ip, self)
        self.edit_ip.setStyleSheet('background-color: #FFFFFF;')
        self.edit_ip.setGeometry(160, 10, 130, 30)
        
        self.lb_port = QLabel('Port', self)
        self.lb_port.setGeometry(320, 10, 50, 30)

        self.edit_port = QLineEdit(_port, self)
        self.edit_port.setStyleSheet('background-color: #FFFFFF;')
        self.edit_port.setGeometry(360, 10, 100, 30)

        self.button = QPushButton("Connect", self)
        self.button.setStyleSheet('background-color: #FFFFFF;')
        self.button.clicked.connect(self.btnHandler)
        self.button.setGeometry(470, 10, 100, 30)
        
        self.lb_rx = QLabel('Rx', self)
        self.lb_rx.setGeometry(580, 10, 20, 30)
        
        self.lb_tx = QLabel('Tx', self)
        self.lb_tx.setGeometry(660, 10, 20, 30)
        
        self.str_warn = 'Initiaze'
        self.lb_warn = QLabel(self.str_warn, self)
        self.lb_warn.setStyleSheet('background-color: #FFFFFF;')
        self.lb_warn.setGeometry(800, 10, 380, 30)
        
        
    def btnHandler(self):
        if self.NetMg.net_operation:
            self.NetMg.stop_Socket()
        else:
            ip = self.NetMg.ip_addr
            port = self.NetMg.port
            self.NetMg.setNet(self.edit_ip.text(), int(self.edit_port.text()))
            
            rst = self.NetMg.checkNet()
            if rst != '':
                self.NetMg.setNet(ip, port)
                self.lb_warn.setText(rst)
                return
            self.NetMg.start_Socket()
        
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        painter.fillRect(rect, QColor(self.bgColor))
        
        color = QColor('#FFFFFF')
        if self.NetMg.rx == 1:
            color = QColor('#00FF00')
        elif self.NetMg.rx == 2:
            color = QColor('#FF0000')
        
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(color)
        
        painter.drawEllipse(610, 10, 30, 30)
        
        color = QColor('#FFFFFF')
        if self.NetMg.tx == 1:
            color = QColor('#00FF00')
        elif self.NetMg.tx == 2:
            color = QColor('#FF0000')
        
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(color)
        
        painter.drawEllipse(690, 10, 30, 30)
        
        if self.NetMg.socket_connected:
            self.edit_ip.setEnabled(False)
            self.edit_port.setEnabled(False)
            self.button.setText('Disconnect')
        else:
            self.edit_ip.setEnabled(True)
            self.edit_port.setEnabled(True)
            self.button.setText('Connect')
        
        if self.NetMg.str_status != '':
            self.str_warn = self.NetMg.str_status
            self.lb_warn.setText(self.str_warn)
            self.NetMg.str_status = ''