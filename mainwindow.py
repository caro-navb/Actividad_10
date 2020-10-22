from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador_particulas import Administrador
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administrador_particulas = Administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_agregar)
        self.ui.pushButton_3.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_4.clicked.connect(self.click_mostrar)
    
    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.administrador_particulas))

    @Slot()
    def click_agregar(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

        particula = Particula(id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.administrador_particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

        particula = Particula(id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.administrador_particulas.agregar_inicio(particula)
