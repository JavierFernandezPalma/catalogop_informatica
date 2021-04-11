class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "arma de los humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "arma de los orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "escudo de los orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura de los humanos"

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png
        self.descripcion = "montura de los orcos"
        
class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

class CuerpoHumanos(Cuerpo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/cuerpo.jpg"
        self.descripcion = "cuerpo de los humanos"

class CuerpoOrcos(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"
        self.descripcion = "cuerpo de los orcos"
