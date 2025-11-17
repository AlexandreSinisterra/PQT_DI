
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
class VentanaBaseDatos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Pulsa Aqui abajo para entrar a tu db")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: blue;")
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        caixa.addWidget(self.lblEtiqueta)


        btnDb = QPushButton("Acceso a DB")
        btnDb.setStyleSheet("background-color: lightgreen;")
        btnDb.clicked.connect(self.abrirDB)
        caixa.addWidget(btnDb)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()



    def abrirDB(self):
        self.close()
        from pyq.DB import DB
        self.vh = DB()
        self.vh.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaBaseDatos()
    sys.exit(app.exec())