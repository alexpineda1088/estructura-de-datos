# Nombre: [Tu Nombre]
# Fecha: [Fecha de entrega]
# Hoja: 1/1

import math

class Circulo:
    """
    Clase que representa un círculo y proporciona métodos para calcular su área y perímetro.
    """
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.
        Inicializa el radio del círculo.
        :param radio: Radio del círculo.
        """
        self.radio = radio

    def calcular_area(self):
        """
        Calcula y devuelve el área del círculo.
        :return: Área del círculo.
        """
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del círculo.
        :return: Perímetro del círculo.
        """
        return 2 * math.pi * self.radio

class Rectangulo:
    """
    Clase que representa un rectángulo y proporciona métodos para calcular su área y perímetro.
    """
    def __init__(self, ancho, alto):
        """
        Constructor de la clase Rectangulo.
        Inicializa el ancho y el alto del rectángulo.
        :param ancho: Ancho del rectángulo.
        :param alto: Alto del rectángulo.
        """
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        """
        Calcula y devuelve el área del rectángulo.
        :return: Área del rectángulo.
        """
        return self.ancho * self.alto

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        :return: Perímetro del rectángulo.
        """
        return 2 * (self.ancho + self.alto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un círculo con un radio de 5 unidades
    circulo = Circulo(5)
    print("Círculo:")
    print(f"	Área: {circulo.calcular_area():.2f}")  # Imprime el área del círculo con 2 decimales
    print(f"	Perímetro: {circulo.calcular_perimetro():.2f}")  # Imprime el perímetro del círculo con 2 decimales

    # Crear un rectángulo con ancho 4 y alto 7 unidades
    rectangulo = Rectangulo(4, 7)
    print("Rectángulo:")
    print(f"	Área: {rectangulo.calcular_area()}")  # Imprime el área del rectángulo
    print(f"	Perímetro: {rectangulo.calcular_perimetro()}")  # Imprime el perímetro del rectángulo
