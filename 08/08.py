FILEPATH = "08-ex.input"


def get_tree_matrix_from_file(filepath: str):
    with open(filepath) as f:
        matrix = [[int(i) for i in line.rstrip()] for line in f.readlines()]
    return matrix


def main():
    matrix = get_tree_matrix_from_file(FILEPATH)
    print(matrix)


if __name__ == "__main__":
    main()
