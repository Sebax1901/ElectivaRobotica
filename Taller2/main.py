import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
import cv2
from PyQt5.QtGui import QPixmap, QImage

class Ui_MainWindow(QMainWindow):
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi("Punto5-A.ui", self)  # Cargar la interfaz gráfica desde el archivo .ui
        self.pushButton.clicked.connect(self.select_image)

    def select_image(self):
        # Abrir un cuadro de diálogo para seleccionar la imagen
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            # Mostrar la imagen seleccionada en el QLabel
            self.show_image(filename)

    def show_image(self, filename):
        # Leer la imagen utilizando OpenCV
        image = cv2.imread(filename)
        # Convertir la imagen a formato RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Convertir la imagen a un formato compatible con QPixmap
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        # Mostrar la imagen en el QLabel
        self.label_3.setPixmap(pixmap)
        self.label_3.setScaledContents(True)  # Escalar la imagen para que se ajuste al QLabel
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())