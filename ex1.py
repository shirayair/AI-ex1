"""
Name: Shira Yair
ID: 315389759
Because the submit system does not accept directories,
I created a tarfile, and I extract it so that my code won't
be broken. Thanks for consideration!
The tarfile can be opened with 7zip
"""


import tarfile
import importlib


def extract():
    with tarfile.open("ex1_ai.tarx") as tar:
        tar.extractall()


def call_export():
    try:
        main = importlib.import_module("main")
        with open("input.txt", "r") as reader:
            file = [line for line in reader.read().splitlines() if line]
        main.dispatch(file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    extract()
    call_export()
