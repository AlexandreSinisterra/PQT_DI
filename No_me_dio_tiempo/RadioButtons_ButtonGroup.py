import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QVBoxLayout, QLabel, QWidget, QPushButton

class DemoRadioCompleto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton Completo")

        layout = QVBoxLayout()

        # Grupo 1
        self.radio1 = QRadioButton("Opción 1")
        self.radio2 = QRadioButton("Opción 2")
        grupo1 = QButtonGroup()
        grupo1.setExclusive(True)
        grupo1.addButton(self.radio1)
        grupo1.addButton(self.radio2)

        # Grupo 2
        self.radio3 = QRadioButton("Opción 3")
        self.radio4 = QRadioButton("Opción 4")
        grupo2 = QButtonGroup()
        grupo2.setExclusive(True)
        grupo2.addButton(self.radio3)
        grupo2.addButton(self.radio4)

        # Conexiones
        self.radio1.toggled.connect(lambda: self.mostrar_seleccion(1))
        self.radio2.toggled.connect(lambda: self.mostrar_seleccion(2))
        self.radio3.toggled.connect(lambda: self.mostrar_seleccion(3))
        self.radio4.toggled.connect(lambda: self.mostrar_seleccion(4))

        layout.addWidget(QLabel("Grupo 1"))
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)

        layout.addWidget(QLabel("Grupo 2"))
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)

        self.label = QLabel("Selecciona una opción")
        layout.addWidget(self.label)

        # Botón para limpiar selección
        boton_limpiar = QPushButton("Limpiar selección")
        boton_limpiar.clicked.connect(self.limpiar_seleccion)
        layout.addWidget(boton_limpiar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_seleccion(self, num):
        radio = [self.radio1, self.radio2, self.radio3, self.radio4][num-1]
        if radio.isChecked():
            self.label.setText(f"Seleccionaste: Opción {num}")

    def limpiar_seleccion(self):
        for r in [self.radio1, self.radio2, self.radio3, self.radio4]:
            r.setAutoExclusive(False)
            r.setChecked(False)
            r.setAutoExclusive(True)
        self.label.setText("Selecciona una opción")


app = QApplication(sys.argv)
window = DemoRadioCompleto()
window.show()
sys.exit(app.exec())
