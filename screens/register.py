from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class RegisterScreen(QWidget):
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

        subtitle = QLabel("Crear Cuenta")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setAlignment(Qt.AlignCenter)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Nombre")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Correo")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)

        btn_register = QPushButton("Crear cuenta")
        btn_register.setStyleSheet("background-color: #4CAF50; color: white;")

        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.name)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(btn_register)
        layout.addWidget(btn_back)
        layout.setSpacing(15)
        self.setLayout(layout)
