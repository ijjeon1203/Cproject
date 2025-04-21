import resources
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import WWidget as Wwgt
import ICD as icd

settings = list()
default_ip = ''
default_port = ''

class MainFrame(QWidget):
    def __init__(self):
        global settings, default_ip, default_port
        
        with open('setting.ini', 'r') as file:
            lines = file.readlines()
            for line in lines:
                txt = line.replace('\n', '').split(' ')
                if txt[0] == '0x00':
                    default_ip = txt[1]
                    default_port = txt[2]
                else:
                    settings.append(txt)
                
        
        super().__init__()

        self.setFixedSize(1250, 1000)
        self.setStyleSheet("background-color: #A0A0A0;")
        
        scroll_rect = QScrollArea(self)
        scroll_rect.setWidgetResizable(True)
        scroll_rect.setFixedWidth(1255)
        scroll_rect.setFixedHeight(1000)

        panel_widget = QWidget()
        self.main_layout = QVBoxLayout(panel_widget)
        scroll_rect.setWidget(panel_widget)
        
        layer_info = [
            ['JAM', 4],
            ['SPO', 3],
            ['RC', 5],
            ['RCACM', 5],
            ['L#PACM', 4],
            ['RSD', 1],
            ['MTGEI', 1],
            ['FMS', 1],
            ['GNT', 1],
            ['ACEQ', 2]
        ]
        self.subwidgets = []
        for i in range(10):
            new_subwidget = SubWidget(self, layer_info[i][0], layer_info[i][1])
            for _ in range(layer_info[i][1]):
                new_subwidget.add_wwidget()
            self.main_layout.addWidget(new_subwidget)
            self.subwidgets.append(new_subwidget)
        
        self.setWindowTitle('Digitron Network Emulator')
        self.setWindowIcon(QIcon(resources.icon))
        
        
    def closeEvent(self, event):
        for sub in self.subwidgets:
            for wwgt in sub.wwidgets:
                wwgt.NetMg.kill()
        event.accept()


class SubWidget(QWidget):
    bgColor = '#F0F0F0'
    class TitleWidget(QWidget):
        bgColor = '#9696FF'
        def __init__(self, parent=None, _title:str=''):
            super().__init__(parent)
            
            title_layout = QHBoxLayout()
            self.setLayout(title_layout)
            
            self.label = QLabel(f"{_title} Section", self)
            self.label.setFixedSize(800, 30)
            self.label.setStyleSheet("background-color: {};".format(self.bgColor))
            title_layout.addWidget(self.label)
            
            self.pushed = False
            self.button = QPushButton('All Control')
            self.button.setStyleSheet('background-color: #FFFFFF;')
            self.button.clicked.connect(parent.btnControl)
            self.button.setFixedSize(100, 30)
            title_layout.addWidget(self.button)
        
        
        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            rect = self.rect()
            painter.fillRect(rect, QColor(self.bgColor))
    
    
    def __init__(self, parent=None, _title:str='', _max:int=1):
        super().__init__(parent)

        self.vbox_layout = QVBoxLayout()
        self.setLayout(self.vbox_layout)
        
        self.part = _title
        self.MAX_WIDGET = _max
        
        self.title_widget = self.TitleWidget(self, _title)
        self.vbox_layout.addWidget(self.title_widget)

        self.wwidgets = []
        
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        painter.fillRect(rect, QColor(self.bgColor))
            
            
    def add_wwidget(self):
        if len(self.wwidgets) < self.MAX_WIDGET :
            wgt_label = ''
            str_part = self.part.split('#')
            if self.part.find('#', 0, -1) > 0:
                wgt_label = str_part[0] + str(len(self.wwidgets) + 1) + str_part[1]
            else:
                wgt_label = str_part[0] + str(len(self.wwidgets) + 1)
            wwidget = Wwgt.WWidget(self, wgt_label)
            
            _icd = icd.ICD_MSG()
            cmp_id = 0
            if self.part == 'JAM':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x11
                _icd = icd.ICD_JAM(cmp_id)
            elif self.part == 'SPO': #id is 0x30, 0x31, 0x32 / it's ascii 0, 1, 2
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x21
                _icd = icd.ICD_SPO(cmp_id)
            elif self.part == 'RC':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x31
                _icd = icd.ICD_RC(cmp_id)
            elif self.part == 'RCACM':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x41
                _icd = icd.ICD_RCACM(cmp_id)
            elif self.part == 'L#PACM':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x46
                _icd = icd.ICD_LnPACM(cmp_id)
            elif self.part == 'RSD':
                _icd.type = 'UDP'
                cmp_id = len(self.wwidgets) + 0x51
                _icd = icd.ICD_RSD(cmp_id)
            elif self.part == 'MTGEI':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x61
                _icd = icd.ICD_MTGEI(cmp_id)
            elif self.part == 'FMS':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x81
                _icd = icd.ICD_FMS(cmp_id)
            elif self.part == 'GNT':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0x91
                _icd = icd.ICD_GNT(cmp_id)
            elif self.part == 'ACEQ':
                _icd.type = 'TCP'
                cmp_id = len(self.wwidgets) + 0xA1
                _icd = icd.ICD_ACEQ(cmp_id)



            wwidget.NetMg.setICD(_icd)
            
            if cmp_id != 0:
                global settings, default_ip, default_port
                for s in settings:
                    if int(s[0], 16) == cmp_id:
                        wwidget.edit_ip.setText(s[1])
                        wwidget.edit_port.setText(s[2])
                        break
                else:
                    wwidget.edit_ip.setText(default_ip)
                    wwidget.edit_port.setText(default_port)
            
            self.vbox_layout.addWidget(wwidget)
            self.wwidgets.append(wwidget)
            
            
    def btnControl(self):
        self.title_widget.pushed = not self.title_widget.pushed
        if self.title_widget.pushed:
            self.title_widget.button.setStyleSheet('background-color: #A0A0A0;')
        else:
            self.title_widget.button.setStyleSheet('background-color: #FFFFFF;')
        for w in self.wwidgets:
            w.btnHandler()

