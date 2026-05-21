import pyperclip
import os
import datetime
import csv

numeros = []
margen = 0.05
# conteo = [[metros], [veces que ha aparecido]]
conteo = [[], []]

def deshacer(conteo):
    conteo[0].pop()
    conteo[1].pop()
    print("Deshaciendo...")

def generador():
    while True:
        entrada = input("Numero: ")
        if entrada == "d":
            deshacer(conteo)
            continue
        try:
            index = float(entrada)
        except ValueError:
            print("  Eso no es un numero valido, intenta de nuevo.")
            continue
        if index == 0:
            break
        numeros.append(index)

        for numero in numeros:
            indice = next(
                (i for i, x in enumerate(conteo[0]) if abs(numero - x) <= margen),
            None
            )
        if indice is not None:
            conteo[1][indice] += 1
        else:
            conteo[0].append(numero)
            conteo[1].append(1)

def guardar():
    projectName = input("Nombre del proyecto: ")
    hora = datetime.datetime.now()
    
    nombreArchivo = f'{hora.strftime("%d-%m-%H-%M-%f")}.csv'
    path = f'./{projectName}/{nombreArchivo}'

    try:
        os.makedirs(projectName)
        print("Carpeta creada exitosamente")
    except FileExistsError:
        print(f'Proyecto: {projectName}')
    except PermissionError:
        print(f"Permiso denegado: No fuimos capaces de crear la carpeta '{projectName}'.")
        print('Intentando de nuevo...\n')
        guardar()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        print('Intentando de nuevo...\n')
        guardar()

    print("Guardando archivo...\n")
    print(path)
    try:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for frecuencia, metros in zip(conteo[1], conteo[0]):
                writer.writerow([frecuencia, metros])
    except Exception as e:
        print(f'Un error ocurrió: {e}')


print("=== Generador de obra ===")
print("Ingresa numeros uno por uno. Escribe 0 para terminar.")
print("Usa 'd' para deshacer \n")

generador()

print(f'\nFrecuencia \t Metros')
for frecuencia, metros in zip(conteo[1], conteo[0]):
    print(f"{frecuencia}\t\t{metros}")

lineas = []
for veces, metros in sorted(zip(conteo[1], conteo[0]), reverse=True):
    lineas.append(f"{veces}\t{metros}")
texto = "\n".join(lineas)

try:
    pyperclip.copy(texto)
    print("\nResultados copiados al portapapeles. Pega con Ctrl+V en Excel.")
except Exception as e:
    print(f"\nNo se pudo copiar al portapapeles: {e}")

save = input("Deseas guardar en un archivo? s/n \n")
if save == "s":
    guardar()

input("\nPresiona Enter para salir...")
print("Te amo mi amorcito, mucha suerte con tu tarea ❤️")
