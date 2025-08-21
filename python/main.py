# pyinstaller -w -F -i="logo.ico" --add-data="logo.ico;/" main.py
# import sys
# import View as view
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# def run_ui() -> None:
#     app = QApplication(sys.argv)
#     mainFrame = view.MainFrame()
#     mainFrame.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     run_ui()


# 기존 gui 서버
############################################
import os

def list_files(start_path, indent=0):
    try:
        for item in os.listdir(start_path):
            item_path = os.path.join(start_path, item)
            if os.path.isdir(item_path):
                print("  " * indent + f"[DIR]  {item}")
                list_files(item_path, indent + 1)
            else:
                print("  " * indent + f"[FILE] {item}")
    except PermissionError:
        print("  " * indent + "[ACCESS DENIED]")

if __name__ == "__main__":
    folder_path = input("폴더 경로를 입력하세요: ").strip()
    if os.path.exists(folder_path):
        list_files(folder_path)
    else:
        print("❌ 경로가 존재하지 않습니다.")
