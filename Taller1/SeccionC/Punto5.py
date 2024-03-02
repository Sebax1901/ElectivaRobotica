import matplotlib.pyplot as plt

def LineaRecta(x0, y0, x1, y1):
    # Dibuja el vector
    plt.arrow(x0, y0, x1-x0, y1-y0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
    
    

opcion=int(input("\n¿Cuál nombre deseas?: \n\n1. Sebas\n2. Helmer\n3. Yader\n4. Alejo\n"))

plt.figure()
plt.xlim(0, 31)
plt.ylim(0, 10)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

if opcion == 1:
    
    #Letra S
    LineaRecta(1, 1, 5, 1)
    LineaRecta(5, 1, 5, 5)
    LineaRecta(5, 5, 1, 5)
    LineaRecta(1, 5, 1, 9)
    LineaRecta(1, 9, 5, 9)
    
    #Letra E
    LineaRecta(7, 1, 7, 9)
    LineaRecta(7, 9, 11, 9)
    LineaRecta(7, 5, 11, 5)
    LineaRecta(7, 1, 11, 1)
    
    #Letra B
    LineaRecta(13, 1, 13, 9)
    LineaRecta(13, 9, 17, 9)
    LineaRecta(13, 5, 17, 5)
    LineaRecta(13, 1, 17, 1)
    LineaRecta(17, 9, 17, 1)

    #Letra A
    LineaRecta(19, 1, 19, 9)
    LineaRecta(23, 1, 23, 9)
    LineaRecta(19, 9, 23, 9)
    LineaRecta(19, 5, 23, 5)

    #Letra S
    LineaRecta(25, 1, 29, 1)
    LineaRecta(29, 1, 29, 5)
    LineaRecta(29, 5, 25, 5)
    LineaRecta(25, 5, 25, 9)
    LineaRecta(25, 9, 29, 9)
    
if opcion == 2:
    #Letra H
    LineaRecta(1, 1, 1, 7)
    LineaRecta(4, 1, 4, 7)
    LineaRecta(1, 4, 4, 4)
    #Letra E
    LineaRecta(6, 1, 6, 7)
    LineaRecta(6, 7, 9, 7)
    LineaRecta(6, 4, 9, 4)
    LineaRecta(6, 1, 9, 1)
    #Letra L
    LineaRecta(11, 1, 11, 7)
    LineaRecta(11, 1, 14, 1)
    #Letra M
    LineaRecta(16, 1, 16, 7)
    LineaRecta(16, 7, 18, 4)
    LineaRecta(18, 4, 20, 7)
    LineaRecta(20, 1, 20, 7)
    #Letra E
    LineaRecta(22, 1, 22, 7)
    LineaRecta(22, 7, 25, 7)
    LineaRecta(22, 4, 25, 4)
    LineaRecta(22, 1, 25, 1)
    #Letra R
    LineaRecta(27, 1, 27, 7)
    LineaRecta(27, 7, 30, 7)
    LineaRecta(27, 4, 30, 4)
    LineaRecta(27, 4, 30, 1)
    LineaRecta(30, 4, 30, 7)

if opcion == 3:
    #Letra Y
    LineaRecta(3, 1, 3, 5)
    LineaRecta(1, 7, 3, 5)
    LineaRecta(3, 5, 5, 7)
    #Letra A
    LineaRecta(7, 1, 7, 7)
    LineaRecta(10, 1, 10, 7)
    LineaRecta(7, 4, 10, 4)
    LineaRecta(7, 7, 10, 7)
    #Letra D
    LineaRecta(12, 1, 12, 7)
    LineaRecta(15, 1, 15, 7)
    LineaRecta(12, 7, 15, 7)
    LineaRecta(12, 1, 15, 1)
    #Letra E
    LineaRecta(17, 1, 17, 7)
    LineaRecta(17, 7, 20, 7)
    LineaRecta(17, 4, 20, 4)
    LineaRecta(17, 1, 20, 1)
    #Letra R
    LineaRecta(22, 1, 22, 7)
    LineaRecta(22, 7, 25, 7)
    LineaRecta(22, 4, 25, 4)
    LineaRecta(22, 4, 25, 1)
    LineaRecta(25, 4, 25, 7)

if opcion == 4:
    #Letra A
    LineaRecta(1, 1, 1, 9)
    LineaRecta(1, 9, 5, 9)
    LineaRecta(5, 1, 5, 9)
    LineaRecta(1, 5, 5, 5)
    #Letra L
    LineaRecta(7, 1, 7, 9)
    LineaRecta(7, 1, 11, 1)
    #Letra E
    LineaRecta(13, 1, 13, 9)
    LineaRecta(13, 9, 17, 9)
    LineaRecta(13, 5, 17, 5)
    LineaRecta(13, 1, 17, 1)
    #Letra J
    LineaRecta(19, 9, 23, 9)
    LineaRecta(21, 9, 21, 1)
    LineaRecta(19, 1, 21, 1)
    #Letra O
    LineaRecta(24, 1, 24, 9)
    LineaRecta(28, 1, 28, 9)
    LineaRecta(24, 9, 28, 9)
    LineaRecta(24, 1, 28, 1)

plt.show()
