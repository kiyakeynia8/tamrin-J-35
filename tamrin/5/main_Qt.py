import sys
import cv2
import numpy as np
from functools import partial
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from decryptor import Decryptor
from encryptor import Encryptor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.lock_btn = QPushButton()
        self.lock_btn.setText("lock")
        layout.addWidget(self.lock_btn)
        self.unlock_btn = QPushButton()
        self.unlock_btn.setText("unlock")
        layout.addWidget(self.unlock_btn)

        self.my_label = QLabel()
        layout.addWidget(self.my_label)

        image = cv2.imread("tamrin/5/image/rubik.png")
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        lu_image = cv2.imread("tamrin/5/image/encrypted.bmp")
        image_qt = QImage(image, image.shape[1], image.shape[0], QImage.Format.Format_RGB888)
        self.my_label.setPixmap(QPixmap.fromImage(image_qt))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        def lock_image(image):
            l_image = Encryptor(image)
            image_qt = QImage(l_image, l_image.shape[1], l_image.shape[0], QImage.Format.Format_RGB888)
            self.my_label.setPixmap(QPixmap.fromImage(image_qt))

        def unlock_image(image):
            image = Decryptor(image)
            image_qt = QImage(image, image.shape[1], image.shape[0], QImage.Format.Format_RGB888)
            self.my_label.setPixmap(QPixmap.fromImage(image_qt))
            
        self.lock_btn.clicked.connect(partial(lock_image, image))
        self.unlock_btn.clicked.connect(partial(unlock_image, lu_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()