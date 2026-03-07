import pandas as pd


def read_from_console():
    """
    Зчитує рядок тексту, введений користувачем у консолі.

    Returns:
        str: Введений текст.
    """
    print("Text pls:")
    return input()


def read_from_file_builtin(file_path):
    """
    Зчитує вміст текстового файлу за допомогою вбудованих функцій Python.

    Args:
        file_path (str): Шлях до файлу.
    Returns:
        str: Вміст файлу.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(file_path):
    """
    Зчитує дані з CSV файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до CSV файлу.
    Returns:
        str: Рядкове представлення даних DataFrame.
    """
    df = pd.read_csv(file_path)
    return df.to_string()