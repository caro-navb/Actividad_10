from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origenx=0, origeny=0, destinox=0, destinoy=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origenx = origenx
        self.__origeny = origeny
        self.__destinox = destinox
        self.__destinoy = destinoy
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.distancia = distancia_euclidiana(origenx, destinox, origeny, destinoy)

    def __str__(self):
        return(
            'ID: ' + str(self.__id) + '\n' +
            'Origen x: ' + str(self.__origenx) + '\n' +
            'Origen y: ' + str(self.__origeny) + '\n' +
            'Destino x: ' + str(self.__destinox) + '\n' +
            'Destino y: ' + str(self.__destinoy) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.distancia) + '\n'
        )
