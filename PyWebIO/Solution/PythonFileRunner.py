from pywebio.output import *
from pywebio.input import *
import os
import re
import asyncio


put_markdown('Python file runner via PyWebIO')


def get_folder_path():
    # get folder path via input | if current folser enter '.' or keep it empty and click Submit
    path = input("Enter your folder directory：", type=TEXT) or '.'
    get_py_files(path)


def get_py_files(path):

    # get all files in selected directory
    all_files = os.listdir(path)

    # regex for *.py files
    pattern = "^([a-zA-Z0-9\s_\\.\-\(\):])+\.py$"

    # choose just python files from list
    py_files = {file for file in all_files if re.match(pattern, file)}

    selecting_target(py_files)


def selecting_target(py_files):
    file_name = select("Choose a file to run", sorted(py_files))
    asyncio.run(file_runner(file_name))


async def file_runner(file_name):
    print(f"you chose \"{file_name}\" to run.\n")

    # run selected file via os.system
    os.system(f"python3 {file_name}")

    put_markdown(f"Successfully runned {file_name}")


if __name__ == '__main__':
    get_folder_path()
