# Nombre del estudiante: Anderson Kaleth Lara Moralez 
# Grupo: 213022_903
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

def mostrarMenu():
    print("\n------Menú principal-----")
    print("1. Matriz ejemplo")
    print("2. Matriz vacia")
    print("3. Salir")
    opcion = int(input("Seleccione una opción(1-3): "))
    if opcion == 1:
        matrizEjemplo()
        popularReciente()
    elif opcion == 2:
        matrizVacia()
    elif opcion == 3:
        print("Programa finalizado...")
        exit()
    else:
        print("Opción no válida. Intente nuevamente.")
        mostrarMenu()
    mostrarMenu()

peliculas = {"titulos":["Robot salvaje", "Mortal Kombat", "Matilda", "Coraline", "Anabelle", "Godzilla vs Kong","Enredados"], "añoLanzamiento":["2024", "2021", "1996", "2009", "2014", "2021", "2010"],
"calificaciones":[9.9, 7.5, 6.3, 6.4, 7.8, 8.4, 6.1],
"generos":["Animación", "Acción", "Comedia", "Terror", "Terror", "Acción", "Animación"]
}

def matrizEjemplo():
    print('''==================================================================
|       Titulo      | Año lanzamiento | Calificación |   Género  |
==================================================================''')

    for i in zip(peliculas["titulos"], peliculas["añoLanzamiento"], peliculas["calificaciones"], peliculas["generos"]):
        print(f'''| {i[0]:<17} | {i[1]:<15} | {i[2]:<12} | {i[3]:<9} |
|___________________|_________________|______________|___________|''')

def matrizVacia():
    espaciosVacios = { "titulos":[], "añoLanzamiento":[], "calificaciones":[], "generos":[] }
    filas = int(input("Cantidad de titulos que desea ingresar: "))
    for i in range(filas):
        titulo = input("Ingrese el título de la película: ").strip()
        while titulo == "":
            print("El titulo no debe estar vacio")
            titulo = input("Ingrese un titulo valido: ").strip()
        while True:
            try:
                año = int(input("Ingrese el año de lanzamiento: "))
                if año <= 1900 or año >= 2026:
                    print("Ingrese un año superior a 1900 e inferior a 2026")
                else:
                    break
            except ValueError:
                print("Ingrese un año de lanzamiento valido")
        calificacion = float(input("Ingrese la calificación(1-10): "))
        while calificacion < 1 or calificacion > 10:
            print("Debe escoger una calificación entre 1 y 10")
            calificacion = float(input("Ingrese una calificación valida: "))
        genero = input("Ingrese el genero: ")
        espaciosVacios["titulos"].append(titulo)
        espaciosVacios["añoLanzamiento"].append(año)
        espaciosVacios["calificaciones"].append(calificacion)
        espaciosVacios["generos"].append(genero)
    print('''==================================================================
|       Titulo      | Año lanzamiento | Calificación |   Género  |
==================================================================''')
    for i in zip(espaciosVacios["titulos"], espaciosVacios["añoLanzamiento"], espaciosVacios["calificaciones"], espaciosVacios["generos"]):
        print(f'''| {i[0]:<17} | {i[1]:<15} | {i[2]:<12} | {i[3]:<9} |
|___________________|_________________|______________|___________|''')

def popularReciente():
    resultado = []
    for titulo, calificacion, año in zip(peliculas["titulos"], peliculas["calificaciones"], peliculas["añoLanzamiento"]):
        if calificacion >= 7 and año >= "2020":
            resultado.append(titulo)
    print("\n------Peliculas populares y recientes-----")
    for i in resultado:
        print("-", i)         

mostrarMenu()