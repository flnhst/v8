import os
import pathlib

def find_all_files():
    f = open("files_to_update", "r")

    ftu = f.read().split("\n")

    f.close()

    ftu = list(map(lambda file: file.replace(".obj", ".cc"), ftu))

    found = []

    for cc_file in pathlib.Path('src').glob('**/*.cc'):
        if pathlib.Path(cc_file).name in ftu:
            found.append(cc_file)
    
    return found


def add_header_to_file(cc_file):
    print(f"Updating file '{cc_file}'.")

    f = open(cc_file, "r")

    contents = f.read()

    f.close()

    if contents.find("namespace v8 {") == -1:
        print("Namespace not found.")

    f = open(cc_file, "w")

    f.write(contents)

    f.close()


all_cc_files = find_all_files()

for cc_file in all_cc_files:
    try:
        add_header_to_file(cc_file)
    except Exception as e:
        print(f"Failed to update file '{cc_file}': '{e}'.")


