# Utils

El módulo `utils` en ColabKit proporciona varias funciones de utilidad que son útiles en el entorno de Google Colab. A continuación, te proporciono una descripción de cada una de las funciones:

1. **`remove_file(route)`**:

   - Esta función elimina un archivo si existe en la ubicación especificada.
   - Recibe la ruta del archivo como argumento y, si el archivo existe, lo elimina.

   - **Ejemplo:**

```
remove_file('/content/test.txt')
```

2. **`file_exists(route)`**:

   - Comprueba si un archivo existe en la ruta especificada.
   - Recibe la ruta del archivo como argumento y devuelve `True` si el archivo existe y `False` si no existe.

   - **Ejemplo:**

```
file_exists('/content/test.txt')
```

3. **`mount_drive()`**:

   - Esta función monta Google Drive en el entorno de Colab si aún no está montado.
   - Se utiliza para acceder y trabajar con archivos almacenados en Google Drive desde un entorno de Colab.

   - **Ejemplo:**

```
mount_drive()
```

4. **`upload_file(route)`**:

   - Permite subir un archivo desde tu sistema local al entorno de Colab.
   - Elimina cualquier archivo existente en la ruta especificada y carga un nuevo archivo desde tu sistema local.

   - **Ejemplo:**

```
upload_file('/content/test.txt')
```

5. **`wait_for_file(file_name, time_limit)`**:

   - Espera a que un archivo exista y permanezca sin cambios durante un tiempo específico.
   - Recibe el nombre del archivo que deseas esperar y un límite de tiempo en segundos.
   - Espera hasta que el archivo exista y no se modifique durante el tiempo especificado. Si el archivo cumple con estas condiciones, devuelve `True`. Si no, devuelve `False`.

   - **Ejemplo:**

```
wait_for_file('/content/test.txt', 5)
```

---

Estas funciones son útiles para realizar tareas comunes en Google Colab, como eliminar archivos, verificar la existencia de archivos, cargar archivos desde tu sistema local y esperar a que se complete una operación antes de continuar. Puedes utilizar estas funciones en tus proyectos de Colab para simplificar las operaciones de manejo de archivos y la interacción con Google Drive.
