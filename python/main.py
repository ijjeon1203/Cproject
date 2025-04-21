# pyinstaller -w -F -i="logo.ico" --add-data="logo.ico;/" main.py
import sys
import FMTSView as view
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MainView import Main_View
from FMTSView import FMTS_View

import FMTSView


# class Main(QWidget):


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emulator")
        self.setGeometry(100, 100, 400, 300)

        # 스택 위젯을 사용하여 여러 페이지 관리
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # 페이지 추가
        self.MainView = Main_View(self)
        self.FMTSView = FMTS_View(self)
        self.stack.addWidget(self.MainView)
        self.stack.addWidget(self.FMTSView)

        # 첫 번째 페이지로 시작
        self.switch_page(1)

        # self.stacked_widget.setCurrentIndex(0)  # 첫 번째 창부터 시작
        # self.stacked_widget.show()

        # layout = QVBoxLayout()
        ##layout.addWidget(self.stacked_widget)
        # self.setLayout(layout)

    def switch_page(self, page_num):
        self.stack.setCurrentIndex(page_num - 1)

    # app = QApplication(sys.argv)
    # FMTSFrame = view.FMTSView()
    # #FMTSFrame.show()
    # MainFrame = view.MainView(self.stacked_widget)
    # MainFrame.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
