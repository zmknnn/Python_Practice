import pandas as pd


def write_to_console(data):
    """
    Виводить отримані дані у консоль.

    Args:
        data (str): Дані для виводу.
    """
    print(f"Result:\n{data}\n" + "-" * 20)


def write_to_file_builtin(data, file_path):
    """
    Записує текст у файл за допомогою вбудованих можливостей Python.

    Args:
        data (str): Текст для запису.
        file_path (str): Шлях до файлу для збереження.
    """
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(data + "\n")


def write_to_file_pandas(data, file_path):
    """
    Записує дані у CSV файл за допомогою бібліотеки pandas.

    Args:
        data (str): Дані для запису (текст або DataFrame).
        file_path (str): Шлях до файлу для збереження.
    """
    df = pd.DataFrame([data], columns=['Content'])
    df.to_csv(file_path, index=False, encoding='utf-8')
    df.to_csv(file_path, index=False, encoding='utf-8')