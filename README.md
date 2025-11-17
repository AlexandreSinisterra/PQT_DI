# PQT_DI

Este es un pequeño diccionario a modo de resumen hecho mediante las nuevas cosas que aprendi en los ejercicios:

En la carpeta **No_me_dio_tiempo** hay mas contenido y con ejemplos simples.
## self

Se utiliza para declarar **atributos y métodos** que deben ser accesibles desde otros métodos de la clase. 
Es como ponerles ```public``` a las variables, tambien podremos acceder a ellas sin pasarlas como parametro

## Imagenes

```
        labelImagen = QLabel()
        pixmap = QPixmap("/home/dam/Descargas/jpeg(2)")
        labelImagen.setPixmap(pixmap)
        labelImagen.setScaledContents(True)
```

## QWidget

  Funciona como si fuera un div

- ```setCentralWidget```: Tienes que asignar un widget que sea el principal

Luego hay otras cosas que cuentan como widgets, como los checkbox, labels, pushbutton...

Se añaden con ```addWidget(el_widget)```

- ```QLabel```: Texto
  - ```setStyleSheet```: para poner el estilo (```setStyleSheet("background-color: red;")```)  
  - ```setAlignment```: para poner el lugar (```setAlignment(Qt.AlignmentFlag.AlignCenter)```)
  - ```setText("texto")``` : Para cambiar el texto de un widget
- ```QPushButton```: Boton
- ```QRadioButton```: Los circulitos de seleccion
- ```QCheckBox```: Checkbox
- ```QTextEdit```: Para escribir  
- ```QLineEdit```: Para escribir linea
  - ```setPlaceholderText```: Texto que se ve cuando no hay nada
- ```QComboBox```: Desplegable de opciones
  - ```addItems(["Rojo", "Verde", "Azul"])```
- ```QTabWidget```: Para pestañas
  - ```addTab(Widget, "nombre")```
- ```QButtonGroup()```: grupo de botones (si se le pasa self, actuara el exclusive solo dentro del grupo)
  - ```addButton```: añade boton
  - ```setExclusive(True)```: solo puede haber 1 activado a la vez, o se desmarcan

Esto no es un widget pero con ```.addStretch()``` podemos dejar un espacio en blanco
### Funciones
Las Funciones se escriben al final del todo y para conectarlas con el codigo se conectan a los widgets mediante
```connect```: (```el_widget.la_accion.connect(lambda: self.Nombre_funcion(parametros))```) se utiliza lambda
porque sin ella las funciones con parametros que llamamos se ejecutarian al instante.  


Los widgets tienen diferentes acciones que pueden hacer un connect:

- ```QPushButton```: clicked
- ```QRadioButton```: toggled
- ```QCheckBox```: stateChanged
- ```QComboBox```: currentIndexChanged y currentTextChanged

A la hora de escribir al función, uno de los parámetros que escribiremos aunque no se pasa directamente es ```self```:
 Un ejemplo (```def cambiar_color(self, color1, color2, color3, check):```)

Metodos que se podrian utilizar en las funciones:

- ```.text()``` : Para recoger el texto de un widget (con ```.strip()``` eliminamos espacios)
- ```.setPlainText("")```: Para cambiar el texto (tambien sirve sin el plain)
- ```.append("")```: para agregar texto
- ```.setChecked(false/true)```: cambiar si esta seleccionado
## Scroll
```
scroll_area = QScrollArea() 
scroll_area.setWidgetResizable(True) 
scroll_area.setWidget(Widget_Central) 
self.setCentralWidget(scroll_area)
```
Este codigo implementa un scroll a la ventana principal, y mete el widget central dentro de este. Al ponerlo True,
el scroll solo aparecerá cuando la ventana sea demasiado pequeña. 

Para implementarlo en otro widget es lo mismo
pero nos sobra la ultima linea, aunq debemos tener en cuenta que cuando hagamos ```.addWidget(scroll)``` no el otro 
widget



## Layout

  Funciona para decir como se van a distribuir los nuevos widgets internos y se asigna a un widget (los widgets se añaden aqui)

- ```setLayout```: Se asigna el Layout  


- ```QHBoxLayout```: De manera horizontal
- ```QVBoxLayout```: Verticalmente
- ```QStackedLayout```: Solo aparece 1 widget a la vez.
```setCurrentIndex(x)``` Se selecciona el widget que se ve.  
```currentWidget()``` se indica el widget actual.

