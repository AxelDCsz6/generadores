import pyperclip

numeros = []
margen = 0.05
# conteo = [[metros], [veces que ha aparecido]]
conteo = [[], []]

print("=== Generador de obra ===")
print("Ingresa numeros uno por uno. Escribe 0 para terminar.\n")

while True:
    entrada = input("Numero: ")
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

print(f'\nFrecuencia \t Metros')
for frecuencia, metros in zip(conteo[1], conteo[0]):
    print(f"{frecuencia}\t{metros}")

lineas = []
for veces, metros in sorted(zip(conteo[1], conteo[0]), reverse=True):
    lineas.append(f"{veces}\t{metros}")
texto = "\n".join(lineas)

try:
    pyperclip.copy(texto)
    print("\nResultados copiados al portapapeles. Pega con Ctrl+V en Excel.")
except Exception as e:
    print(f"\nNo se pudo copiar al portapapeles: {e}")

input("\nPresiona Enter para salir...")
