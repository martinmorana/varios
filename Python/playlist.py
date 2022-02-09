from re import T


playlist = {} # Definino diccionario de playlist vacio
playlist['canciones'] = [] # genero una lista de canciones en el diccionario

# funcion principal
def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿ como quieres que se llame la playlist ? \r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True
    while agregar_cancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agregar las canciones a la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe X para salir \r\n'
        cancion = input(pregunta)
        if cancion == "X":
            agregar_cancion = False

            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
app()
