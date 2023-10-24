import os


def count_files_from_path(path: str = "None", recursive: bool = False) -> dict:
    """Функция, которая принимает на вход путь до директории и
    возвращает словарь с количеством папок и файлов директории"""
    dirs_counter = 0
    files_counter = 0
    new_dict = {}
    current_directory = os.getcwd()

    if path == "None":
        if not recursive:
            for dirs in os.listdir(current_directory):
                if os.path.isdir(os.path.join(current_directory, dirs)):
                    dirs_counter += 1
                else:
                    files_counter += 1

        else:
            for root, dirs, files in os.walk(current_directory):
                dirs_counter += len(dirs)
                files_counter += len(files)

    else:
        if not recursive:
            for dirs in os.listdir(path):
                if os.path.isdir(os.path.join(path, dirs)):
                    dirs_counter += 1
                else:
                    files_counter += 1
        else:
            for root, dirs, files in os.walk(path):
                dirs_counter += len(dirs)
                files_counter += len(files)

    new_dict["files"] = files_counter
    new_dict["folders"] = dirs_counter
    return new_dict
