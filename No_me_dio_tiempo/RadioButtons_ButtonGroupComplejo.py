import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QVBoxLayout, QLabel, QWidget, QPushButton

class DemoRadioGrupos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton Grupos Demo con Limpiar")

        layout = QVBoxLayout()

        # Grupo 1
        self.radio1 = QRadioButton("Grupo1 - Opción 1")
        self.radio2 = QRadioButton("Grupo1 - Opción 2")
        self.radio5 = QRadioButton("Grupo1 - Opción 3")
        self.grupo1 = QButtonGroup(self)
        self.grupo1.setExclusive(True)
        self.grupo1.addButton(self.radio1)
        self.grupo1.addButton(self.radio2)
        self.grupo1.addButton(self.radio5)

        # Grupo 2
        self.radio3 = QRadioButton("Grupo2 - Opción 1")
        self.radio4 = QRadioButton("Grupo2 - Opción 2")
        self.radio6 = QRadioButton("Grupo2 - Opción 3")
        self.grupo2 = QButtonGroup(self)
        self.grupo2.setExclusive(True)
        self.grupo2.addButton(self.radio3)
        self.grupo2.addButton(self.radio4)
        self.grupo2.addButton(self.radio6)

        # Label para mostrar la selección
        self.label = QLabel("Selecciona una opción de cada grupo")

        # Botón para limpiar selección
        self.boton_limpiar = QPushButton("Limpiar selección")
        self.boton_limpiar.clicked.connect(self.limpiar_seleccion)

        # Conexión de eventos
        for r in [self.radio1, self.radio2, self.radio5, self.radio3, self.radio4, self.radio6]:
            r.toggled.connect(self.mostrar_seleccion)

        # Añadir widgets al layout
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio5)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio6)
        layout.addWidget(self.label)
        layout.addWidget(self.boton_limpiar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_seleccion(self):
        g1 = "Ninguno"
        g2 = "Ninguno"
        if self.radio1.isChecked():
            g1 = "Opción 1"
        elif self.radio2.isChecked():
            g1 = "Opción 2"
        elif self.radio5.isChecked():
            g1 = "Opción 3"

        if self.radio3.isChecked():
            g2 = "Opción 1"
        elif self.radio4.isChecked():
            g2 = "Opción 2"
        elif self.radio6.isChecked():
            g2 = "Opción 3"

        self.label.setText(f"Grupo1: {g1}, Grupo2: {g2}")

    def limpiar_seleccion(self):
        # Desactivar exclusividad del grupo 1, limpiar botones, volver a activar
        self.grupo1.setExclusive(False)
        for btn in self.grupo1.buttons():
            btn.setChecked(False)
        self.grupo1.setExclusive(True)

        # Desactivar exclusividad del grupo 2, limpiar botones, volver a activar
        self.grupo2.setExclusive(False)
        for btn in self.grupo2.buttons():
            btn.setChecked(False)
        self.grupo2.setExclusive(True)

        self.label.setText("Selecciona una opción de cada grupo")


app = QApplication(sys.argv)
window = DemoRadioGrupos()
window.show()
sys.exit(app.exec())
