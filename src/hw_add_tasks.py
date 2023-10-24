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


def get_format_string(any_list: list[str]) -> list[str]:
    """принимает на вход список строк и возвращает список строк,
    в которых первая и последняя буквы совпадают"""
    new_list = []
    for string in any_list:
        if string != "":
            if string[0] == string[-1]:
                new_list.append(string)
        else:
            new_list.append(string)
    return new_list


def get_nums_multiple(any_list: list[int]) -> int:
    """принимает на вход список целых чисел и возвращает
    максимальное произведение двух чисел из списка"""
    if len(any_list) >= 2:
        sorted_list = sorted([abs(item) for item in any_list])
        return sorted_list[-1] * sorted_list[-2]
    else:
        return 0
