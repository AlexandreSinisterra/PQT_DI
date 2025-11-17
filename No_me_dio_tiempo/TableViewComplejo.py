import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QTextEdit, QVBoxLayout, QWidget, QCheckBox, QComboBox, QPushButton

class DemoTabsCompleto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabWidget Completo")

        tabs = QTabWidget()

        # ---------------- Pestaña 1 ----------------
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Bienvenido a la pestaña 1"))
        layout1.addWidget(QTextEdit("Área de texto editable"))

        self.check1 = QCheckBox("Opción 1")
        self.check2 = QCheckBox("Opción 2")
        layout1.addWidget(self.check1)
        layout1.addWidget(self.check2)

        boton_estado = QPushButton("Mostrar estado CheckBoxes")
        boton_estado.clicked.connect(self.mostrar_estado_check)
        layout1.addWidget(boton_estado)

        self.label_check = QLabel("")
        layout1.addWidget(self.label_check)

        tab1.setLayout(layout1)

        # ---------------- Pestaña 2 ----------------
        tab2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Bienvenido a la pestaña 2"))

        self.combo = QComboBox()
        self.combo.addItems(["Rojo", "Verde", "Azul"])
        self.combo.currentTextChanged.connect(self.mostrar_combo)
        layout2.addWidget(QLabel("Selecciona un color:"))
        layout2.addWidget(self.combo)

        self.label_combo = QLabel("Color seleccionado: Ninguno")
        layout2.addWidget(self.label_combo)

        tab2.setLayout(layout2)

        # ---------------- Pestaña 3 ----------------
        tab3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.addWidget(QLabel("Bienvenido a la pestaña 3"))
        layout3.addWidget(QTextEdit("Otra área de texto para probar"))
        layout3.addWidget(QLabel("Información adicional"))

        tab3.setLayout(layout3)

        # Añadir pestañas
        tabs.addTab(tab1, "Pestaña 1")
        tabs.addTab(tab2, "Pestaña 2")
        tabs.addTab(tab3, "Pestaña 3")

        self.setCentralWidget(tabs)

    # Funciones
    def mostrar_estado_check(self):
        estado1 = "✔️" if self.check1.isChecked() else "❌"
        estado2 = "✔️" if self.check2.isChecked() else "❌"
        self.label_check.setText(f"Check1: {estado1}, Check2: {estado2}")

    def mostrar_combo(self, texto):
        self.label_combo.setText(f"Color seleccionado: {texto}")


app = QApplication(sys.argv)
window = DemoTabsCompleto()
window.show()
sys.exit(app.exec())
