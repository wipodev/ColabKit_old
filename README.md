<p align="center">
  <img src="PyColab.jpg" alt="PyColab logo" width="250" height="250">
</p>

---

# PyColab

PyColab es una biblioteca de Python diseñada para mejorar la experiencia de trabajar en entornos de Jupyter Notebook y Google Colab. Con PyColab, puedes simplificar tareas comunes, manipular medios, grabar audio y crear widgets interactivos de manera más eficiente.

## Instalación

Puedes instalar PyColab fácilmente utilizando `pip`. Abre una terminal y ejecuta:

```bash
pip install pycolab
```

## Características Principales

- **Manipulación de Medios**: Visualiza y modifica archivos de video y audio directamente en tu notebook.
- **Grabación de Audio**: Graba audio en tiempo real a través de tu navegador con una simple función.
- **Widgets Interactivos**: Crea botones interactivos en la notebook para ejecutar código personalizado.
- **Utilidades de Sistema**: Simplifica tareas comunes, como eliminar archivos y verificar la existencia de archivos.

## Ejemplos de Uso

### Visualización de Video

```python
from pycolab.media import showMedia

# Muestra un archivo de video
showMedia('video.mp4', 'video')
```

### Grabación de Audio

```python
from pycolab.record import record

# Graba audio y guarda el resultado en un archivo WAV
record('grabacion.wav')
```

### Creación de Botones Interactivos

```python
from pycolab.widget import generate_button

# Crea un botón interactivo
def mi_funcion():
    print("¡Hiciste clic en el botón!")

generate_button("Hacer clic", "Haz clic para ejecutar mi_funcion", "success", mi_funcion)
```

## Documentación

Para obtener más información y documentación detallada, visita [el repositorio de PyColab en GitHub](https://github.com/wipodev/pycolab).

## Contribuciones

¡Apreciamos las contribuciones! Si deseas contribuir o informar sobre problemas, visita [nuestro repositorio en GitHub](https://github.com/wipodev/pycolab).

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---
