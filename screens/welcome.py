from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class WelcomeScreen(QWidget):
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

        welcome = QLabel("¡Bienvenido/a!")
        welcome.setFont(QFont("Arial", 16))
        welcome.setAlignment(Qt.AlignCenter)

        btn_login = QPushButton("Iniciar sesión")
        btn_login.setStyleSheet("background-color: #4CAF50; color: white;")
        btn_login.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        btn_register = QPushButton("Crear Cuenta")
        btn_register.setStyleSheet("background-color: #4285F4; color: white;")
        btn_register.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        btn_guest = QPushButton("Ingresar como invitado")
        btn_guest.setStyleSheet("background-color: #4285F4; color: white;")
        btn_guest.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addWidget(btn_login)
        layout.addWidget(btn_register)
        layout.addWidget(btn_guest)
        layout.setSpacing(20)
        self.setLayout(layout)
