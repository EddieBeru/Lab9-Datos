# Contrato de consola

`python -m graph_lab sort ARCHIVO`
Éxito: JSON {"order": [nombres]}, salto final, estado 0, stderr vacío.
Elegir el menor nombre Unicode disponible según FR-202. Vacío: {"order": []}.
Ciclo/bucle: estado 1, stdout vacío, stderr exactamente
`Error: el grafo contiene un ciclo; no existe orden topológico` y salto final.
Lectura y formato: mismos mensajes y estado 1 de Feature 1.
Uso inválido: estado 2, uso en stderr; --help: estado 0 y ayuda en stdout.
Show conserva todo el contrato de Feature 1, incluso ciclos y autoaristas.
