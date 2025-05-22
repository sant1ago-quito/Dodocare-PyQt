from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.jpg").scaled(100, 100, Qt.KeepAspectRatio))
        logo.setAlignment(Qt.AlignCenter)

        title = QLabel("Dodocare")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Iniciar Sesión")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setAlignment(Qt.AlignCenter)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Correo")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)

        btn_login = QPushButton("Iniciar sesión")
        btn_login.setStyleSheet("background-color: #4CAF50; color: white;")

        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(btn_login)
        layout.addWidget(btn_back)
        layout.setSpacing(15)
        self.setLayout(layout)
