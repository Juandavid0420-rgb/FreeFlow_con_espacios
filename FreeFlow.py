# FreeFlow - Juego de conexiones lógicas en una grilla
# Autor: Proyecto de curso Análisis de Algoritmos
# Descripción: Juego en consola que permite a un jugador (humano o sintético) resolver tableros del juego FreeFlow

from collections import deque
from colorama import init, Fore, Style
from copy import deepcopy
import sys

# Inicializa colorama para colores en consola
init(autoreset=True)

# ===========================
# FUNCION: leer_archivo()
# ===========================
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        raise

    primera_linea = lineas[0].strip().replace(',', ' ')
    n, _ = map(int, primera_linea.split())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    pairs = {}

    for linea in lineas[1:]:
        fila, col, valor = map(int, linea.strip().replace(',', ' ').split())
        fila -= 1
        col -= 1
        grid[fila][col] = valor
        if valor in pairs:
            pairs[valor].append((fila, col))
        else:
            pairs[valor] = [(fila, col)]

    return grid, pairs, n

# ===========================
# FUNCION: mostrar_tablero_coloreado()
# ===========================
def mostrar_tablero_coloreado(grid, n):
    colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    print("  " + " ".join(str(i + 1) for i in range(n)))
    for i in range(n):
        fila = f"{i + 1} "
        for j in range(n):
            val = grid[i][j]
            if val == 0:
                fila += ". "
            else:
                color = colores[(val - 1) % len(colores)]
                fila += f"{color}{val} {Style.RESET_ALL}"
        print(fila)

# ===========================
# FUNCION: es_camino_valido()
# ===========================
def es_camino_valido(grid, par, celdas, pairs):
    if not celdas:
        return False

    inicio, fin = pairs[par]

    if celdas[0] not in [inicio, fin] or celdas[-1] not in [inicio, fin]:
        return False

    if celdas[0] == celdas[-1]:
        return False

    for i in range(len(celdas) - 1):
        r1, c1 = celdas[i]
        r2, c2 = celdas[i + 1]
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            return False

    puntos_ocupados = set()
    for p, posiciones in pairs.items():
        if p != par:
            puntos_ocupados.update(posiciones)

    for r, c in celdas:
        if (r, c) not in [inicio, fin] and grid[r][c] != 0 and grid[r][c] != par:
            return False
        if (r, c) in puntos_ocupados and (r, c) not in [inicio, fin]:
            return False

    return True

# ===========================
# FUNCION: trazar_camino()
# ===========================
def trazar_camino(grid, par, celdas):
    for r, c in celdas:
        grid[r][c] = par

# ===========================
# FUNCION: encontrar_caminos()
# ===========================
def encontrar_caminos(grid, n, inicio, fin):
    caminos = []
    cola = deque()
    cola.append((inicio, [inicio]))

    while cola:
        (r, c), path = cola.popleft()
        if (r, c) == fin:
            caminos.append(path)
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in path:
                if grid[nr][nc] == 0 or (nr, nc) == fin:
                    cola.append(((nr, nc), path + [(nr, nc)]))

    return caminos

# ===========================
# FUNCION: resolver_juego()
# ===========================
def resolver_juego(grid, pairs, n):
    pares = list(pairs.items())

    def backtrack(index):
        if index == len(pares):
            return True  # Todos los pares han sido conectados

        par, (inicio, fin) = pares[index]
        caminos = encontrar_caminos(grid, n, inicio, fin)

        for camino in caminos:
            if es_camino_valido(grid, par, camino, pairs):
                celdas_backup = [(r, c, grid[r][c]) for r, c in camino if (r, c) not in [inicio, fin]]
                trazar_camino(grid, par, camino)
                if backtrack(index + 1):
                    return True
                # Retroceso (deshacer cambios)
                for r, c, val in celdas_backup:
                    grid[r][c] = 0

        return False

    return backtrack(0)


# ===========================
# FUNCION: main()
# ===========================
def main():
    archivo = sys.argv[1] if len(sys.argv) > 1 else "tableros/tablero2_medio.txt"
    try:
        grid, pairs, n = leer_archivo(archivo)
    except Exception:
        return

    mostrar_tablero_coloreado(grid, n)

    while True:
        comando = input("\nComando (resolver | trazar | verificar | deshacer | salir): ").strip().lower()

        if comando == "resolver":
            exito = resolver_juego(grid, pairs, n)
            mostrar_tablero_coloreado(grid, n)
            print("\n✅ Solución encontrada correctamente." if exito else "\n❌ No se pudo resolver el tablero.")

        elif comando.startswith("trazar"):
            try:
                partes = comando.split()
                par = int(partes[1])
                coords = [(int(x)-1, int(y)-1) for x, y in (c.split(",") for c in partes[2:])]
                if es_camino_valido(grid, par, coords, pairs):
                    trazar_camino(grid, par, coords)
                    print(f"Camino trazado para {par}.")
                else:
                    print("❌ Camino inválido.")
            except Exception:
                print("⚠️ Formato incorrecto. Ej: trazar 1 1,1 1,2 1,3")

        elif comando == "verificar":
            completo = all(
                grid[i][j] != 0
                for i in range(n)
                for j in range(n)
            )
            print("✅ El tablero está completo." if completo else "❌ El tablero no está completo.")

        elif comando.startswith("deshacer"):
            try:
                num = int(comando.split()[1])
                inicio, fin = pairs[num]
                for i in range(n):
                    for j in range(n):
                        if grid[i][j] == num and (i, j) not in [inicio, fin]:
                            grid[i][j] = 0
                print(f"🧹 Camino del número {num} deshecho.")
            except:
                print("⚠️ Usa: deshacer <numero>")

        elif comando == "salir":
            print("👋 Saliendo del juego...")
            break

        else:
            print("⚠️ Comando no reconocido.")

        mostrar_tablero_coloreado(grid, n)

if __name__ == "__main__":
    main()
