import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass


def get_todos(filepath_local=FILEPATH):
    """
    :param filepath_local: string
    :return: list
    """
    # file = open("data.txt", 'r')
    # todos = file.readlines()
    # file.close()
    with open(filepath_local, 'r') as file_local:
        todos_local: list[str] = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath_local=FILEPATH):
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_local)


# print(__name__)
#
# if __name__ == "__main__":
#     print("Hello")
#     print(get_todos())
