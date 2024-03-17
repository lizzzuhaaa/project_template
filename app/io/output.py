def output_terminal(text):
    """
    Function to show given text in terminal
    :param text: text to show(str)
    """
    print(text)


def output_file(text, path):
    """
    Function to write given text in a given file
    :param text: text to write(str)
    :param path: path to the file(str)
    """
    try:
        with open(path, 'w') as file:
            file.write(text)
    except IOError:
        print("Error was occurred by writing to file")
