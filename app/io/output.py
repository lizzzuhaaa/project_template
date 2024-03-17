def output_terminal(text):
    print(text)


def output_file(text, path):
    try:
        with open(path, 'w') as file:
            file.write(text)
    except IOError:
        print("Error was occurred by writing to file")
