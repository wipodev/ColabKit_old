# Record

**Módulo `record` de ColabKit: Grabación y Procesamiento de Audio en Google Colab**

Este módulo proporciona funciones para grabar audio en Google Colab, convertirlo a formato WAV y guardar el archivo resultante. También incluye herramientas para mostrar mensajes y notificaciones en el entorno de Google Colab.

**Guía Básica de Uso:**

1. **Grabación de Audio:**

   - Utiliza la función `get_audio()` para grabar audio desde la entrada del usuario a través del navegador.
   - Esta función devuelve una tupla con el audio grabado en formato Numpy (como un ndarray) y la tasa de muestreo (sample rate) del audio.

   Ejemplo:

   ```python
   audio, sr = get_audio()
   ```

2. **Grabar y Guardar Audio:**

   - Utiliza la función `record(file_audio="record.wav")` para grabar audio y guardar el resultado en un archivo WAV.
   - Puedes especificar el nombre del archivo WAV con el argumento `file_audio`.

   Ejemplo:

   ```python
   record("mi_grabacion.wav")
   ```

3. **Esperar a que se Guarde el Archivo:**

   - La función `record` también utiliza la función `wait_for_file(file_audio)` para esperar a que se guarde el archivo de audio en el entorno de Google Colab.
   - Muestra un mensaje y una notificación cuando la grabación se guarda con éxito.

4. **Notificaciones en Google Colab:**

   - El módulo utiliza la función `display(HTML(SAVED_AUDIO_RECORDING))` para mostrar una notificación que indica que la grabación de audio se ha guardado con éxito.

5. **Conversión de Datos Binarios a WAV:**
   - La grabación de audio se recopila en formato binario. Luego, el módulo utiliza la biblioteca FFmpeg para convertir estos datos binarios en un archivo WAV.

El módulo `record` facilita la grabación de audio en Google Colab y la gestión de archivos de audio en formato WAV. Puedes utilizar estas funciones para capturar audio desde el navegador y realizar tareas relacionadas con el procesamiento de audio en tu entorno de Google Colab.
