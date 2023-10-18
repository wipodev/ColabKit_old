# Media

**ColabKit: Biblioteca de Funciones para Google Colab**

Este módulo proporciona funciones para Google Colab que simplifica el manejo de archivos multimedia, como videos y audios, y permite realizar tareas comunes de procesamiento de medios. Facilita la visualización de medios y ofrece herramientas para realizar operaciones como obtener la duración de un video, obtener la resolución de un video, convertir formatos de medios y recortar videos.

**Guía Básica de Uso:**

1. **Visualización de Medios:**

   - Utiliza la función `showMedia(file_path, media)` para mostrar archivos multimedia en Google Colab.
   - `file_path` es la ruta al archivo multimedia.
   - `media` debe ser "video" o "audio", dependiendo del tipo de archivo multimedia que desees mostrar.

   Ejemplo:

   ```python
   showMedia("video.mp4", "video")
   ```

2. **Obtener Duración de Video:**

   - Utiliza la función `video_duration(video_path)` para obtener la duración de un video.
   - `video_path` es la ruta al archivo de video.

   Ejemplo:

   ```python
   duration = video_duration("video.mp4")
   print(f"Duración del video: {duration} segundos")
   ```

3. **Obtener Resolución de Video:**

   - Utiliza la función `get_video_resolution(video_path)` para obtener la resolución (ancho y alto) de un video.
   - `video_path` es la ruta al archivo de video.

   Ejemplo:

   ```python
   resolution = get_video_resolution("video.mp4")
   print(f"Resolución del video: {resolution[0]}x{resolution[1]}")
   ```

4. **Conversión de Formato de Video:**

   - Utiliza la función `ffmpeg_conv(input_file, output_file)` para convertir un video de un formato a otro.
   - `input_file` es la ruta al archivo de video de entrada.
   - `output_file` es la ruta donde se guardará el video convertido.

   Ejemplo:

   ```python
   success = ffmpeg_conv("input_video.mp4", "output_video.avi")
   ```

5. **Recortar un Video:**

   - Utiliza la función `ffmpeg_trim(input_file, start, interval, output_file)` para recortar un video ó un audio.
   - `input_file` es la ruta al archivo de entrada.
   - `start` es el punto de inicio en segundos.
   - `interval` es la duración en segundos para recortar.
   - `output_file` es la ruta donde se guardará el archivo recortado.

   Ejemplo:

   ```python
   trimmed_file = ffmpeg_trim("input_video.mp4", 10, 20, "output_video.mp4")
   ```

6. **Redimensionar un Video:**

   - Utiliza la función `resize_video(video_path, new_resolution)` para redimensionar un video a una nueva resolución.
   - `video_path` es la ruta al archivo de video original.
   - `new_resolution` es la nueva altura en píxeles para la resolución.

   Ejemplo:

   ```python
   resized_file = resize_video("input_video.mp4", 720)
   ```

El módulo `media` proporciona una variedad de herramientas para trabajar con archivos multimedia en Google Colab, lo que facilita la visualización y el procesamiento de medios. Puedes utilizar estas funciones para realizar tareas comunes en tu entorno de Google Colab.
