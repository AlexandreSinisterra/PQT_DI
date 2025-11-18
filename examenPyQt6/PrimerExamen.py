import sys
from contextlib import nullcontext
from xmlrpc.client import boolean

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Probando para el examen")
        self.resize(700, 600)

        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        layout_principal = QVBoxLayout()
        self.widget_central.setLayout(layout_principal)

        gpbCliente = QGroupBox("Cliente")
        layout_panel_superior = QVBoxLayout(gpbCliente)


        widget_NCnome = QWidget()
        layout_NCnome = QHBoxLayout()
        widget_NCnome.setLayout(layout_NCnome)

        self.lblNumeroCliente = QLabel("Número Cliente")
        self.txtNumeroCliente = QLineEdit()
        self.lblNomeCliente = QLabel("Nome")
        self.txtNomeCliente = QLineEdit()

        layout_NCnome.addWidget(self.lblNumeroCliente)
        layout_NCnome.addWidget(self.txtNumeroCliente)
        layout_NCnome.addWidget(self.lblNomeCliente)
        layout_NCnome.addWidget(self.txtNomeCliente)

        layout_panel_superior.addWidget(widget_NCnome)


        widget_Apelidos = QWidget()
        layout_Apelidos = QHBoxLayout()
        widget_Apelidos.setLayout(layout_Apelidos)

        self.lblApelidosCliente = QLabel("Apelidos")
        self.txtApelidosCliente = QLineEdit()

        layout_Apelidos.addWidget(self.lblApelidosCliente)
        layout_Apelidos.addWidget(self.txtApelidosCliente)

        layout_panel_superior.addWidget(widget_Apelidos)


        widget_Dirección = QWidget()
        layout_Dirección = QHBoxLayout()
        widget_Dirección.setLayout(layout_Dirección)

        self.lblDirección = QLabel("Dirección")
        self.txtDirección = QLineEdit()

        layout_Dirección.addWidget(self.lblDirección)
        layout_Dirección.addWidget(self.txtDirección)

        layout_panel_superior.addWidget(widget_Dirección)


        widget_CP = QWidget()
        layout_CP = QHBoxLayout()
        widget_CP.setLayout(layout_CP)

        self.lblCidade = QLabel("Cidade")
        self.txtCidade = QLineEdit()
        self.lblProvinciaEstado = QLabel("Provincia")
        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["","A Coruña", "Lugo", "Ourense", "Pontevedra"])
        layout_CP.addWidget(self.lblCidade)
        layout_CP.addWidget(self.txtCidade)
        layout_CP.addWidget(self.lblProvinciaEstado)
        layout_CP.addWidget(self.cmbProvincia)

        layout_panel_superior.addWidget(widget_CP)


        layout_principal.addWidget(gpbCliente)


        widget_TextoCuadradoYBotones = QWidget()
        layout_TextoCuadradoYBotones = QHBoxLayout()
        widget_TextoCuadradoYBotones.setLayout(layout_TextoCuadradoYBotones)

        self.txeClientes = QTextEdit()
        layout_TextoCuadradoYBotones.addWidget(self.txeClientes)


        widget_BotonesDelTexto = QWidget()
        layout_BotonesDelTexto = QVBoxLayout()
        widget_BotonesDelTexto.setLayout(layout_BotonesDelTexto)

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(lambda:  self.añadirInfo())
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        layout_BotonesDelTexto.addWidget(btnEngadir)
        layout_BotonesDelTexto.addWidget(btnEditar)
        layout_BotonesDelTexto.addWidget(btnBorrar)

        layout_BotonesDelTexto.addStretch()

        layout_TextoCuadradoYBotones.addWidget(widget_BotonesDelTexto)


        layout_principal.addWidget(widget_TextoCuadradoYBotones)


        widget_AC = QWidget()
        layout_AC = QHBoxLayout()
        widget_AC.setLayout(layout_AC)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        layout_AC.addStretch()

        layout_AC.addWidget(btnCancelar)
        layout_AC.addWidget(btnAceptar)

        layout_principal.addWidget(widget_AC)


    def añadirInfo(self):

        NC = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apelidos = self.txtApelidosCliente.text()
        txtDirección = self.txtDirección.text()
        txtCidade = self.txtCidade.text()
        cmbProvincia = self.cmbProvincia.currentText()

        if (self.validacion(NC,nome,apelidos,txtDirección,txtCidade,cmbProvincia)):

            texto = (
            f"{NC},{nome},{apelidos},{txtDirección}.{txtCidade},{cmbProvincia}"
            )
            self.txeClientes.append(texto)

        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDirección.clear()
        self.txtCidade.clear()
        self.cmbProvincia.clear()
        self.cmbProvincia.addItems(["","A Coruña", "Lugo", "Ourense", "Pontevedra"])

    def validacion(self,NC,nome,apelidos,txtDirección,txtCidade,cmbProvincia):
        boolean = True
        if (NC=="" or nome=="" or apelidos=="" or txtDirección=="" or txtCidade=="" or cmbProvincia==""):
            boolean = False
            if (NC==""):
                self.lblNumeroCliente.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            if (nome==""):
                self.lblNomeCliente.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            if (apelidos==""):
                self.lblApelidosCliente.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            if (txtDirección==""):
                self.lblDirección.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            if (txtCidade==""):
                self.lblCidade.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            if (cmbProvincia == ""):
                self.lblProvinciaEstado.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
        return boolean






if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()

    aplicacion.exec()