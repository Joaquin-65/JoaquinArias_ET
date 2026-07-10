from os import system
from funciones import *




while True:
    try:
        system("pause")
        system("cls")
        juegos_ ={
            'PC':  ['Eclipse Runner', 'Puzzle Atlas', 'Racing Pulse'],
            'PS5': ['Sky Legends', 'Mistic Farm'],
            'Switch': ['Mistic Farm', 'Shadow Tactics','Sky Legends'],
            'Xbox' : ['Shadow Tactics', 'Sky Legends']
        }
        juegos_inventario = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    }

        inventario = {
        '9990' :['Eclipse Runner','G001', '7'],
        '19990':['Puzzle Atlas','G002', '0'],
        '42990':['Sky Legends','G003' '3'],
        '14990':['Racing Pulse','G004', '5'],
        '17990':['Mystic Farm','G005' '9'],
        '39990':['Shadow Tactics','G006', '2'],
        }


        print("""
========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================
""")
        opcion = int(input("Ingrese opción: "))

        match(opcion):
            case 1: 
                consulta = input("Ingrese plataforma a consultar: ").upper()
                print("El total de stock disponibles es", (len(juegos_[consulta])))
            case 2: 
                precioMin = int(input("Ingrese precio mínimo: "))
                if precioMin<=0:
                    print("Debe ingresar valores enteros")
                precioMax = int(input("Ingrese precio máximo: "))
                if precioMax<=0:
                 print("Debe ingresar valores enteros")
                
            
                print("Los juegos encontrados son: ",(inventario))
                      
            case 3: 
                while True: 
                    codigo = input("Ingrese código del juego: ")
                    Nvprecio = int(input("Ingrese nuevo precio: "))
                    if codigo and Nvprecio==juegos_inventario:
                        print("Precio actualizado con éxito")
                    else:
                        print("El código no existe")
                    resp = input("¿Desea actualizar otro precio (s/n)?: ")
                    if resp == "n":
                        break

            case 4: 
                
                code  = input("Ingrese código del juego: ")
                title = input("Ingrese título: ")
                plat  = input("Ingrese plataforma: ").upper()
                gen   = input("Ingrese género: ")
                clas  = input("Ingrese clasificacion: ").upper()
                mult  = input("¿Es multiplayer? (s/n): ").lower()
                edit  = input("Ingrese editor: ")
                pre   = int(input("Ingrese precio: "))
                stk   = int(input("Ingrese stock: "))

            case 5: pass
            case 6: 
                print("Programa finalizado.") 
                break
            case _:print("Error")


    except Exception as e:
        print(f"Error {e}")
