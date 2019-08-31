import os
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QSpinBox, QLineEdit
from PyQt5.QtCore import QCoreApplication
import time

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        qbtn = QPushButton('Завершить работу', self)
        qbtn.clicked.connect(self.shutdown)
        self.text = QLineEdit()
        self.spin = QSpinBox()
        self.spin.setRange(0, 3600000)
        self.spin.setSingleStep(60)
        self.spin.setValue(60)
        vbox = QVBoxLayout()
        vbox.addWidget(qbtn)
        vbox.addWidget(self.text)
        vbox.addWidget(self.spin)
        self.setWindowTitle('Завершение по таймеру')
        self.show()
        self.setLayout(vbox)
        self.setGeometry(150, 150, 250, 150)
        myCmd = 'tasklist'
        os.system(myCmd)


    def shutdown(self):
        time.sleep(self.spin.value())
        myCmd = 'taskkill /IM {}'.format(self.text.text())
        os.system(myCmd)
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


