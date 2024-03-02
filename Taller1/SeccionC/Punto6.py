import cv2

# Asegúrate de que la ruta del archivo sea correcta
chevrolet = cv2.imread('./chevrolet.png')
#Binarizar la imagen
imgCanny = cv2.Canny(chevrolet, 10, 50)
imgCannyBGR = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)
#Encontrar contornos
contornos , jerarquia = cv2.findContours(imgCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("**** Coordenadas de los contornos del logo de Chevrolet ****")
print(contornos)

#Dibujar contornos 
cv2.drawContours(imgCannyBGR, contornos, -1, (200,0,0), 3)
cv2.imshow("Imagen", imgCannyBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Asegúrate de que la ruta del archivo sea correcta
hyundai = cv2.imread('./hyundai.png')
#Binarizar la imagen
imgCannyH = cv2.Canny(hyundai, 10, 50)
imgCannyBGR2 = cv2.cvtColor(imgCannyH, cv2.COLOR_GRAY2BGR)
#Encontrar contornos
contornos2 , jerarquia = cv2.findContours(imgCannyH, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("**** Coordenadas de los contornos del logo de Hyundai ****")
print(contornos2)

#Dibujar contornos 
cv2.drawContours(imgCannyBGR2, contornos2, -1, (200,0,0), 3)
cv2.imshow("Imagen", imgCannyBGR2)
cv2.waitKey(0)
cv2.destroyAllWindows()