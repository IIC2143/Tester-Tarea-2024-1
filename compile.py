import os
import py_compile


if __name__ == '__main__':
    files = os.listdir('src')
    py_files = [file for file in files if file.endswith('.py')]
    for file in py_files:
        py_compile.compile(f'src/{file}', cfile=f'srccpm/{file}c')
