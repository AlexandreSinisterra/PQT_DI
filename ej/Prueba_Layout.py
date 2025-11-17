import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QLabel, QHBoxLayout, QStackedLayout


class colores(QMainWindow):
    def __init__(self):
        super().__init__()
        # nombre de la ventana
        self.setWindowTitle("Ejercicio de colores")
        # tamaño de la ventana
        self.resize(700, 600)
        # creamos un div donde se almacenaran todos demas
        self.widget_central = QWidget()
        # se asigna como el principal
        self.setCentralWidget(self.widget_central)
        # es como los elementod dentro de el se van a organizar (en este caso en horizontal)
        layout_principal = QHBoxLayout()
        # le asignamos la distribucion al div
        self.widget_central.setLayout(layout_principal)

        # creamos otro div
        panel_izquierdo1 = QWidget()
        layout_panel_izquierdo1 = QVBoxLayout()
        panel_izquierdo1.setLayout(layout_panel_izquierdo1)

        # creamos labels (texto ya escrito)
        label_izquierdo1 = QLabel("")
        # modificamos las caracteristicas del label
        label_izquierdo1.setStyleSheet("background-color: red;")
        label_izquierdo2 = QLabel("")
        label_izquierdo2.setStyleSheet("background-color: yellow;")
        label_izquierdo3 = QLabel("")
        label_izquierdo3.setStyleSheet("background-color: purple;")

        # añadimos los label al layout
        layout_panel_izquierdo1.addWidget(label_izquierdo1)
        layout_panel_izquierdo1.addWidget(label_izquierdo2)
        layout_panel_izquierdo1.addWidget(label_izquierdo3)

        # añadimos el div al layout principal, como si fuera un label, es un elemento
        layout_principal.addWidget(panel_izquierdo1)


        panel_medio1 = QWidget()
        layout_panel_medio1 = QVBoxLayout()
        panel_medio1.setLayout(layout_panel_medio1)

        label_medio1 = QLabel("")
        label_medio1.setStyleSheet("background-color: green;")

        layout_panel_medio1.addWidget(label_medio1)

        layout_principal.addWidget(panel_medio1)


        panel_derecho1 = QWidget()
        layout_panel_derecho1 = QVBoxLayout()
        panel_derecho1.setLayout(layout_panel_derecho1)

        label_derecho1 = QLabel("")
        label_derecho1.setStyleSheet("background-color: red;")

        label_derecho2 = QLabel("")
        label_derecho2.setStyleSheet("background-color: purple;")

        layout_panel_derecho1.addWidget(label_derecho1)
        layout_panel_derecho1.addWidget(label_derecho2)

        layout_principal.addWidget(panel_derecho1)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # el nombre de tu clase
    fiestra = colores()
    fiestra.show()
    sys.exit(app.exec())