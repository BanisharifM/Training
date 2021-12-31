from pywebio.output import *
from pywebio.input import *
import os
import re
import asyncio
import time
from index import training, detecting

put_markdown('Logistic Regression with a Neural Network mindset')


def get_config():

    info = input_group('Training config', [
        input(label='Enter number of iterations：',
              value=2000, type=NUMBER, name='number'),
        input("Enter learning tate：", value=0.005, type=NUMBER, name='rate')
    ])
    get_py_files(info)


# def progress():


def get_py_files(info):

    #     asyncio(progress())

    #     put_processbar('bar')
    #     for i in range(1, 101):
    #         set_processbar('bar', i / 100)
    #         time.sleep(0.5)
    #     put_markdown("Here is your model! Lets test it!")

    put_markdown("Your model is training ...")
    logistic_regression_model=training(info['number'], info['rate'])

    with popup("Training Result:"):
        put_text("Here is your model! Lets test it!")

    # get all files in selected directory
    all_files = os.listdir('images')

    # regex for *.py files
    pattern = "^([a-zA-Z0-9\s_\\.\-\(\):])+\.jpg$"

    # choose just python files from list
    py_files = {file for file in all_files if re.match(pattern, file)}

    selecting_target(py_files,logistic_regression_model)


def selecting_target(py_files,logistic_regression_model):
    file_name = select("Choose a picture to test:", sorted(py_files))
#     asyncio.run(file_runner(file_name))
    result = detecting(file_name,logistic_regression_model)
    with popup("Detecting Result:"):
        put_text("your algorithm predicts a \""+result + "\" picture.")
#     get_py_files()


# async def file_runner(file_name):
#     print(f"you chose \"{file_name}\" to run.\n")

#     # run selected file via os.system
#     os.system(f"python3 {file_name}")

#     put_markdown(f"Successfully runned {file_name}")


if __name__ == '__main__':
    get_config()

# main(num_iterations, learning_rate)
