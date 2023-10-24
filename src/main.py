from src.hw_add_tasks import count_files_from_path
from src.masks import format_acc_number, format_card_number

if __name__ == "__main__":
    print(format_card_number("7000792289606361"))
    print(format_acc_number("73654108430135874305"))

    print(
        count_files_from_path(
            path="/home/vlad/PycharmProjects/HW_1_Morozov_beta/src",
            recursive=True,
        )
    )
    print(count_files_from_path(path="/home/vlad/PycharmProjects/HW_1_Morozov_beta/src"))
    print(count_files_from_path(recursive=True))
    print(count_files_from_path())
