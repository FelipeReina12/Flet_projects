## Proycto Flet
Este repositorio contiene una aplicación de interfaz gráfica construida con Python y Flet, gestionada con `uv`.

**Crear entorno virtual**
uv venv

**Activar entorno virtual en bash**
source .venv/Scripts/activate
*Recordar seleccionar el interprete de python de nuestro entorno virtual*

**Agregar flet desde uv**
uv add 'flet[all]'
*Instalar todo rápidamente*
uv sync

**Comando para ejecutar programa flet**
flet run -d main.py

Agregué el comando `uv sync`. Así, cuando descargue este repositorio en tu otro PC usando la memoria USB, no tengo que volver a hacer el `uv add`, simplemente correr `uv sync` y la herramienta se encargará de leer el archivo y dejar Flet instalado exactamente en la misma versión.