import sys  # NECESARIO PARA GESTIONAR LA SALIDA DEL PROGRAMA
from PyQt6.QtWidgets import QApplication, QScrollArea, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, \
    QHBoxLayout, QCheckBox, QLineEdit, QRadioButton, QStackedLayout  # WIDGETS BÁSICOS
from PyQt6.QtCore import Qt  # PARA FLAGS COMO ALINEACIÓN


# SIGUIENTE BLOQUE SIEMPRE IGUAL ( SOLO CAMBIA EL TITULO Y EL TAMAÑO QUE YO QUIERA PONER )
class probando(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Probando para el examen")
        self.resize(700, 600)

        # ESTE BLOQUE TAMBIÉN PUEDE SER IGUAL ( ES DECIR PUEDO COPIAR Y PEGAR CASI SIEMPRE )
        # EN ESTE BLOQUE SE DEFINE EL WIDGET CENTRAL Y EL LAYOUT
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        # EL LAYOUT LO DECLARAMOS Y LO AÑADIMOS AL WIDGET CENTRAL
        layout_principal = QVBoxLayout()
        self.widget_central.setLayout(layout_principal)

        # PROBANDO NIVEL 1 ------------------------------------------------------------------------

        # AQUÍ VOY A CREAR UNA SIMPLE ETIQUETA ( LABEL ) PARA MOSTRAR UN TEXTO
        self.etiqueta = QLabel("ESTOY PROBANDO")
        # LE DOY LA PROPIEDAD DE QUE ESTÉ EN EL MEDIO
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # AÑADO EL LAYOUT ( QUE CONTIENE EL LABEL CREADO ) AL WIDGET
        layout_principal.addWidget(self.etiqueta)

        # PROBANDO NIVEL 2 ------------------------------------------------------------------------

        # VAMOS A MODIFICAR EL LABEL CREADO ANTERIORMENTE CON UN BOTÓN
        # CREAMOS EL BOTÓN CON EL CONTENIDO QUE QUEREMOS QUE TENGA
        self.boton = QPushButton("CAMBIA EL TEXTO")
        # AÑADIMOS EL LAYOUT DEL BOTÓN AL WIDGET
        layout_principal.addWidget(self.boton)
        # DEFINIMOS LA CONEXIÓN ENTRE EL BOTÓN Y LO QUE QUEREMOS QUE REALICE ( UN EVENTO )
        self.boton.clicked.connect(self.cambiar_texto)

        # EL EVENTO ESTARÁ EN LA PARTE FINAL DLE PROGRAMA ( EL METODO SE LLAMA cambiar_texto )

        # PROBANDO NIVEL 3 ------------------------------------------------------------------------------------------

        # EN ESTE NIVEL VAMOS A CREAR DISTINTOS LAYOUTS ( NO SOLO UNO PRINCIPAL )
        # PARA ELLO DEBEMOS DE CAMBIAR LA DECLARACION DEL PRINCIPIO

        # ANTES ->
        # self.layout = QVBoxLayout()
        # self.widget_central.setLayout(self.layout)
        # Y TODAS LAS DECLARACIONES SOBRE EL LAYOUT ERAN CON SELF

        # AHORA ->
        # layout_principal = QVBoxLayout()
        # self.widget_central.setLayout(layout_principal)
        # AHORA TODAS LAS DECLARACIONES VAN SOBRE LA "VARIABLE" DE LAYOUT_PRINCIPAL

        # VAMOS A REALIZAR UN TÍTULO PARA PONER EN CONTEXTO DEL NIVEL
        # CREAMOS EL LABEL
        titulo = QLabel("VAMOS A HACER LAYOUTS ANIDADOS ")
        # LO PONEMOS EN EL CENTRO
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # LE DAMOS ESTILO
        titulo.setStyleSheet("color: green; font-weight: bold; font-size: 14px;")
        # AÑADIMOS LAYOUT AL WIDGET PRINCIPAL
        layout_principal.addWidget(titulo)

        # AHORA CREAREMOS EL LAYOUT HORIZONTAL ( EN ESTE LAYOUT TENDREMOS DOS PANELES ( IZQUIERDO Y DERECHO ))

        # DECLARAMOS EL LAYOUT HORIZONTAL
        layout_horizontal = QHBoxLayout()

        # DECLARAMOS TODO EL PANEL IZQUIERDO DEL LAYOUT HORIZONTAL
        # EL PANEL IZQUIERDO VA A SER UN WIDGET
        panel_izquierdo = QWidget()
        # DECLARAMOS EL PROPIO LAYOUT DEL PANEL IZQUIERDO ( LAYOUT DEL WIDGET / PANEL IZQUIERDO )
        layout_izquierdo = QVBoxLayout()
        panel_izquierdo.setLayout(layout_izquierdo)

        # DECLARAMOS LO QUE QUEREMOS QUE CONTENGA EL EL PANEL IZQUIERDO
        # EN ESTE CASO DOS LABELS
        label1 = QLabel("ESTE ES EL PANEL IZQUIERDO")
        # LE DAMOS ESTILO AL PRIMER LABEL ( COLOR, ESTILO DE LETRA, PADDING DEL LABEL )
        label1.setStyleSheet("background-color: brown; font-weight: bold; padding: 14px;")
        # CREAMOS EL SEGUNDO LABEL
        label2 = QLabel("ESTE PANEL CONTIENE ETIQUETAS")
        label2.setStyleSheet("background-color: black; font-weight: bold; padding: 14px;")

        # AÑADIMOS EL LAYOUT IZQUIERDO AL WIDGET SELECCIONADO ANTERIORMENTE
        # SELECCIONADO CON panel_izquierdo.setLayout(layout_izquierdo)
        layout_izquierdo.addWidget(label1)
        layout_izquierdo.addWidget(label2)

        # AHORA DECLARAMOS TODO EL PANEL DERECHO
        panel_derecho = QWidget()
        layout_derecho = QVBoxLayout()
        # DECLARAMOS CUÁL QUEREMOS QUE SEA EL LAYOUT DEL PANEL DERECHO
        panel_derecho.setLayout(layout_derecho)

        # CREAREMOS UNOS CHECKBOXES EN EL LADO DERECHO
        check1 = QCheckBox("OPCION 1")
        check2 = QCheckBox("OPCION 2")
        check3 = QCheckBox("OPCION 3")

        # AÑADIMOS EL LAYOUT DE LOS CHECKBOXES AL WIDGET SELECCIONADO ANTERIORMENTE
        layout_derecho.addWidget(check1)
        layout_derecho.addWidget(check2)
        layout_derecho.addWidget(check3)

        # AÑADIMOS AMBOS PANELES ( AMBOS WIDGETS ) AL LAYOUT HORIZONTAL CREADO ANTERIORMENTE
        layout_horizontal.addWidget(panel_izquierdo)
        layout_horizontal.addWidget(panel_derecho)

        # AÑADIMOS AL LAYOUT PRINCIPAL EL LAYOUT HORIZONTAL QUE ACABAMOS DE CONFIGURAR
        layout_principal.addLayout(layout_horizontal)

        # PROBANDO NIVEL 4 -------------------------------------------------------------------------------

        # REALIZAMOS UN FORMULARIO
        # CREAMOS OTRO LAYOUT HORIZONTAL DEBAJO DONDE EDITAREMOS EL CONTENIDO DE LA FORMA DESEADA
        layout_horizontal_formulario = QHBoxLayout()  # ESTE ES EL LAYOUT DONDE TENDREMOS QUE AÑADIR EL CONTENIDO
        # ESTE EL ES PANEL DEL FORMULARIO ALIAS WIDGET
        panel_formulario = QWidget()
        # CREAMOS UN LAYOUT ESPECÍFICO PARA AÑADIR CONTENIDO DEL FORMULARIO ( LUEGO TENEMOS QUE AÑADIR ESTE LAYOUT AL LAYOUT HORIZONTAL
        layout_formulario = QVBoxLayout()
        # ADJUDICAMOS EL CONTENIDO DEL LAYOUT DEL FORMULARIO AL PANEL/WIDGET
        panel_formulario.setLayout(layout_formulario)

        # ESTABLECEMOS UN TITULO PARA EL FORMULARIO
        titulo_formulario = QLabel("FORMULARIO")
        titulo_formulario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_formulario.addWidget(titulo_formulario)

        # AÑADIMOS EL CAMPO NOMBRE AL FORMULARIO
        # CREAMOS EL LAYOUT PARA GESTIONAR EL CAMPO NOMBRE
        layout_formulario_nombre = QHBoxLayout()
        # CREAMOS EL LABEL PARA INDICAR CUAL DEBERA DE SER EL CONTENIDO DEL CAMPO
        label_nombre = QLabel("NOMBRE: ")
        # CREAMOS LA CAJA PARA INTRODUCIR EL NOMBRE
        self.txt_nombre = QLineEdit()
        # TEXTO PARA INDICAR AL USUARIO QUE DEBE PONER EN LA CAJA
        self.txt_nombre.setPlaceholderText("PON TU NOMBRE AQUÍ..")

        # AÑADIMOS EL LAYOUT ENTERO DEL NOMBRE AL WIDGET
        layout_formulario_nombre.addWidget(label_nombre)
        layout_formulario_nombre.addWidget(self.txt_nombre)
        # AÑADIMOS AL LAYOUT FORMULARIO EL LAYOUT DEL NOMBRE
        layout_formulario.addLayout(layout_formulario_nombre)

        # REALIZAMOS LO MISMO PARA EL CAMPO MAIL
        layout_formulario_mail = QHBoxLayout()
        label_mail = QLabel("EMAIL: ")
        self.txt_mail = QLineEdit()
        self.txt_mail.setPlaceholderText("tu@mail.com")

        # AÑADIMOS AL LAYOUT MAIL EL WIDGET DEL LABEL Y EL BLOQUE DONDE SE INTRODUCE EL MAIL
        layout_formulario_mail.addWidget(label_mail)
        layout_formulario_mail.addWidget(self.txt_mail)

        # AÑADIMOS EL LAYOUT DE MAIL AL LAYOUT DEL FORMULARIO
        layout_formulario.addLayout(layout_formulario_mail)

        # CREAMOS UN BOTÓN PARA ENVIAR EL FORMULARIO
        self.boton_enviar = QPushButton("ENVIAR")

        # AÑADIMOS EL WIDGET DEL BOTÓN AL LAYOUT DEL FORMULARIO
        layout_formulario.addWidget(self.boton_enviar)

        # CREAMOS UNA ETIQUETA PARA IMPRIMIR EL RESULTADO DEL ENVÍO DEL FORMULARIO
        self.label_resultado = QLabel("")
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # AÑADIMOS LA ETIQUETA DEL RESULTADO AL LAYOUT DEL FORMULARIO
        layout_formulario.addWidget(self.label_resultado)

        # CREAMOS LA CONEXIÓN ENTRE EL BOTÓN Y EL MÉTODO
        self.boton_enviar.clicked.connect(self.procesar_formulario)

        # AÑADIMOS TODO EL LAYOUT DEL FORMULARIO CREADO AL NUEVO LAYOUT HORIZONTAL Y ESTE A SU VEZ
        # - AL LAYOUT PRINCIPAL
        layout_horizontal_formulario.addLayout(layout_formulario)
        layout_horizontal_formulario.addWidget(panel_formulario)
        layout_principal.addLayout(layout_horizontal_formulario)

        # PROBANDO NIVEL 5 ----------------------------------------------------------------------

        # AÑADIMOS RADIOBUTTONS Y MÁS CHECKBOXES
        # CREAMOS EL PROPIO LAYOUT HORIZONTAL PARA EL NIVEL 5
        layout_horizontal_nivel5 = QHBoxLayout()
        # SU PROPIO PANEL
        panel_nivel5 = QWidget()
        # EL PROPIO LAYOUT VERTICAL DENTRO DEL LAYOUT HORIZONTAL
        layout_nivel5 = QVBoxLayout()
        # ASIGNAMOS EL LAYOUT VERTICAL AL PANEL ( EL WIDGET )
        panel_nivel5.setLayout(layout_nivel5)

        # AÑADIMOS UN NUEVO TITULO A LA SECCION
        titulo_nivel5 = QLabel("NIVEL 5")
        titulo_nivel5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_nivel5.setStyleSheet("color:yellow; font-weight: bold; font-size: 14pt;")
        # AÑADIMOS EL WIDGET DEL TITULO AL LAYOUT DEL NIVEL 5
        layout_nivel5.addWidget(titulo_nivel5)

        # CREAMOS UNA LÍNEA DIVISORA PARA QUE HAYA ESPACIO ENTRE EL TÍTULO Y EL SIGUIENTE CONTENIDO
        separador1 = QLabel("")
        # LE PONEMOS ALTURA AL TEXTO VACÍO
        separador1.setFixedHeight(10)
        # AÑADIMOS LE WIDGET DEL SEPARADOR AL LAYOUT DEL NIVEL 5
        layout_nivel5.addWidget(separador1)

        # CREAMOS LA SECCIÓN CHECKBOXES CON UN LABEL ( WIDGET ) QUE AÑADIMOS LA LAYOUT
        label_checkboxes = QLabel("CHECKBOES")
        layout_nivel5.addWidget(label_checkboxes)

        # CREAMOS LOS CHECKBOXES CORRESPONDIENTES
        self.checkBox1 = QCheckBox("Opcion 1")
        self.checkBox2 = QCheckBox("Opcion 2")
        self.checkBox3 = QCheckBox("Opcion 3")

        # MARCAR LA PRIMERA POR DEFECTO UNA VEZ SE INICIE EL PROGRAMA
        self.checkBox1.setChecked(True)

        # AÑADIR LOS WIDGETS ( CHECKBOXES ) AL LAYOUT DEL NIVEL 5
        layout_nivel5.addWidget(self.checkBox1)
        layout_nivel5.addWidget(self.checkBox2)
        layout_nivel5.addWidget(self.checkBox3)

        # BOTON PARA MOSTRAR EL ESTADO DE LOS CHECKBOXES
        self.boton_estado_check = QPushButton("MOSTRAR ESTADO")
        # AÑADIMOS EL WIDGET DEL BOTON AL LAYOUT
        layout_nivel5.addWidget(self.boton_estado_check)

        # ETIQUETA PARA EL RESULTADO -> ESTA ETIQUETA ATENDERÁ A UN EVENTO
        self.label_resultado_check = QLabel("...")
        self.label_resultado_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # AÑADIMOS EL WIDGET DE LA ETIQUETA
        layout_nivel5.addWidget(self.label_resultado_check)

        # CONECTAMOS LOS CHECKBOXES AL METODO PARA GENERAR EVENTOS
        # ESTE EVENTO VA A INDICAR CUANTAS CHECKBOXES MARCAMOS
        self.boton_estado_check.clicked.connect(self.mostrar_estado_checkbox)

        # CREAMOS OTRO DIVISOR
        separador2 = QLabel("")
        separador2.setFixedHeight(10)
        layout_nivel5.addWidget(separador2)

        # SECCION 2 DEL NIVEL 5 - RADIOBUTTONS
        # CREAMOS EL LABEL PARA LOS RADIOBUTTONS Y LO AÑADIMOS AL LAYOUT DEL NIVEL 5
        label_radio = QLabel("SOLO PUEDES SELECCIONAR UN RADIOBUTTON")
        layout_nivel5.addWidget(label_radio)

        # CREAMOS LOS RADIO BUTTONS
        self.radio1 = QRadioButton("Opcion 1")
        self.radio2 = QRadioButton("Opcion 2")
        self.radio3 = QRadioButton("Opcion 3")

        # DECLARAMOS QUE EL PRIMERO AL INICIAR EL PROGRAMA ESTÁ A TRUE
        self.radio1.setChecked(True)

        # LOS AÑADIMOS AL LAYOUT
        layout_nivel5.addWidget(self.radio1)
        layout_nivel5.addWidget(self.radio2)
        layout_nivel5.addWidget(self.radio3)

        # CREAMOS UN BOTON PARA MOSTRAR EL ESTADO DE LOS RADIOS
        self.boton_radios = QPushButton("MOSTRAR RESULTADO RADIOBUTTON")
        layout_nivel5.addWidget(self.boton_radios)

        # CREAMOS UNA ETIQUETA PARA EL RESULTADO = EVENTO
        self.label_resultado_radio = QLabel("...")
        self.label_resultado_radio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_nivel5.addWidget(self.label_resultado_radio)

        # CREAMOS LA CONEXION AL EVENTO
        self.boton_radios.clicked.connect(self.mostrar_estado_radios)

        # NUEVO SEPARADOR
        separador3 = QLabel("")
        separador3.setFixedHeight(20)
        layout_nivel5.addWidget(separador3)

        # SECCIÓN 3 NIVEL 5
        # BOTÓN DE RESUMEN GLOBAL
        self.boton_resumen_global = QPushButton("RESUMEN")
        # AÑADIMOS EL BOTON AL LAYOUT DE NIVEL 5
        layout_nivel5.addWidget(self.boton_resumen_global)

        # AÑADIMOS EL LABEL POR EL QUE SE INTERPOLARÁ EL RESULTADO
        self.label_resumen = QLabel("")
        self.label_resumen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_resumen.setStyleSheet("font-weight: bold;")
        layout_nivel5.addWidget(self.label_resumen)

        # CREAMOS LAS CONEXIONES PARA QUE SE ACTUALICE EL RESULTADO DE LOS ANTERIORES RESUMENES
        self.checkBox1.toggled.connect(self.actualizar_resumen)
        self.checkBox2.toggled.connect(self.actualizar_resumen)
        self.checkBox3.toggled.connect(self.actualizar_resumen)

        # AHORA LAS CONEXIONES PARA LOS RADIO
        self.radio1.toggled.connect(self.actualizar_resumen)
        self.radio2.toggled.connect(self.actualizar_resumen)
        self.radio3.toggled.connect(self.actualizar_resumen)

        # AÑADIMOS EL LA CONEXIÓN PARA QUE INTERPOLE EL LABEL DEL RESULTADO POR EL RESUMEN GLOBAL AL CLICAR EL BOTON
        self.boton_resumen_global.clicked.connect(self.mostrar_resumen_global)

        # AÑADIMOS TODO EL NIVEL 5 AL LAYOUT PRINCIPAL
        layout_horizontal_nivel5.addLayout(layout_nivel5)
        layout_horizontal_nivel5.addWidget(panel_nivel5)
        layout_principal.addLayout(layout_horizontal_nivel5)

        # NIVEL 6 PROBANDO ---------------------------------------------------------------------------------------------------------------------
        # STACKED WINDOWS
        # CREAMOS EL PROPIO LAYOUT HORIZONTAL PARA EL NIVEL 6
        layout_horizontal_nivel6 = QHBoxLayout()
        # SU PROPIO PANEL
        panel_nivel6_izquierda = QWidget()
        panel_nivel6_derecha = QWidget()

        # EL PROPIO LAYOUT VERTICAL DENTRO DEL LAYOUT HORIZONTAL
        layout_nivel6_izquierda = QVBoxLayout()
        self.layout_nivel6_derecha = QStackedLayout()

        # ASIGNAMOS LOS LAYOUTS VERTICALES A LOS PANELES ( EL WIDGET )
        panel_nivel6_izquierda.setLayout(layout_nivel6_izquierda)
        panel_nivel6_derecha.setLayout(self.layout_nivel6_derecha)

        # PANEL IZQUIERDO NIVEL 6 → BOTONES / RADIO / CHECKBOX

        # QPushButtons
        btn_vista1 = QPushButton("Vista 1")
        btn_vista2 = QPushButton("Vista 2")
        btn_vista3 = QPushButton("Vista 3")

        layout_nivel6_izquierda.addWidget(btn_vista1)
        layout_nivel6_izquierda.addWidget(btn_vista2)
        layout_nivel6_izquierda.addWidget(btn_vista3)

        # QRadioButtons
        radio1_nivel6 = QRadioButton("Rojo")
        radio2_nivel6 = QRadioButton("Verde")
        radio3_nivel6 = QRadioButton("Azul")

        layout_nivel6_izquierda.addWidget(radio1_nivel6)
        layout_nivel6_izquierda.addWidget(radio2_nivel6)
        layout_nivel6_izquierda.addWidget(radio3_nivel6)

        # QCheckBox
        chk_color_nivel6 = QCheckBox("Activar color")

        layout_nivel6_izquierda.addWidget(chk_color_nivel6)

        # SIRVE PARA RELLENAR EL SITIO SOBRANTE CON UN ESPACIO EN BLANCO
        layout_nivel6_izquierda.addStretch()

        # PANEL DERECHA NIVEL 6 → QStackedLayout

        # CREAMOS 3 PÁGINAS
        self.pag1_nivel6 = QLabel("PÁGINA 1")
        self.pag2_nivel6 = QLabel("PÁGINA 2")
        self.pag3_nivel6 = QLabel("PÁGINA 3")

        self.pag1_nivel6.setStyleSheet("background-color: lightgray;")
        self.pag2_nivel6.setStyleSheet("background-color: lightgray;")
        self.pag3_nivel6.setStyleSheet("background-color: lightgray;")

        # AÑADIR AL STACKED
        self.layout_nivel6_derecha.addWidget(self.pag1_nivel6)
        self.layout_nivel6_derecha.addWidget(self.pag2_nivel6)
        self.layout_nivel6_derecha.addWidget(self.pag3_nivel6)

        # ============================================================
        # CONEXIONES NIVEL 6
        # ============================================================

        # CAMBIAR PÁGINA CON BOTONES
        btn_vista1.clicked.connect(lambda: self.layout_nivel6_derecha.setCurrentIndex(0))
        btn_vista2.clicked.connect(lambda: self.layout_nivel6_derecha.setCurrentIndex(1))
        btn_vista3.clicked.connect(lambda: self.layout_nivel6_derecha.setCurrentIndex(2))

        # CAMBIAR COLOR SEGÚN RADIOBUTTONS + CHECKBOX
        radio1_nivel6.toggled.connect(lambda: self.cambiar_color_nivel6("red", chk_color_nivel6))
        radio2_nivel6.toggled.connect(lambda: self.cambiar_color_nivel6("green", chk_color_nivel6))
        radio3_nivel6.toggled.connect(lambda: self.cambiar_color_nivel6("blue", chk_color_nivel6))

        chk_color_nivel6.stateChanged.connect(lambda: self.cambiar_color_nivel6(None, chk_color_nivel6))

        # AÑADIMOS AMBOS PANELES AL LAYOUT HORIZONTAL DEL NIVEL 6
        layout_horizontal_nivel6.addWidget(panel_nivel6_izquierda)
        layout_horizontal_nivel6.addWidget(panel_nivel6_derecha)

        # AÑADIMOS EL LAYOUT HORIZONTAL DEL NIVEL 6 AL LAYOUT PRINCIPAL
        layout_principal.addLayout(layout_horizontal_nivel6)

        # SCROLL VERTICAL
        # CREAMOS UNA ÁREA DE SCROLL Y LE ASIGNAMOS EL WIDGET CENTRAL ACTUAL
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # PERMITE QUE EL CONTENIDO SE AJUSTE
        scroll_area.setWidget(self.widget_central)  # ¡EL MISMO WIDGET QUE YA TENÍAS!
        self.setCentralWidget(scroll_area)  # REEMPLAZA EL WIDGET CENTRAL POR EL SCROLL

    # MÉTODOS ----------------------------------------------------------------------------------------------------

    # MÉTODO PARA PROBANDO NIVEL 2 ---------------------------------------------------------------------
    # ESTE SERÍA EL METODO QUE CONECTA EL BOTÓN ( EL EVENTO EN SÍ ) ( IMPORTANTE TABULAR BIEN )
    # TIENE QUE ESTAR TABULADO AL NIVEL DE SELF INIT
    def cambiar_texto(self):
        # DEFINIMOS COMO QUEREMOS QUE CAMBIE LE TEXTO UNA VEZ CLICADO EL BOTÓN
        self.etiqueta.setText("YA NO ESTOY PROBANDO, SOY UN PRO")
        # LE DAMOS ESTILO AL LABEL ( AMARILLO Y NEGRITA )
        self.etiqueta.setStyleSheet("color:yellow; font-weight: bold;")

    # MÉTODO PARA PROBANDO NIVEL 4 --------------------------------------------------------------
    # MÉTODO QUE PROCESA EL FORMULARIO, MIRA SI LOS CAMPOS ESTAN VACIOS, DE NO ESTARLO SE MUESTRA UN MENSAJE
    # CONFORME EL FORMULARIO SE HA ENVIADO CORRECTAMENTE
    def procesar_formulario(self):
        # OBTENEMOS EL TEXTO DE LOS CAMPOS
        # .text() DEVUELVE SIEMPRE UNA CADENA STRING ( CON STRIP ELIMINAMOS ESPACIOS )
        nombre = self.txt_nombre.text().strip()
        email = self.txt_mail.text().strip()

        # VALIDAMOS QUE NO ESTÉN VACÍOS
        if not nombre or not email:
            self.label_resultado.setText("COMPLETA TODOS LOS CAMPOS CABRON")
            self.label_resultado.setStyleSheet("color:red; font-weight: bold;")
            return

        self.label_resultado.setText(f"Gracias {nombre} te contactaremos al mail : {email}")
        self.label_resultado.setStyleSheet("color:green; font-weight: bold;")

    # MÉTODOS PARA EL NIVEL 5 ----------------------------------------------------------------------
    # MÉTODO PARA LOS CHECKBOXES
    def mostrar_estado_checkbox(self):
        estado1 = "✔️" if self.checkBox1.isChecked() else "❌"
        estado2 = "✔️" if self.checkBox2.isChecked() else "❌"
        estado3 = "✔️" if self.checkBox3.isChecked() else "❌"
        texto = f"CheckBoxes: 1={estado1}, 2={estado2}, 3={estado3}"
        self.label_resultado_check.setText(texto)

    # MÉTODO PARA LOS RADIO BUTTONS
    def mostrar_estado_radios(self):
        # SOLO UNO PUEDE ESTAR MARCADO
        if self.radio1.isChecked():
            seleccion = "1"
        elif self.radio2.isChecked():
            seleccion = "2"
        else:
            seleccion = "3"
        self.label_resultado_radio.setText(f"RadioButton seleccionado: {seleccion}")

    def actualizar_resumen(self):
        # ESTE MÉTODO SE EJECUTA AUTOMÁTICAMENTE AL CAMBIAR CUALQUIER CHECK O RADIO
        # ES ÚTIL PARA MANTENER INTERFAZ EN TIEMPO REAL
        pass  # EN ESTE EJEMPLO, NO HACE NADA AUTOMÁTICO, PERO PODRÍA

        # MÉTODO PARA RESUMEN GLOBAL (AL PULSAR BOTÓN)

    def mostrar_resumen_global(self):
        # RECOGER ESTADO DE CHECKBOXES
        checks = []
        # SI SE HA CLICADO ALGUNO DE LOS CHECKBOXES... ->
        if self.checkBox1.isChecked(): checks.append("1")
        if self.checkBox2.isChecked(): checks.append("2")
        if self.checkBox3.isChecked(): checks.append("3")
        # QUE SE ALMACENE EN UNA CADENA DE TEXTO CUANTOS CHECK SE HAN MARCADO
        checks_string = ", ".join(checks) if checks else "NINGUNO"

        # RECOGER ESTADO DE RADIOBUTTONS
        if self.radio1.isChecked():
            radio = "1"
        elif self.radio2.isChecked():
            radio = "2"
        else:
            radio = "3"

        resumen = (
            f"  RESUMEN:\n"
            f"- CheckBoxes activos: {checks_string}\n"
            f"- RadioButton seleccionado: {radio}"
        )
        self.label_resumen.setText(resumen)

    # MÉTODO NIVEL 6 - FUNCIÓN PARA CAMBIAR EL COLOR A LA PÁGINA ACTUAL
    def cambiar_color_nivel6(self, color, check):
        pagina = self.layout_nivel6_derecha.currentWidget()

        if not check.isChecked():
            pagina.setStyleSheet("background-color: lightgray;")
            return

        if color is not None:
            pagina.setStyleSheet(f"background-color: {color};")


# BLOQUE DE EJECUCIÓN PRINCIPAL ( SIEMPRE IGUAL )
if __name__ == "__main__":
    # CREAR LA APLICACIÓN — SOLO UNA INSTANCIA POR PROGRAMA
    # sys.argv PERMITE PASAR ARGUMENTOS DESDE LA LÍNEA DE COMANDOS (NO SE USA AQUÍ)
    app = QApplication(sys.argv)

    # CREAR UNA INSTANCIA DE LA VENTANA
    fiestra = probando()

    # MOSTRAR LA VENTANA EN PANTALLA
    fiestra.show()

    # INICIAR EL BUCLE DE EVENTOS — "ESCUCHA" CLICKS, TECLAS, ETC.
    # app.exec() DEVUELVE UN CÓDIGO DE SALIDA (0 = ÉXITO)
    sys.exit(app.exec())