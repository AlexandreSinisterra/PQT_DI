
# PQT_DI - Ampliado (Nuevas funcionalidades)

## ComboBox

* QComboBox → lista desplegable
* addItems(lista) → añade elementos desde una lista
* currentIndexChanged → captura el índice seleccionado
* currentTextChanged → captura el texto seleccionado

Ejemplo de uso:
```
cmb = QComboBox()
cmb.addItems(["uno","dos","tres"])
cmb.currentIndexChanged.connect(funcion_indice)
cmb.currentTextChanged.connect(funcion_texto)
```
---

## TabWidget

* QTabWidget → pestañas
* addTab(widget, "nombre") → añade pestaña
* setTabPosition(QTabWidget.TabPosition.North) → posición de las pestañas

Ejemplo de uso:
```
tabs = QTabWidget()
tabs.addTab(QLabel("Contenido1"), "Pestaña 1")
tabs.addTab(QTextEdit(), "Pestaña 2")
```
---

## RadioButtons y ButtonGroup

* QRadioButton → botón de opción
* QButtonGroup → agrupa botones para que solo uno sea activo por grupo

  * setExclusive(True) → solo uno puede estar activo
* addButton(radio) → añadir botón al grupo

Ejemplo de uso:
```
radio1 = QRadioButton("Opción 1")
radio2 = QRadioButton("Opción 2")
grupo = QButtonGroup()
grupo.setExclusive(True)
grupo.addButton(radio1)
grupo.addButton(radio2)
```
---

## TableView y Modelos (QAbstractTableModel)

* QTableView → tabla visual
* QAbstractTableModel → modelo para datos dinámicos
* rowCount() → número de filas
* columnCount() → número de columnas
* data(indice, rol) → contenido según rol: DisplayRole, BackgroundRole, ForegroundRole, DecorationRole
* selectionModel().selectionChanged.connect(función) → captura selección de tabla

Roles útiles:

* DisplayRole → contenido del cell
* BackgroundRole → color de fondo
* ForegroundRole → color de texto
* DecorationRole → iconos o imágenes según el valor

Ejemplo de uso:
```
modelo = ModeloTabla(datos)
tabla = QTableView()
tabla.setModel(modelo)
tabla.selectionModel().selectionChanged.connect(funcion_seleccion)
```
---

