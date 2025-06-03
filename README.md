# FreeFlow 🎲✨

¡Bienvenido al proyecto **FreeFlow**! 🎉 Este es un juego de lógica desarrollado como parte del curso **Análisis de Algoritmos** del **Departamento de Ingeniería de Sistemas** de la **Pontificia Universidad Javeriana**. Este README explica cómo usar el programa, las reglas del juego, su estructura interna y cómo probar tableros de distintos niveles. 🚀

---

## 📌 Índice

* [Descripción del Proyecto](#descripción-del-proyecto-)
* [Reglas del Juego](#reglas-del-juego-)
* [Requisitos](#requisitos-)
* [Estructura del Proyecto](#estructura-del-proyecto-)
* [Instrucciones de Uso](#instrucciones-de-uso-)
* [Comandos Disponibles](#comandos-disponibles-)
* [🧠 Detalles del Código](#detalles-del-código-)
* [🧪 Tableros de Prueba](#tableros-de-prueba-)
* [Entregas](#entregas-📆)
* [Autores](#autores-)

---

## Descripción del Proyecto 🏫

Este proyecto implementa una interfaz en consola para jugar **FreeFlow** (también conocido como NumberLink), un juego donde conectas pares de números en una grilla sin que los caminos se crucen. 🖥️ Incluye un jugador manual y un **jugador sintético** (algoritmo automático) que resuelve el tablero con backtracking.

---

## Reglas del Juego 📏

* Cada número en el tablero aparece exactamente dos veces. Debes conectar cada par con un camino continuo. 🔗
* Los caminos solo pueden ser **horizontales o verticales** (no diagonales). 🚫↘️
* Los caminos **no pueden cruzarse** ni pasar por celdas ocupadas por otros números. 🚷
* El tablero debe quedar completamente lleno, sin celdas vacías. 🧩

---

## Requisitos 📋

* Python 3.x 🐍
* Módulo `colorama` (opcional para colores en consola):

  ```bash
  pip install colorama
  ```

---

## Estructura del Proyecto 🗂️

```
FreeFlow/
├── freeflow.py              # Código principal
├── README.md                # Este archivo 😄
├── tableros/                # Carpeta con tableros de prueba
│   ├── tablero1_facil.txt
│   ├── tablero2_medio.txt
│   ├── tablero3_dificil.txt
```

---

## Instrucciones de Uso ⚙️

1. Ejecuta el programa desde consola:

   ```bash
   python freeflow.py tableros/tablero1_facil.txt
   ```

   Si no pasas ningún argumento, buscará `tablero.txt` por defecto.

2. Una vez cargado, verás el tablero inicial en consola con colores.

3. Escribe:

   ```
   resolver
   ```

   para que el algoritmo intente resolver automáticamente el tablero.

---

## Comandos Disponibles 📋

| Comando     | Descripción                                                         |
| ----------- | ------------------------------------------------------------------- |
| `resolver`  | Ejecuta el jugador sintético y resuelve el tablero automáticamente. |
| `trazar`    | Permite ingresar un camino manualmente para un número. ✍️           |
| `verificar` | Valida si el tablero actual cumple las reglas. ✔️                   |
| `deshacer`  | Borra el camino actual de un número dejando sus extremos. 🔁        |
| `salir`     | Termina la ejecución del juego. ❌                                   |

---

## 🧠 Detalles del Código

### `leer_archivo(nombre_archivo)` 📄

Lee un archivo `.txt` que contiene:

* Una línea con el tamaño del tablero (e.g., `7,7`)
* Varias líneas con coordenadas y valores (`fila,columna,valor`).
  Devuelve:
* La matriz del tablero (con ceros en celdas vacías).
* Un diccionario con las posiciones de cada par.

### `mostrar_tablero_coloreado(grid, n)` 🌈

Imprime el tablero en consola, mostrando números en colores. Los ceros se imprimen como `.`.

### `es_camino_valido(grid, par, celdas, pairs)` ✅

Valida que un camino trazado por el usuario o el algoritmo:

* Empiece y termine en las posiciones del par.
* No sea trivial.
* Use solo movimientos ortogonales.
* No se cruce con otros pares.

### `trazar_camino(grid, par, celdas)` ✏️

Dibuja el camino del par en la grilla, reemplazando celdas con el número correspondiente.

### `encontrar_caminos(grid, n, inicio, fin)` 🔍

Usa BFS (búsqueda en anchura) para encontrar **todos los caminos posibles** desde `inicio` hasta `fin`, solo a través de celdas vacías.

### `resolver_juego(grid, pairs, n)` 🧠

El **jugador sintético**:

* Ordena los pares.
* Para cada par, prueba caminos posibles.
* Usa **backtracking** para intentar conectar todos los pares sin violar reglas.
* Si no encuentra solución, retrocede y prueba otra ruta.

### `main()` 🧪

* Permite ejecutar el programa desde consola con el archivo que desees.
* Muestra el tablero y ejecuta la solución automática con `resolver`.

---

## 🧪 Tableros de Prueba

### 1️⃣ Tablero Fácil – `tableros/tablero1_facil.txt`

```plaintext
5,5
1,1,1
5,5,1
1,5,2
5,1,2
3,3,3
5,3,3
```

🔹 Pares bien distribuidos.
🔹 Caminos cortos y no cruzados.

✅ Resultado esperado:

```
1 1 1 1 2
. . 1 . 2
. . 3 . 2
. . 3 . 2
2 2 3 1 1
```

---

### 2️⃣ Tablero Medio – `tableros/tablero2_medio.txt`

```plaintext
7,7
3,5,1
6,3,1
2,5,2
7,1,2
2,2,3
3,4,3
1,4,4
7,5,4
2,6,5
4,4,5
```

🔹 Tablero clásico usado en los ejemplos del juego.
🔹 Combinación de rutas cortas y largas.

✅ Puedes trazar manualmente cada camino con los siguientes comandos:

```bash
trazar 1 6,3 5,3 5,4 5,5 4,5 3,5
trazar 2 2,5 2,4 2,3 1,3 1,2 1,1 2,1 3,1 4,1 5,1 6,1 7,1
trazar 3 2,2 3,2 3,3 3,4
trazar 4 7,5 7,6 7,7 6,7 5,7 4,7 3,7 2,7 1,7 1,6 1,5 1,4
trazar 5 4,4 4,3 4,2 5,2 6,2 7,2 7,3 7,4 6,4 6,5 6,6 5,6 4,6 3,6 2,6
verificar
```

💡 Alternativamente, puedes usar `resolver` para que el algoritmo lo complete automáticamente.

---

### 3️⃣ Tablero Difícil – `tableros/tablero3_dificil.txt`

```plaintext
9,9
1,1,1
9,9,1
1,9,2
9,1,2
2,2,3
8,8,3
2,8,4
8,2,4
3,3,5
7,7,5
5,5,6
5,6,6
```

🔹 Tablero 9x9 con múltiples pares.
🔹 Ideal para probar la eficiencia del algoritmo de backtracking.

⚠️ Puede tardar más en resolverse.

---

## Entregas 📆

### ✅ Interfaz del Juego:

* Desarrollo completo de la interfaz de consola con comandos manuales (`trazar`, `verificar`, `deshacer`, `salir`).
* Fecha: Semana 12 (21 de abril de 2025).

### ✅ Jugador Sintético:

* Algoritmo automático con backtracking (`resolver`) que conecta los pares del tablero.
* Fecha de entrega: 4 de mayo de 2025.

---

## Autores 📞

* Juan David – `juandavid0420-rgb` – [juandsanchez@javeriana.edu.co](mailto:juandsanchez@javeriana.edu.co)
* Alejandro Pinzón – `alejandro09pf` – [alejandro\_pinzon@javeriana.edu.co](mailto:alejandro_pinzon@javeriana.edu.co)

---

🎓 Proyecto presentado para el curso **Análisis de Algoritmos**, Universidad Javeriana, 2025.

¡Gracias por jugar! 🚀🎮
