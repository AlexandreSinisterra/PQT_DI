import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor, QIcon


class ModeloTabla(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def rowCount(self, parent=None):
        return len(self.datos)

    def columnCount(self, parent=None):
        return len(self.datos[0]) if self.datos else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        valor = self.datos[index.row()][index.column()]

        # Mostrar el valor como texto
        if role == Qt.ItemDataRole.DisplayRole:
            return str(valor)

        # Cambiar color de fondo si es True/False
        if role == Qt.ItemDataRole.BackgroundRole:
            if valor is True:
                return QColor("lightgreen")
            elif valor is False:
                return QColor("lightcoral")

        # Cambiar color de texto si es nombre "Ana"
        if role == Qt.ItemDataRole.ForegroundRole:
            if valor == "Ana":
                return QColor("blue")

        # Ejemplo de icono: mostrar icono si valor es True
        if role == Qt.ItemDataRole.DecorationRole:
            if valor is True:
                return QIcon.fromTheme("dialog-ok")  # Icono estándar del sistema

        return None


class DemoTabla(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo TableView con Roles y Selección")

        layout = QVBoxLayout()

        # Datos de ejemplo
        datos = [
            ["Nombre", "Edad", "Activo"],
            ["Ana", 25, True],
            ["Luis", 30, False],
            ["Marta", 28, True]
        ]

        # Crear modelo y tabla
        self.modelo = ModeloTabla(datos)
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)
        layout.addWidget(self.tabla)

        # Label para mostrar selección
        self.label_seleccion = QLabel("Fila seleccionada: ninguna")
        layout.addWidget(self.label_seleccion)

        # Conectar selección de filas
        self.tabla.selectionModel().selectionChanged.connect(self.fila_seleccionada)

        # Layout principal
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def fila_seleccionada(self, selected, deselected):
        # Obtener índices de filas seleccionadas
        filas = [index.row() for index in self.tabla.selectionModel().selectedIndexes()]
        filas = sorted(set(filas))  # quitar duplicados
        if filas:
            self.label_seleccion.setText(f"Fila seleccionada: {filas}")
        else:
            self.label_seleccion.setText("Fila seleccionada: ninguna")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DemoTabla()
    window.show()
    sys.exit(app.exec())
