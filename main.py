import os, sys
import shutil

def file_exists(path):
    return os.path.exists(path)

def specify_cwd():
    path = input("Specify a directory to create parsed files: ")
    if not file_exists(path):
        print("Not a directory!")
        path = specify_cwd()
    
    return path

def greekify(src, cwd: str):
    file = os.path.basename(src)
    file_basename, file_ext = os.path.splitext(file)
    if os.path.exists(cwd + "/greekified-" + file):
        print("Greekified file already exists!")
    else:
        with open(cwd + "/greekified-" + file, "w") as nf:
            try:
                shutil.copy(file, nf.name)
            except FileNotFoundError:
                pass

def text_input(text, pos_vals: list=[]):
    val = input(text).lower()
    if val in pos_vals or len(pos_vals) == 0:
        return val
    elif val == "quit":
        sys.exit()
    else:
        text_input(text, pos_vals)


cwd = os.getcwd()

print("Hello! This is the code Greekifier!")
while True:
    print(cwd)
    app_func = text_input("What would you like to do? (\"s\" to specify current directory / \"g\" to Greekify file) ", ["g", "s"])

    if app_func == "s":
        cwd = specify_cwd()
    elif app_func == "g":
        f = text_input("Specify a file to Greekify! ")
        greekify(f, cwd)