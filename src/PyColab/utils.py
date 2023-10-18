if 'google.colab' in globals():
  from google.colab import files, drive
import time
import os

def remove_file(route) -> None:
    """
    Removes a file if it exists.
    Args:
        route (str): The route of the file to be removed.
    Returns:
        None
    """
    if os.path.isfile(route):
        os.remove(route)


def file_exists(route) -> bool:
    """
    Check if a file exists at the given route.
    Args:
        route (str): The route to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(route)


def mount_drive() -> None:
    """
    Mounts the Google Drive to the Colab environment.
    Returns:
        None
    """
    if not os.path.isdir("/content/drive/MyDrive"):
        drive.mount('/content/drive', force_remount=True)


def upload_file(route) -> None:
    """
    Uploads a file to the specified route.
    Args:
        route (str): The destination route for the uploaded file.
    Returns:
        None
    """
    remove_file(route)
    uploaded = files.upload()
    for filename in uploaded.keys():
        os.rename(filename, route)


def wait_for_file(file_name: str, time_limit: int = 60) -> bool:
    """
    Wait for a file to exist and remain unchanged for a specific time limit.
    Args:
        file_name (str): The name of the file to wait for.
        time_limit (int, optional): The maximum time to wait in seconds. Defaults to 60.
    Returns:
        bool: True if the file exists and remains unchanged within the time limit, False otherwise.
    """
    initial_time = time.time()
    exists = False

    while time.time() - initial_time < time_limit:
        if os.path.exists(file_name):
            previous_size = os.path.getsize(file_name)
            time.sleep(1)
            current_size = os.path.getsize(file_name)
            if current_size == previous_size:
                exists = True
                break
    return exists
