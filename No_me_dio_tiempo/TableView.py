import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt6.QtCore import QAbstractTableModel, Qt


class ModeloTabla(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def rowCount(self, parent=None):
        return len(self.datos)

    def columnCount(self, parent=None):
        return len(self.datos[0]) if self.datos else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.datos[index.row()][index.column()]


class DemoTabla(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TableView Demo")

        datos = [
            ["Nombre", "Edad", "Activo"],
            ["Ana", 25, True],
            ["Luis", 30, False],
            ["Marta", 28, True]
        ]

        modelo = ModeloTabla(datos)
        tabla = QTableView()
        tabla.setModel(modelo)

        layout = QVBoxLayout()
        layout.addWidget(tabla)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = DemoTabla()
window.show()
sys.exit(app.exec())
