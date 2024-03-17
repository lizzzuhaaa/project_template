from app.io.input import *
from app.io.output import *


def main():
    path = "D:/project_template/data/text.txt"
    text1 = input_from_terminal()
    output_terminal(text1)
    output_file(text1, path)

    text2 = input_from_file(path)
    output_terminal(text2)
    output_file(text2, path)

    path = "D:/project_template/data/text.csv"
    text2 = input_from_file_pandas(path)
    output_terminal(text2)
    output_file(text2, path)


if __name__ == '__main__':
    main()
