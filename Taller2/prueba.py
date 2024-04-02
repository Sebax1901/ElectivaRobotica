
        self.suma_op.clicked.connect(self.Suma)
        self.resta_op.clicked.connect(self.Resta)
        self.multiplicacion_op.clicked.connect(self.Multiplicacion)
        self.cociente_op.clicked.connect(self.Cociente)
        self.residuo_op.clicked.connect(self.Residuo)

        self.limpiar.clicked.connect(self.Limpiar)



## Funciones de los botones

    def Limpiar(self):
        self.resultado.setText("")
        self.valor1.setText("")
        self.valor2.setText("")
        self.tipo_operacion.setText("?")

    def Suma(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        resultado = valor1 + valor2
        self.resultado.setText(str(resultado))
        self.tipo_operacion.setText("+")

    def Resta(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        resultado = valor1 - valor2
        self.resultado.setText(str(resultado))
        self.tipo_operacion.setText("-")
    
    def Multiplicacion(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        resultado = valor1 * valor2
        self.resultado.setText(str(resultado))
        self.tipo_operacion.setText("*")

    def Cociente(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        if valor2 != 0:
            resultado = valor1 / valor2
            self.resultado.setText(str(resultado))
            self.tipo_operacion.setText("/")
        else:
            self.resultado.setText("Error")
            self.tipo_operacion.setText("/")
    
    def Residuo(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        if valor2 != 0:
            resultado = valor1 % valor2
            self.resultado.setText(str(resultado))
            self.tipo_operacion.setText("%")
        else:
            self.resultado.setText("Error")
            self.tipo_operacion.setText("/")

    def Seno(self):
        try:
            valor1 = int(self.valor1.toPlainText())
        except:
            valor1 = 0
            self.valor1.setText("0")
        try:
            valor2 = int(self.valor2.toPlainText())
        except:
            valor2 = 0
            self.valor2.setText("0")
        resultado = valor1 / valor2
        self.resultado.setText(str(resultado))
        self.tipo_operacion.setText("/")
        self.resultado.setText("Error")
        self.tipo_operacion.setText("/")
