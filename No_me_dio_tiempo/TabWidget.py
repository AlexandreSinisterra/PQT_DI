import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QTextEdit, QVBoxLayout, QWidget


class DemoTabs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabWidget Demo")

        tabs = QTabWidget()
        tabs.addTab(QLabel("Contenido de la primera pestaña"), "Pestaña 1")
        tabs.addTab(QTextEdit(), "Pestaña 2")

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = DemoTabs()
window.show()
sys.exit(app.exec())
