import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QTextEdit, QVBoxLayout, QWidget


class DemoCombo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox Demo")

        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(["Rojo", "Verde", "Azul"])
        self.combo.currentIndexChanged.connect(self.mostrar_indice)
        self.combo.currentTextChanged.connect(self.mostrar_texto)

        self.area_texto = QTextEdit()

        layout.addWidget(self.combo)
        layout.addWidget(self.area_texto)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_indice(self, indice):
        self.area_texto.setPlainText(f"Índice seleccionado: {indice}")

    def mostrar_texto(self, texto):
        self.area_texto.append(f"Texto seleccionado: {texto}")


app = QApplication(sys.argv)
window = DemoCombo()
window.show()
sys.exit(app.exec())
