import sys
from PyQt5.QtWidgets import QApplication
from src.chat import ChatLoveAI

def main():
    app = QApplication(sys.argv)
    chat = ChatLoveAI()
    chat.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()