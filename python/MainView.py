import sys
from PyQt5.QtWidgets import *

class Main_View(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.initUI()


    def initUI(self):
        layout =QVBoxLayout()
        btn_next = QPushButton("FMTS")
        btn_next.clicked.connect(lambda: self.parent.switch_page(2))

        layout.addWidget(btn_next)
        self.setLayout(layout)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)  # 두 번째 페이지로 전환

    def closeEvent(self, event):
        for sub in self.subwidgets:
            for wwgt in sub.wwidgets:
                wwgt.NetMg.kill()
        event.accept()