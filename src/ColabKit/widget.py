from IPython.display import display
import ipywidgets as widgets


def generate_button(text, tip, style, func, *param) -> widgets.Button:
    """
    Generates an interactive button in the Jupyter Notebook environment with the specified functionality.
    Args:
        text (str): The text displayed on the button.
        tip (str): The tooltip text displayed when hovering over the button.
        style (str): The style of the button (e.g., 'success' for a green button).
        func (callable): The function to be executed when the button is clicked.
        *param: Optional parameters to be passed to the function when the button is clicked.
    Returns:
        widgets.Button
    Example:
        To create a button that executes the function 'my_function' with two parameters:
        generate_button("My Button", "Click here", "success", my_function, param1, param2)
    """
    button = widgets.Button(description=text, button_style=style, tooltip=tip, icon='erase')
    def on_button_click(b):
        func(*param)
    button.on_click(on_button_click)
    display(button)
    return button