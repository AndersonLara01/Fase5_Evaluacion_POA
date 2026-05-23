# Nombre del estudiante: Anderson Kaleth Lara Moralez 
# Grupo: 213022_903
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

peliculas = { "titulo":["Robot salvaje", "Mortal Kombat", "Matilda", "Coraline", "Godzilla vs Kong", "Enredados"], "añoLanzamiento":["2024", "2021", "1996", "2009", "2021", "2010"],
"calificacion":[9.9, 7.5, 6.3, 6.4, 8.4, 6.1],
"genero":["Animación", "Acción", "Comedia", "Terror", "Acción", "Animación"]
}

print('''==================================================================
|       Titulo      | Año lanzamiento | Calificación |   Género  |
==================================================================''')

for i in zip(peliculas["titulo"], peliculas["añoLanzamiento"], peliculas["calificacion"], peliculas["genero"]):
    print(f'''| {i[0]:<17} | {i[1]:<15} | {i[2]:<12} | {i[3]:<9} |
|___________________|_________________|______________|___________|''')

def popularReciente():
    resultado = []
    for nombre, puntaje, año in zip(peliculas["titulo"], peliculas["calificacion"], peliculas["añoLanzamiento"]):
        if puntaje >= 7 and año >= "2010":
            resultado.append(nombre)


popularReciente()