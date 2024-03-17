def input_from_terminal():
    """
    Function to get text from terminal
    :return:
    (str): text from terminal
    """
    return input()


def input_from_file(path):
    """
    Function to get text from file using builtin functionality
    :param path: path to the file(str)
    :return:
    (str): text from file
    """
    try:
        with open(path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File was not found")
        return None


def input_from_file_pandas(path):
    """
    Function to get text from csv file using lib pandas functionality
    :param path: path to the file(str)
    :return: text from file
    """
    import pandas
    try:
        data = pandas.read_csv(path)
        return data.to_string()
    except FileNotFoundError:
        print("File was not found")
        return None
