import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QRadioButton, QCheckBox, QStackedLayout, QLabel, QScrollArea
)


class VentanaStacked(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio QStackedLayout")
        self.resize(600, 400)

        # ------------------------
        #  WIDGET CENTRAL
        # ------------------------


        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QHBoxLayout()
        central.setLayout(layout_principal)

        # ============================================================
        # PANEL IZQUIERDO → BOTONES / RADIO / CHECKBOX
        # ============================================================
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        panel_controles = QWidget()
        layout_controles = QVBoxLayout()
        panel_controles.setLayout(layout_controles)
        scroll.setWidget(panel_controles)




        # -----------------
        # QPushButtons
        # -----------------
        btn_vista1 = QPushButton("Vista 1")
        btn_vista2 = QPushButton("Vista 2")
        btn_vista3 = QPushButton("Vista 3")

        layout_controles.addWidget(btn_vista1)
        layout_controles.addWidget(btn_vista2)
        layout_controles.addWidget(btn_vista3)

        # -----------------
        # QRadioButtons
        # -----------------
        radio1 = QRadioButton("Rojo")
        radio2 = QRadioButton("Verde")
        radio3 = QRadioButton("Azul")

        layout_controles.addWidget(radio1)
        layout_controles.addWidget(radio2)
        layout_controles.addWidget(radio3)

        # -----------------
        # QCheckBox
        # -----------------
        chk_color = QCheckBox("Activar color")

        layout_controles.addWidget(chk_color)

        # sirve para rellenar el sitio sobrante con un espacio en blanco
        layout_controles.addStretch()

        layout_principal.addWidget(scroll)

        # ============================================================
        # PANEL DERECHA → QStackedLayout
        # ============================================================
        panel_stack = QWidget()
        # Este layout sirve para solo mostar 1 de los widgets a la vez que se meten
        self.stacked = QStackedLayout()
        panel_stack.setLayout(self.stacked)

        # Creamos 3 páginas
        self.pag1 = QLabel("PÁGINA 1")
        self.pag2 = QLabel("PÁGINA 2")
        self.pag3 = QLabel("PÁGINA 3")

        self.pag1.setStyleSheet("background-color: lightgray;")
        self.pag2.setStyleSheet("background-color: lightgray;")
        self.pag3.setStyleSheet("background-color: lightgray;")

        # Añadir al stacked
        self.stacked.addWidget(self.pag1)
        self.stacked.addWidget(self.pag2)
        self.stacked.addWidget(self.pag3)

        layout_principal.addWidget(panel_stack)



        # ============================================================
        # CONEXIONES
        # ============================================================

        # Cambiar página con botones
        btn_vista1.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        btn_vista2.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        btn_vista3.clicked.connect(lambda: self.stacked.setCurrentIndex(2))

        # Cambiar color según RadioButtons + CheckBox
        radio1.toggled.connect(lambda: self.cambiar_color(radio1,radio2,radio3, chk_color))
        radio2.toggled.connect(lambda: self.cambiar_color(radio1,radio2,radio3, chk_color))
        radio3.toggled.connect(lambda: self.cambiar_color(radio1,radio2,radio3, chk_color))

        chk_color.stateChanged.connect(lambda: self.cambiar_color(radio1,radio2,radio3, chk_color))


    # ============================================================
    # FUNCIÓN PARA CAMBIAR EL COLOR A LA PÁGINA ACTUAL
    # ============================================================
    def cambiar_color(self, color1, color2, color3, check):
        pagina = self.stacked.currentWidget()

        if not check.isChecked():
            pagina.setStyleSheet("background-color: lightgray;")
            return

        if color1.isChecked():
            pagina.setStyleSheet("background-color: red;")

        if color2.isChecked():
            pagina.setStyleSheet("background-color: green;")

        if color3.isChecked():
            pagina.setStyleSheet("background-color: blue;")


# ============================================================
# EJECUCIÓN
# ============================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaStacked()
    ventana.show()
    sys.exit(app.exec())
