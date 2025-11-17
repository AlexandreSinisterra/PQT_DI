import sys
from mimetypes import inited

from ModeloTabla import ModeloTabla
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QListWidget, QComboBox, QTextEdit, QGridLayout, QRadioButton,
                             QButtonGroup, QTableView, QTableWidget, QTabWidget, QAbstractItemView)

"""
Aprendiendo a usar el ComboBox en Python Qt
"""
class Combo(QMainWindow):
    """
    Metodo principal del programa
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo combobox QT")
        maia = QGridLayout() # Grid para colocar ordenadamente los layout

        # Valores para crear una tabla
        datos = [['Nombre','Rol','Falecido'],
                 ['Meliodas', 'el diablo', False],
                 ['Jin jo Sun', 'aura pura', True],
                 ['Kazsuke', 'loqeusea', True  ]]

        self.nome_dni = [['p1','p2','p3'],['p1','p2','p3']]

        caixaV = QVBoxLayout() # Sirve para crear cada una de las cajas que tienen sus diferentes funcionalidades


        caixaV2 = QVBoxLayout()
        # Crea 4 Radio Buttons
        # Tenemos que añadirle self a cada uno para que funcionen los grupos de los botones
        self.rbtBoton1 = QRadioButton("Botón1",self)
        self.rbtBoton1.toggled.connect(self.pulsarBoton1)

        rbtBoton2 = QRadioButton("Botón2",self)
        rbtBoton3 = QRadioButton("Botón3",self)
        rbtBoton4 = QRadioButton("Botón4",self)

        # Crea 2 grupos para administrar el orden de los botones
        grupo1 = QButtonGroup(self)
        grupo2 = QButtonGroup(self)
        # Para permitir que se conecten
        grupo1.setExclusive(True)
        grupo2.setExclusive(True)

        # Añade los botones a los grupos
        grupo1.addButton(self.rbtBoton1)
        grupo1.addButton(rbtBoton2)
        grupo2.addButton(rbtBoton3)
        grupo2.addButton(rbtBoton4)



        txtCadro1 = QLineEdit() # Bloque donde podemos escribir texto
        txtCadro2 = QLineEdit() # Bloque donde podemos escribir texto

        self.cmbComboBox = QComboBox() # Lista desplegable
        self.cmbComboBox.addItems(self.nome_dni[0]) # Otra forma de hacerlo con una lista de tuples
        self.cmbComboBox.currentIndexChanged.connect(self.mandarMensajeUsuarioSeleccionado) # Que ocurre cuando seleccionamos un objeto del comboBox
        self.cmbComboBox.currentTextChanged.connect(self.textoSeleccionado)

        # Añade los 4 Radio Buttons
        caixaV2.addWidget(self.rbtBoton1)
        caixaV2.addWidget(rbtBoton2)
        caixaV2.addWidget(rbtBoton3)
        caixaV2.addWidget(rbtBoton4)
        maia.addLayout(caixaV2,0,0,1,1)

        # Crea una tabla aplicando el modelo de la clase ModeloTaboa, y le pasamos los datos creados
        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)


        maia.addWidget(clasificador,0,1,1,1)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.modelo = ModeloTabla(datos)
        self.tvwTaboa.setModel(self.modelo)

        self.seleccion = self.tvwTaboa.selectionModel()

        self.seleccion.selectionChanged.connect(self.textoSeleccionadoUsuario)



        clasificador.addTab(self.tvwTaboa, "Taboa")
        txeOutroCadroTexto = QTextEdit()
        clasificador.addTab(txeOutroCadroTexto, "Cadro de texto")

        caixaV.addWidget(txtCadro1)  # Añade en el primer cuadro, tanto el texto 1 el 2 y el desplegable
        caixaV.addWidget(txtCadro2) # Añade el segundo cuadro de texto
        caixaV.addWidget(self.cmbComboBox) # Añade la comboBox

        maia.addLayout(caixaV,1,0,1,1) # Como caixaV es layout tiene que ser addLayout

        self.txeAreaTexto = QTextEdit() # Area donde podremos introducir texto
        maia.addWidget(self.txeAreaTexto,1,1,1,1) # Aquí como txtArea no es un layout, se le añade con widget

        # MOSTRAR LO DISEÑADO ANTERIORMENTE(OBLIGATORIO)
        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()


    """
    Lo que ocurre cuando seleccionamos una opción del ComboBox
    Al seleccionar una opción mostrará tanto el nombre del usuario como su DNI
    indice: indice de cada una de las opciones del comboBox
    """
    def mandarMensajeUsuarioSeleccionado(self, indice):
        print(self.cmbComboBox.itemText(indice)) # Muestra por consola la opción escogida del comboBox
        self.txeAreaTexto.setPlainText("Has seleccionado el usuario: "+ self.cmbComboBox.itemText(indice)+ " con el dni: "+ self.nome_dni[1][indice] ) # Muestra en el bloque de texto el texto seleccionado del comboBox

    """
    Muestra el usuario seleccionado
    texto: recoge el valor del string del indice seleccionado del comboBox
    """
    def textoSeleccionado(self, texto):
        print("El combo tiene seleccionado el elemento: "+ texto)

    def textoSeleccionadoUsuario(self):

        indice = self.tvwTaboa.selectedIndexes()
        if indice is not None:
            print(self.modelo.taboa[indice[0].row()][indice[0].column()])
            self.txeAreaTexto.setPlainText(str(self.modelo.taboa[indice[0].row()][indice[0].column()]))
        else:
            print("no seleccionado")


    def pulsarBoton1(self):
        if self.rbtBoton1.isChecked():
           campos = self.txeAreaTexto.toPlainText().split(",")
           self.modelo.taboa.append([(campos[0],campos[1],True if campos[2] == 'True' else False)])
           self.modelo.layoutChanged.emit()



# EJECUTA LA VENTANA(OBLIGATORIO)
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Combo()
    aplicacion.exec()