import pandas as pd


def output_text_to_console(text):
    """A function to output text to the console."""
    print(text)


def write_text_to_file(text, file_path):
    """A function to write text to a file using Python's built-in capabilities."""
    with open(file_path, 'w') as file:
        file.write(text)


def write_text_to_file_with_pandas(text, file_path):
    """A function to write text to a file using the pandas' library."""
    df = pd.DataFrame({'Text': [text]})
    df.to_csv(file_path, index=False)
