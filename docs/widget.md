# Widget

El módulo `widget` en ColabKit proporciona una función llamada `generate_button` que se utiliza para generar botones interactivos en el entorno de Google Colab. Aquí tienes una descripción de la función `generate_button`:

- **`generate_button(text, tip, style, func, *param)`**:
  - Genera un botón interactivo en el entorno de Jupyter Notebook (o Google Colab) con la funcionalidad especificada.
  - Recibe los siguientes argumentos:
    - `text` (str): El texto que se muestra en el botón.
    - `tip` (str): El texto del mensaje emergente que se muestra al pasar el cursor sobre el botón.
    - `style` (str): El estilo del botón, que puede ser un string como 'success', 'info', 'warning', 'danger', etc. Esto controla el aspecto del botón.
    - `func` (callable): La función que se ejecutará cuando se haga clic en el botón.
    - `*param` (parámetros opcionales): Cualquier número de parámetros que desees pasar a la función `func` cuando el botón se haga clic.
  - Ejemplo de uso:
    - Para crear un botón que ejecute la función 'my_function' con dos parámetros, puedes usarlo de esta manera:
    ```python
    generate_button("Mi Botón", "Haz clic aquí", "success", my_function, param1, param2)
    ```
  - La función `generate_button` crea un botón con el texto y el estilo especificados, y establece una función de controlador de evento que se ejecuta cuando el botón se hace clic. Los parámetros especificados se pasan a la función `func` cuando se hace clic en el botón.

---

Esta función es útil para crear botones interactivos en Google Colab, lo que permite a los usuarios interactuar con tu código y ejecutar funciones personalizadas con solo hacer clic en un botón. Puedes personalizar el aspecto y el comportamiento del botón según tus necesidades.
