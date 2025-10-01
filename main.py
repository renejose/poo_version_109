from universidad import Universidad
from profesor import Profesor
from estudiante import Estudiante

if __name__ == "__main__":
    uni1 = Universidad("Uniersidad de Lima","454545454545","Privada")
    #crear un objeto profesor
    profe1 = Profesor("Ricardo Montenegro","458796",48,"Bases de Datos")


    #crear estudiantes
    estu1 = Estudiante("Juan","98756587",22,"adminsitracion")
    estu1.agregar_nota(18)
    estu1.agregar_nota(9)

    estu2 = Estudiante("Ricardo","945856587",32,"sistemas")
    estu2.agregar_nota(11)
    estu2.agregar_nota(9)

    #a una universidad agregarle alumnos y agrearle profesores

    uni1.agregar_persona(profe1)
    uni1.agregar_persona(estu1)
    uni1.agregar_persona(estu2)

    uni1.listar_personas()



