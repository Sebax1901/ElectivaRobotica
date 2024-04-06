# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Punto1-B.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep # Importación del módulo sleep para hacer delays

GPIO.setmode(GPIO.BCM) #BCM - Importación de los pines para llamarlos por la dirección física
GPIO.setwarnings(False) #Desactiva los mensajes 

pwmgpio13 = 13 #Use el GPIO13 en BCM = PWM1 Para la señal de PWM
pwmgpio12 = 12 #Use el GPIO13 en BCM = PWM1 Para la señal de PWM
frecuencia = 50 #Esta frecuencia la da el fabricante del servomotor SG90, o sea un T = 20ms
GPIO.setup(pwmgpio13, GPIO.OUT) #Configuro el GPIO13 como salida, o sea la señal PWM
GPIO.setup(pwmgpio12, GPIO.OUT) #Configuro el GPIO13 como salida, o sea la señal PWM
pwm1 = GPIO.PWM(pwmgpio13, frecuencia)
pwm2 = GPIO.PWM(pwmgpio12, frecuencia)

def porcentaje(angulo): #defino la función que va a calcular el procentaje desde el ángulo
    if angulo > 180 or angulo < 0: #Condicion que no se va a dar
        return False
    
    comienzo = 4
    final = 12.5

    radio = (final - comienzo) / 180 #Calculo el radio conel recorrido en tiempo para un giro de 180 grados
    angulocomoporcentaje = angulo * radio #Valor del ángulo en términos de porcentaje.

    return (comienzo + angulocomoporcentaje)

pwm1.start(porcentaje(0)) #Arranco el PWM para que el motor esté en 90 grados
pwm2.start(porcentaje(0)) #Arranco el PWM para que el motor esté en 90 grados
sleep(0.5) #Espero un segundo


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 335)
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
        self.label.setGeometry(QtCore.QRect(10, 170, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 180, 310, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_2.setObjectName("label_2")
        self.posicion = QtWidgets.QSlider(Dialog)
        self.posicion.setGeometry(QtCore.QRect(230, 80, 160, 22))
        self.posicion.setMaximum(180)
        self.posicion.setSingleStep(5)
        self.posicion.setPageStep(5)
        self.posicion.setProperty("value", 90)
        self.posicion.setSliderPosition(90)
        self.posicion.setOrientation(QtCore.Qt.Horizontal)
        self.posicion.setObjectName("posicion")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 159, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(230, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.posicion.valueChanged(self.Run)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculadora"))
        self.title_window.setText(_translate("Dialog", "Escritura de Puertos"))
        self.label.setText(_translate("Dialog", "Sebastián Camilo Ariza Rodríguez\n"
"Alejandro Melo\n"
"Yader Gamba Forero\n"
"Helmer Sierra Sierra"))
        self.label_3.setText(_translate("Dialog", "Posición del Servo"))
        self.seleccion.setItemText(0, _translate("Dialog", "Servo1"))
        self.seleccion.setItemText(1, _translate("Dialog", "Servo2"))
        self.label_4.setText(_translate("Dialog", "Selección del Servo"))
    
    def Run(self):
        global pwm1
        global pwm2
        if self.textEdit.currentText() == "Servo1":
            grados = porcentaje(float(self.posicion.value()))
            pwm1.ChangeDutyCycle(grados)
            sleep(0.1)
            pwm1.ChangeDutyCycle(0)
            sleep(0.1)
            pwm2.ChangeDutyCycle(0)
            sleep(0.1)
        if self.textEdit.currentText() == "Servo2":
            grados = porcentaje(float(self.posicion.value()))
            pwm2.ChangeDutyCycle(grados)
            sleep(0.1)
            pwm2.ChangeDutyCycle(0)
            sleep(0.1)
            pwm1.ChangeDutyCycle(0)
            sleep(0.1)

import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
