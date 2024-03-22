import pandas as pd


def input_text_from_console():
    """Function for entering text from the console"""
    return input("Write text: ")


def read_text_from_file(file_path):
    """A function to read text from a file using Python's built-in capabilities"""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


def read_text_from_file_with_pandas(file_path):
    """A function to read text from a file using the pandas' library."""
    try:
        data = pd.read_csv(file_path)
        return data.to_string(index=False)
    except FileNotFoundError:
        return "File not found"
