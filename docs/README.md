<p align="center">
  <img src="../ColabKit.jpg" alt="ColabKit logo" width="250" height="250">
</p>

# **ColabKit**

ColabKit es una librería de Python diseñada para simplificar y mejorar tu experiencia de programación en Google Colab. Ofrece un conjunto de funciones y utilidades comunes para trabajar de manera eficiente con las características y herramientas de Colab. Con ColabKit, puedes realizar tareas básicas como manipulación de medios, grabación de audio, generación de widgets interactivos, utilidades de sistema y visualización interactiva de video y audio de una manera fácil y conveniente.

¡Simplifica tu flujo de trabajo en Google Colab con ColabKit y aprovecha al máximo esta plataforma de programación en la nube!

A continuación, se presenta una descripción general de los módulos y funciones disponibles en ColabKit:

**Módulo `media`**:

- Este módulo se centra en la manipulación de medios, como archivos de video y audio.
- Ofrece funciones para mostrar medios en una notebook, obtener la duración de un archivo de video, obtener la resolución de un archivo de video y manejar errores de FFmpeg.
- También proporciona la capacidad de convertir y recortar videos, así como redimensionarlos a una resolución deseada.
- Sus funciones permiten una integración sencilla de contenido multimedia en tu flujo de trabajo de Colab.

**Módulo `record`**:

- Este módulo se especializa en la grabación de audio y la manipulación de datos de audio.
- Ofrece una función para capturar audio desde la entrada del usuario a través del navegador, lo que facilita la grabación y procesamiento de audio en entornos de notebook.
- También proporciona una función para grabar audio y guardar los datos resultantes en un archivo WAV.
- Estas funciones son especialmente útiles para tareas que involucran grabación y procesamiento de audio en tiempo real.

**Módulo `template`**:

- Este módulo contiene plantillas HTML para incrustar contenido multimedia en notebooks.
- Proporciona plantillas para mostrar archivos de audio y video en un formato fácil de usar con controles integrados.
- También ofrece una plantilla para grabar audio directamente desde una notebook, lo que simplifica la interacción con la entrada de audio en tiempo real.

**Módulo `utils`**:

- El módulo proporciona una variedad de funciones de utilidad para simplificar tareas comunes en entornos de notebook.
- Incluye funciones para eliminar archivos, verificar la existencia de archivos, montar Google Drive en Colab y cargar archivos desde la máquina local a la notebook.
- También contiene una función que permite esperar la existencia y estabilidad de un archivo en un tiempo límite especificado.

**Módulo `widget`**:

- Este módulo ofrece una función para generar botones interactivos en la notebook.
- Los botones se pueden personalizar con texto, estilos y funcionalidades específicas, y se pueden utilizar para interactuar con código personalizado en la notebook.
- La función `generate_button` facilita la creación de widgets interactivos para ejecutar funciones personalizadas en respuesta a eventos de clic.

En resumen, ColabKit es una biblioteca versátil que simplifica muchas tareas comunes en Google Colab, desde la manipulación de medios hasta la grabación de audio y la creación de widgets interactivos. Está diseñada para mejorar la productividad y facilitar el desarrollo de proyectos en estos entornos de notebook. Las funciones proporcionadas en los módulos de ColabKit son herramientas útiles que pueden acelerar el flujo de trabajo en proyectos de análisis de datos, desarrollo de aplicaciones y más.
