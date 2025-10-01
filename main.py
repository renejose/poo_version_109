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
    print()
    uni1.listar_personas()
    print()
    uni1.listar_estudiantes()
    print()
    uni1.listar_profesores()
    print()
    uni1.buscar_estudiante("Juan")
    uni1.buscar_estudiante("Ricardo")
    uni1.buscar_estudiante("12312")
    uni1.buscar_estudiante(2123)
    print()
    uni1.buscar_estudiantes_por_inicial("J")
    uni1.buscar_estudiantes_por_inicial("R")
    uni1.buscar_estudiantes_por_inicial("X")
    uni1.buscar_estudiantes_por_inicial(5)
    uni1.buscar_estudiantes_por_inicial("Ju")
    print()
    uni1.total_personas()
