from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy                                #Libreria para realizar el manejo de las funciones
import matplotlib.pyplot as plt             #Libreria requerida para generar las graficas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('Qt5Agg')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1162, 829)
        Form.setAutoFillBackground(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainWindow = QtWidgets.QFrame(Form)
        self.MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainWindow.setAutoFillBackground(False)
        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWindow.setObjectName("MainWindow")
        self.Boton_Graficar = QtWidgets.QPushButton(self.MainWindow)
        self.Boton_Graficar.setGeometry(QtCore.QRect(860, 200, 201, 81))
        self.Boton_Graficar.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"background-color: rgb(219, 255, 249);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"\n"
"")
        self.Boton_Graficar.setObjectName("Boton_Graficar")
        self.textBrowser = QtWidgets.QTextBrowser(self.MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(270, 680, 211, 141))
        self.textBrowser.setStyleSheet("border: 1px solid #ffffff;\n"
"alternate-background-color: rgb(85, 255, 255);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.MainWindow)
        self.label.setGeometry(QtCore.QRect(550, 650, 241, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Base_Grafica = QtWidgets.QFrame(self.MainWindow)
        self.Base_Grafica.setGeometry(QtCore.QRect(80, 80, 761, 561))
        self.Base_Grafica.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"\n"
"")
        self.Base_Grafica.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Base_Grafica.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Base_Grafica.setObjectName("Base_Grafica")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Base_Grafica)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 100, 721, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Grafica = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Grafica.setContentsMargins(0, 0, 0, 0)
        self.Grafica.setObjectName("Grafica")
        self.Titulo = QtWidgets.QLabel(self.Base_Grafica)
        self.Titulo.setGeometry(QtCore.QRect(210, 30, 331, 41))
        self.Titulo.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.Titulo.setObjectName("Titulo")
        self.Lista_Funciones = QtWidgets.QComboBox(self.MainWindow)
        self.Lista_Funciones.setGeometry(QtCore.QRect(870, 340, 201, 31))
        self.Lista_Funciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Lista_Funciones.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"")
        self.Lista_Funciones.setObjectName("Lista_Funciones")
        self.Lista_Funciones.addItem("Seno")
        self.Lista_Funciones.addItem("Coseno")
        self.Lista_Funciones.addItem("Tangente")
        self.Lista_Funciones.addItem("Cotangente")
        self.Lista_Funciones.addItem("Secante")
        self.Lista_Funciones.addItem("Cosecante")
        self.Valor_Minimo = QtWidgets.QTextEdit(self.MainWindow)
        self.Valor_Minimo.setGeometry(QtCore.QRect(870, 480, 131, 51))
        self.Valor_Minimo.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;")
        self.Valor_Minimo.setObjectName("Valor_Minimo")
        self.Valor_Maximo = QtWidgets.QTextEdit(self.MainWindow)
        self.Valor_Maximo.setGeometry(QtCore.QRect(1010, 480, 131, 51))
        self.Valor_Maximo.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"")
        self.Valor_Maximo.setObjectName("Valor_Maximo")
        self.Min = QtWidgets.QLabel(self.MainWindow)
        self.Min.setGeometry(QtCore.QRect(890, 430, 101, 41))
        self.Min.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 127);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"")
        self.Min.setObjectName("Min")
        self.Max = QtWidgets.QLabel(self.MainWindow)
        self.Max.setGeometry(QtCore.QRect(1020, 430, 101, 41))
        self.Max.setStyleSheet("font: 8pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 127);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #000000;\n"
"border-radius:10px;")
        self.Max.setObjectName("Max")
        self.Nota = QtWidgets.QTextEdit(self.MainWindow)
        self.Nota.setGeometry(QtCore.QRect(880, 570, 251, 61))
        self.Nota.setStyleSheet("border: none")
        self.Nota.setObjectName("Nota")
        self.horizontalLayout.addWidget(self.MainWindow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Toma de valores para manejo en las funciones
        self.Boton_Graficar.clicked.connect(self.Click_Boton)                           #Comando para lamar a la funcion que ejecutara el codigo
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Boton_Graficar.setText(_translate("Form", "Graficar"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sebastián Camilo Ariza </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Alejandro Melo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Yader Gamba Forero</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Helmer Sierra Sierra</span></p></body></html>"))
        self.Titulo.setText(_translate("Form", "GRAFICADOR DE FUNCIONES"))
        self.Lista_Funciones.setItemText(0, _translate("Form", "Seno"))
        self.Lista_Funciones.setItemText(1, _translate("Form", "Coseno"))
        self.Lista_Funciones.setItemText(2, _translate("Form", "Tangente"))
        self.Lista_Funciones.setItemText(3, _translate("Form", "Cotangente"))
        self.Lista_Funciones.setItemText(4, _translate("Form", "Secante"))
        self.Lista_Funciones.setItemText(5, _translate("Form", "Cosecante"))
        self.Min.setText(_translate("Form", "Min (Pi*Rad)"))
        self.Max.setText(_translate("Form", "Max (Pi*Rad)"))


    
    
    def Click_Boton(self):                                              #Funcion para cuando se de clic al boton
        seleccion=self.Lista_Funciones.currentIndex()                            #Entrega el indice de la funcion dentro de combo box
        VMax=self.Valor_Maximo.toPlainText()                                     # Leemos el valor maximo del edit text
        VMin=self.Valor_Minimo.toPlainText()                                     # Leemos el valor ninimo del edit text
        print(VMax)
        print(VMin)
        a=int(VMin)*numpy.pi                                                    # Valor de inicio de la funcion
        b=int(VMax)*numpy.pi                                                    # Valor de fin de la funcion
        esp=2                                                                   # Valor de espacio de puntos de la funcion
        x=numpy.linspace(a,b,int(360/esp+1))                                    # Punto inicial / Punto final / Espaciamiento de los puntos de la grafica en este caso 13 puntos con 12 intervalos Forzamos que el numero se antero

        match seleccion:
                case 0:
                        self.limpiar_Grafica()
                        Funcion=numpy.sin(x)
                        plt.grid()                                              #Miestra la frafica de los valores
                        self.fig, self.ax = plt.subplots()                      # Declaramos la figura
                        self.ax.plot(x, Funcion)                                #Asignamos los valores a la figura
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',  # Damos nombre a los ejes
                        title='Funcion Seno')                                   # Colocamos el titulo de la grafica
                        self.Graf = FigureCanvas(self.fig)                    # Convertimos la figura de un objeto en Matplotlib a PyQt5
                        self.Grafica.addWidget(self.Graf)                     # Agreamso la grafica al Layout
                        
                case 1:
                        self.limpiar_Grafica()
                        Funcion=numpy.cos(x)
                        plt.grid(True)
                        self.fig, self.ax = plt.subplots()
                        self.ax.plot(x, Funcion)
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',
                        title='Funcion Coseno')
                        self.canvas = FigureCanvas(self.fig)
                        self.Grafica.addWidget(self.canvas)                        
                case 2:
                        self.limpiar_Grafica()
                        Funcion=numpy.tan(x)
                        plt.grid(True)
                        self.fig, self.ax = plt.subplots()
                        self.ax.plot(x, Funcion)
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',
                        title='Funcion Tangente')
                        self.canvas = FigureCanvas(self.fig)
                        self.Grafica.addWidget(self.canvas) 
                case 3:
                        self.limpiar_Grafica()
                        print('Cotangente')
                        Funcion=numpy.arctan(x)
                        plt.grid(True)
                        self.fig, self.ax = plt.subplots()
                        self.ax.plot(x, Funcion)
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',
                        title='Funcion Cotangente')
                        self.canvas = FigureCanvas(self.fig)
                        self.Grafica.addWidget(self.canvas)  
                case 4:
                        self.limpiar_Grafica()
                        print('Secante')
                        Funcion=numpy.arccos(x)
                        plt.grid(True)
                        self.fig, self.ax = plt.subplots()
                        self.ax.plot(x, Funcion)
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',
                        title='Funcion Secante')
                        self.canvas = FigureCanvas(self.fig)
                        self.Grafica.addWidget(self.canvas) 
                case 5:
                        self.limpiar_Grafica()
                        print('Cosecante')
                        Funcion=numpy.arcsin(x)
                        plt.grid(True)
                        self.fig, self.ax = plt.subplots()
                        self.ax.plot(x, Funcion)
                        self.ax.set(xlabel='Posicion πRad', ylabel='Amplitud',
                        title='Funcion Cosecante')
                        self.canvas = FigureCanvas(self.fig)
                        self.Grafica.addWidget(self.canvas) 
                case _:
                        print('El valor no es valido')

    def limpiar_Grafica(self):
        # Eliminar todos los widgets del layout
        for i in reversed(range(self.Grafica.count())):
            widget = self.Grafica.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

def seno(i):                                                            #Declaramos la variable para seno
        return numpy.sin(i)                                             #Pedimos que nos devuelva el valor de la funcion

def coseno(i):
        return numpy.cos(i)

def tangente(i):
        return numpy.tan(i)

def cotangente(i):
        return 1/(numpy.tan(i))

def secante(i):
        return 1/(numpy.cos(i))

def cosecante(i):
        return 1/(numpy.sin(i))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



