import os, sys

def file_exists(path):
    return os.path.exists(path)

# Used to determine directory to place Greekified files
def specify_cwd():
    path = input("Specify a directory to create parsed files: ")
    if not file_exists(path):
        print("Not a directory!")
        path = specify_cwd()
    
    return path

# "Greekifies" files given a source file & cwd
def greekify(cwd: str):

    src = input("Specify a file to Greekify! ")

    if not file_exists(cwd + "/" + src): # Checks if file exists
        print ("File does not exist!")
        return

    file = os.path.basename(src)
    full_path = cwd + "/" + src
    
    file_basename, file_ext = os.path.splitext(file)

    if os.path.exists(cwd + "/greekified-" + file): # Ensures that no Greekified file already exists
        print("Greekified file already exists!")
        return
    else:
        try:
            with open(full_path, "r") as f:
                f_text = f.read().split("\n") # Splits file into list for each instance of \n

        except:
            print("Could not read file.")

    # Iterates through file text and replaces semicolons with Greek question marks
    greekified = map(lambda line: line.replace(";", "\u037e"), f_text) # Used unicode as to avoid confusion

    # Appends code to new file
    with open(cwd + "/greekified-" + file, "w") as nf:
        for line in greekified:
            nf.write(line + "\n")

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
        print("Current directory: {0}".format(cwd))
        app_func = fixed_inputs("What would you like to do? (\"s\" to specify current directory / \"g\" to Greekify file / \"q\" to quit application) ", ["g", "s", "q"])

        if app_func == "s":
            cwd = specify_cwd()
        elif app_func == "g":
            greekify(cwd)
        elif app_func == "q":
            return

if __name__ == "__main__":
    app()
    sys.exit()
