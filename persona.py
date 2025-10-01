
from abc import ABC,abstractmethod
class Persona(ABC):
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @abstractmethod
    def mostrar_info(self):
        pass