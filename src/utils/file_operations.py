import os
import sys
import requests
import io
from typing import Union


def open_file(file_path: str, mode: str = 'r', encoding: str = 'utf-8') -> Union[str, None]:
    """
    Open and read a file, returning its contents.

    Args:
    file_path (str): Path to the file to be opened.
    mode (str): Mode in which to open the file. Defaults to 'r' (read mode).
    encoding (str): Encoding to use when opening the file. Defaults to 'utf-8'.

    Returns:
    str: Contents of the file, or None if an error occurred.
    """
    try:
        with open(file_path, mode, encoding=encoding) as file:
            return file.read()
    except IOError as e:
        print(f"Error opening file: {e}")
        return None


def save_file(file_path: str, content: str, mode: str = 'w', encoding: str = 'utf-8') -> bool:
    """
    Save content to a file.

    Args:
    file_path (str): Path where the file should be saved.
    content (str): Content to be written to the file.
    mode (str): Mode in which to open the file. Defaults to 'w' (write mode).
    encoding (str): Encoding to use when writing the file. Defaults to 'utf-8'.

    Returns:
    bool: True if the file was saved successfully, False otherwise.
    """
    try:
        with open(file_path, mode, encoding=encoding) as file:
            file.write(content)
        return True
    except IOError as e:
        print(f"Error saving file: {e}")
        return False


def download_image(url: str) -> Union[io.BytesIO, None]:
    """
    Download an image from a URL and return it as a BytesIO object.

    Args:
    url (str): URL of the image to download.

    Returns:
    io.BytesIO: BytesIO object containing the image data, or None if download failed.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return io.BytesIO(response.content)
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None


def open_output_folder(output_folder_path: str) -> None:
    """
    Open the output folder in the default file explorer.

    Args:
    output_folder_path (str): Path to the output folder.
    """
    try:
        if sys.platform == "win32":
            os.startfile(output_folder_path)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open {output_folder_path}")
        else:  # Linux and other Unix-like
            os.system(f"xdg-open {output_folder_path}")
    except Exception as e:
        print(f"Error opening output folder: {e}")


def ensure_directory_exists(directory_path: str) -> bool:
    """
    Ensure that a directory exists, creating it if necessary.

    Args:
    directory_path (str): Path to the directory.

    Returns:
    bool: True if the directory exists or was created successfully, False otherwise.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return True
    except OSError as e:
        print(f"Error creating directory: {e}")
        return False
