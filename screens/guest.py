from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class GuestScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        layout = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(100, 100, Qt.KeepAspectRatio))
        logo.setAlignment(Qt.AlignCenter)

        title = QLabel("Dodocare")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Modo Invitado")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setAlignment(Qt.AlignCenter)

        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(btn_back)
        layout.setSpacing(15)
        self.setLayout(layout)
