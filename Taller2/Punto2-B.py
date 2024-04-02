from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO #Importación de los pines GPIO
from time import sleep # Importación del módulo sleep para hacer delays

GPIO.setmode(GPIO.BCM) #BCM - Importación de los pines para llamarlos por la dirección física
GPIO.setwarnings(False) #Desactiva los mensajes 

led_amarilloGPIO = 23
GPIO.setup(led_amarilloGPIO, GPIO.OUT)
led_rojoGPIO = 24
GPIO.setup(led_rojoGPIO, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
led_verdeGPIO = GPIO.PWM(13, 100)
led_verdeGPIO.start(50)
GPIO.setup(12, GPIO.OUT)
led_azulGPIO = GPIO.PWM(12, 100)
led_azulGPIO.start(50)

estado_amarillo = 0
estado_rojo = 0

GPIO.output(led_amarilloGPIO, GPIO.LOW)
GPIO.output(led_rojoGPIO, GPIO.LOW)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 451)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.title_window = QtWidgets.QLabel(Dialog)
        self.title_window.setGeometry(QtCore.QRect(34, 30, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.title_window.setFont(font)
        self.title_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_window.setAutoFillBackground(False)
        self.title_window.setAlignment(QtCore.Qt.AlignCenter)
        self.title_window.setObjectName("title_window")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 300, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 310, 310, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_2.setObjectName("label_2")
        self.led_amarillo = QtWidgets.QPushButton(Dialog)
        self.led_amarillo.setGeometry(QtCore.QRect(120, 80, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.led_amarillo.setFont(font)
        self.led_amarillo.setObjectName("led_amarillo")
        self.led_rojo = QtWidgets.QPushButton(Dialog)
        self.led_rojo.setGeometry(QtCore.QRect(290, 80, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.led_rojo.setFont(font)
        self.led_rojo.setObjectName("led_rojo")
        self.led_verde = QtWidgets.QSlider(Dialog)
        self.led_verde.setGeometry(QtCore.QRect(200, 180, 160, 22))
        self.led_verde.setMaximum(100)
        self.led_verde.setSingleStep(10)
        self.led_verde.setPageStep(20)
        self.led_verde.setSliderPosition(50)
        self.led_verde.setOrientation(QtCore.Qt.Horizontal)
        self.led_verde.setObjectName("led_verde")
        self.led_azul = QtWidgets.QSlider(Dialog)
        self.led_azul.setGeometry(QtCore.QRect(200, 230, 160, 22))
        self.led_azul.setMaximum(100)
        self.led_azul.setSingleStep(10)
        self.led_azul.setPageStep(20)
        self.led_azul.setSliderPosition(50)
        self.led_azul.setOrientation(QtCore.Qt.Horizontal)
        self.led_azul.setObjectName("led_azul")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 86, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 86, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.led_amarillo.clicked.connect(self.LedAmarillo)
        self.led_rojo.clicked.connect(self.LedRojo)
        self.led_azul.valueChanged.connect(self.LedAzul)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LEDS"))
        self.title_window.setText(_translate("Dialog", "Escritura de Puertos"))
        self.label.setText(_translate("Dialog", "Sebastián Camilo Ariza Rodríguez\n"
"Alejandro Melo\n"
"Yader Gamba Forero\n"
"Helmer Sierra Sierra"))
        self.led_amarillo.setText(_translate("Dialog", "Led amarillo"))
        self.led_rojo.setText(_translate("Dialog", "Led Rojo"))
        self.label_3.setText(_translate("Dialog", "Led verde"))
        self.label_4.setText(_translate("Dialog", "Led Azul"))
        self.led_amarillo.setStyleSheet('QPushButton {background-color: yellow; color: black;}')
        self.led_rojo.setStyleSheet('QPushButton {background-color: red; color: black;}')
    
    def LedAmarillo(self):
        global estado_amarillo
        if estado_amarillo == 0:
            GPIO.output(led_amarilloGPIO, GPIO.HIGH)
            estado_amarillo = 1
        elif estado_amarillo == 1:
            GPIO.output(led_amarilloGPIO, GPIO.LOW)
            estado_amarillo = 0
    
    def LedRojo(self):
        global estado_rojo
        if estado_rojo == 0:
            GPIO.output(led_rojoGPIO, GPIO.HIGH)
            estado_rojo = 1
        elif estado_rojo == 1:
            GPIO.output(led_rojoGPIO, GPIO.LOW)
            estado_rojo = 0
    
    def LedAzul(self):
        potencia = float(self.led_azul.value())
        led_azulGPIO.ChangeDutyCycle(potencia)
        sleep(0.02)

    def LedRojo(self):
        potencia = float(self.led_verde.value())
        led_verdeGPIO.ChangeDutyCycle(potencia)
        sleep(0.02)
        
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
