from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 683)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.title_window = QtWidgets.QLabel(Dialog)
        self.title_window.setGeometry(QtCore.QRect(34, 30, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.title_window.setFont(font)
        self.title_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_window.setAutoFillBackground(False)
        self.title_window.setAlignment(QtCore.Qt.AlignCenter)
        self.title_window.setObjectName("title_window")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 510, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 510, 310, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(320, 80, 151, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 267, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 110, 461, 331))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/cilindrico.jpg"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.description = QtWidgets.QLabel(Dialog)
        self.description.setGeometry(QtCore.QRect(40, 430, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.description.setFont(font)
        self.description.setObjectName("description")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tipos de Robot"))
        self.title_window.setText(_translate("Dialog", "Tipos de Robot"))
        self.label.setText(_translate("Dialog", "Sebastián Camilo Ariza Rodríguez\n"
"Alejandro Melo\n"
"Yader Gamba Forero\n"
"Helmer Sierra Sierra"))
        self.comboBox.setItemText(0, _translate("Dialog", "Cartesiano"))
        self.comboBox.setItemText(1, _translate("Dialog", "Esferico"))
        self.comboBox.setItemText(2, _translate("Dialog", "Cilindrico"))
        self.label_3.setText(_translate("Dialog", "Seleccione el tipo de robot a visualizar"))
        initial_text = "Robot Cartesiano:\nRobot de tipo PPP. Cuenta con tres articulaciones prismáticas."
        self.description.setText(_translate("Dialog", initial_text))

import cartesiano_rc
import logo_rc
import cilindrico
import esferico

def RefreshWindow():
    valor = ui.comboBox.currentText()
    if valor == "Cartesiano":
        ui.label_4.setPixmap(QtGui.QPixmap(":/images/cartesiano.png"))
        text = "Robot Cartesiano:\nRobot de tipo PPP. Cuenta con tres articulaciones prismáticas."
        ui.description.setText(text)
    elif valor == "Esferico":
        ui.label_4.setPixmap(QtGui.QPixmap(":/images/esferico.jpg"))
        text = "Robot Esférico:\nRobot de tipo RRP. Cuenta con dos articulaciones rotacionales y una articulación prismática."
        ui.description.setText(text)
    elif valor == "Cilindrico":
        ui.label_4.setPixmap(QtGui.QPixmap(":/images/cilindrico.jpg"))
        text = "Robot Cilíndrico:\nRobot de tipo RPP. Cuenta con dos articulaciones prismáticas y una articulación rotacional."
        ui.description.setText(text)

# Crea un QTimer
timer = QTimer()
timer.timeout.connect(RefreshWindow)  # Conecta el temporizador a la función cambiar_estilo
timer.start(100)  # Establece el temporizador para que se ejecute cada 1000 milisegundos (1 segundo)

def Run():
    ui.label_4.setPixmap(QtGui.QPixmap(":/images/cartesiano.png"))
    Dialog.show()
    timer.start()  # Inicia el temporizador si aún no está corriendo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Run()
    sys.exit(app.exec_())
