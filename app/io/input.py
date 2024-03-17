def input_from_terminal():
    return input()


def input_from_file(path):
    try:
        with open(path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File was not found")
        return None


def input_from_file_pandas(path):
    import pandas
    try:
        data = pandas.read_csv(path)
        return " ".join(data.iloc[:,0])
    except FileNotFoundError:
        print("File was not found")
        return None
