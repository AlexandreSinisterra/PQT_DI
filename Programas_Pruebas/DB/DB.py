import sys
import sqlite3 as dbapi
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QGroupBox,
    QHBoxLayout  # Necesario para centrar el botón
)


class DB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visor de Datos de SQLite con PyQt6")
        self.setMinimumSize(600, 500)
        self.db_path = 'baseDatos.dat'

        # Cargar base de datos correctamente
        self.crearTablasDatos()
        self.insertarTablasDatos()
        profesores_data, usuarios_data = self.selectdeTablas()

        # Layout principal
        main_layout = QVBoxLayout()

        # --- CORRECCIÓN 1: Integración del Botón en el Layout ---
        self.btnDb = QPushButton("Recargar Datos de DB")
        self.btnDb.setStyleSheet("background-color: lightgreen; font-size: 14pt; padding: 10px; border-radius: 6px;")
        self.btnDb.clicked.connect(self.recargaDB)

        self.btnUsuarios = QPushButton("Volver al Menu de Usuarios")
        self.btnUsuarios.setStyleSheet("background-color: blue; font-size: 14pt; padding: 10px; border-radius: 6px;")
        self.btnUsuarios.clicked.connect(self.ventanaUsuarios)

        # Layout horizontal para centrar el botón
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()  # Espaciador izquierdo
        btn_layout.addWidget(self.btnDb)
        btn_layout.addWidget(self.btnUsuarios)
        btn_layout.addStretch()  # Espaciador derecho

        main_layout.addLayout(btn_layout)  # Añadir el botón al layout principal
        # --- FIN CORRECCIÓN 1 ---

        # --- Tabla de Usuarios ---
        usuarios_group = QGroupBox("Tabla de Usuarios")
        self.table_usuarios = QTableWidget()
        self.cargartablas(self.table_usuarios, usuarios_data, ["ID", "Nombre"])

        usuarios_layout = QVBoxLayout()
        usuarios_layout.addWidget(self.table_usuarios)
        usuarios_group.setLayout(usuarios_layout)

        main_layout.addWidget(usuarios_group)

        # --- Tabla de Profesores ---
        profesores_group = QGroupBox("Tabla de Profesores")
        self.table_profesores = QTableWidget()
        self.cargartablas(self.table_profesores, profesores_data, ["ID", "Nombre"])

        profesores_layout = QVBoxLayout()
        profesores_layout.addWidget(self.table_profesores)
        profesores_group.setLayout(profesores_layout)

        main_layout.addWidget(profesores_group)

        # 4. Asignar el layout al contenedor central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show()


    def crearTablasDatos(self):
        try:
            # 1. Conexión a la base de datos
            with dbapi.connect(self.db_path) as bdd:
                bd = bdd.cursor()

                # 2. Definición y Creación de Tablas
                sql_profesores = """
                    CREATE TABLE IF NOT EXISTS profesores (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT
                    )
                """
                sql_usuarios = """
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT
                    )
                """
                bd.execute(sql_profesores)
                bd.execute(sql_usuarios)

        except dbapi.Error as e:
            print(f"Error de base de datos: {e}")
            return [], []

    def insertarTablasDatos(self):
        try:
            with dbapi.connect(self.db_path) as bdd:
                bd = bdd.cursor()

                # Insertar datos de ejemplo si las tablas están vacías
                bd.execute("SELECT COUNT(*) FROM usuarios")
                if bd.fetchone()[0] == 0:
                    datosUsuarios = [
                        (1, "Ana Garcia"),
                        (2, "Luis Perez"),
                        (3, "Sofia Rodriguez")
                    ]
                    bd.executemany("INSERT INTO usuarios VALUES (?, ?)", datosUsuarios)
                    print("Usuarios insertados.")
                else:
                    print("Usuarios ya existentes.")

                bd.execute("SELECT COUNT(*) FROM profesores")
                if bd.fetchone()[0] == 0:
                    datosProfesores = [
                        (101, "Prof. Maria Lopez"),
                        (102, "Prof. Javier Diaz")
                    ]
                    bd.executemany("INSERT OR IGNORE INTO profesores VALUES (?, ?)", datosProfesores)
                    print("Profesores insertados.")
                else:
                    print("Profesores ya existentes.")

            bdd.commit()
        except dbapi.Error as e:
            print(f"Error de base de datos: {e}")
            return [], []


    def selectdeTablas(self):

        try:
            # 1. Conexión a la base de datos
            with dbapi.connect(self.db_path) as bdd:
                bd = bdd.cursor()

                # 4. Recuperación de datos
                bd.execute("SELECT * FROM usuarios")
                usuarios = bd.fetchall()

                bd.execute("SELECT * FROM profesores")
                profesores = bd.fetchall()

                print(f"Datos de {len(usuarios)} usuarios y {len(profesores)} profesores recuperados.")
                return profesores, usuarios

        except dbapi.Error as e:
            print(f"Error de base de datos: {e}")
            return [], []

    def cargartablas(self, tabla, data, cabeceras):
        """
        Carga los datos recuperados de la BD en el QTableWidget especificado.
        """
        # Establecer el número de filas y columnas
        tabla.setRowCount(len(data))
        tabla.setColumnCount(len(cabeceras))

        # Establecer los encabezados (nombres de columna)
        tabla.setHorizontalHeaderLabels(cabeceras)

        # Rellenar la tabla con los datos
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                # Crear un QTableWidgetItem con el dato
                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                # Insertar el item en la posición (fila, columna)
                tabla.setItem(row_index, col_index, item)

        # Ajustar el tamaño de las columnas para llenar el espacio
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Ajustar la altura de las filas al contenido
        tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def recargaDB(self):

        print("--- Botón de recarga clickeado ---")

        # 1. Obtener los nuevos datos de la base de datos
        profesores_data, usuarios_data = self.fetch_data_and_setup()

        # 2. Recargar las tablas con los nuevos datos
        self.cargartablas(self.table_usuarios, usuarios_data, ["ID", "Nombre"])
        self.cargartablas(self.table_profesores, profesores_data, ["ID", "Nombre"])

        # 3. Mostrar un mensaje de éxito (opcional)
        self.statusBar().showMessage("Datos de la Base de Datos recargados con éxito.", 2000)

    def ventanaUsuarios(self):
            self.close()
            from pyq.VentanaBaseDatos import VentanaBaseDatos
            self.vh = VentanaBaseDatos()
            self.vh.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DB()
    sys.exit(app.exec())