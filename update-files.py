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

    f = open(cc_file, "rb")

    raw_contents = f.read()

    f.close()

    contents = str(raw_contents, 'UTF-8')

    if contents.find("fixed-array-inl.h") != -1:
        print("Header fixed-array-inl.h found.")

        return

    if contents.find("namespace v8 {") != -1:
        new_value = "#include \"src/objects/fixed-array-inl.h\"\n\nnamespace v8 {"
        contents = contents.replace("namespace v8 {", new_value, 1)
    else:
        print("Namespace not found.")

    f = open(cc_file, "wb")

    f.write(bytes(contents, 'UTF-8'))

    f.close()


all_cc_files = find_all_files()

for cc_file in all_cc_files:
    try:
        add_header_to_file(cc_file)
    except Exception as e:
        print(f"Failed to update file '{cc_file}': '{e}'.")
        raise


