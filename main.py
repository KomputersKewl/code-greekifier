import os
from os.path import exists as file_exists

# Used to determine directory to place Greekified files
def specify_cwd():

    while True:
        path = input("Specify a directory to create parsed files: ")
        if file_exists(path):
            return path
        print("Not a directory!")
    
    return path

# "Greekifies" files given a source file & cwd
def greekify(cwd: str):

    src = input("Specify a file to Greekify! ")

    full_path = cwd + "/" + src
    
    if not file_exists(full_path): # Checks if file exists
        print ("File does not exist!")
        return

    file = os.path.basename(src)
    greekified_path = cwd + "/greekified-" + file

    if os.path.exists(greekified_path): # Ensures that no Greekified file already exists
        print("Greekified file already exists!")
        return
    else:
        try:
            with open(full_path, "r") as f:
                f_text = f.read()

        except:
            print("Could not read file.")
            return

    greekify = f_text.replace(";", "\u037e") # Used unicode so as to avoid confusion

    # Appends code to new file
    with open(greekified_path, "w") as nf:
        nf.write(greekify)

    print("Successfully created Greekified file! Congrats!")

# Handles user text input
def fixed_inputs(text, pos_values: list=[]):
    val = input(text).lower()

    if val in pos_values or len(pos_values) == 0:
        return val
    else:
        fixed_inputs(text, pos_values)

def app():
    cwd = os.getcwd()

    print("Hello! This is the code Greekifier!")
    while True:
        print(f"Current directory: {cwd}")
        app_func = fixed_inputs("What would you like to do? (\"s\" to specify current directory / \"g\" to Greekify file / \"q\" to quit application) ", ["g", "s", "q"])

        if app_func == "s":
            cwd = specify_cwd()
        elif app_func == "g":
            greekify(cwd)
        elif app_func == "q":
            return

if __name__ == "__main__":
    app()