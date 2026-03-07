from app.io.input import (
    read_from_console,
    read_from_file_builtin,
    read_from_file_pandas,
)

from app.io.output import (
    write_to_console,
    write_to_file_builtin,
    write_to_file_pandas,
)

def main():
    txt_path = "D:\\Work\\Nonna\\unik\\Python_Practice\\project_template\\data\\test.txt"
    txt_for_pandas = "D:\\Work\\Nonna\\unik\\Python_Practice\\project_template\\data\\test_fot_pandas.csv"
    output_builtin_path = "D:\\Work\\Nonna\\unik\\Python_Practice\\project_template\\data\\results_builtin.txt"
    output_pandas_path = "D:\\Work\\Nonna\\unik\\Python_Practice\\project_template\\data\\results_pandas.csvf1"

    console_data = read_from_console()
    write_to_console(console_data)
    write_to_file_builtin(console_data, output_builtin_path)

    file_data = read_from_file_builtin(txt_path)
    write_to_console(file_data)
    write_to_file_builtin(file_data, output_builtin_path)

    pandas_data = read_from_file_pandas(txt_for_pandas)
    write_to_console(pandas_data)
    write_to_file_pandas(pandas_data, output_pandas_path)

if __name__ == "__main__":
    main()