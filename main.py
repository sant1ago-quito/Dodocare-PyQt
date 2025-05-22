import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from screens.welcome import WelcomeScreen
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.guest import GuestScreen 
app = QApplication(sys.argv)

stack = QStackedWidget()

welcome = WelcomeScreen(stack)
login = LoginScreen(stack)
register = RegisterScreen(stack)
guest = GuestScreen(stack) # Asumiendo que tengamos la pantalla de invitado

stack.addWidget(welcome)   # index 0
stack.addWidget(login)     # index 1
stack.addWidget(register)  # index 2
stack.addWidget(guest)     # index 3
stack.setFixedSize(360, 640)
stack.setCurrentIndex(0)
stack.show()

sys.exit(app.exec_())
