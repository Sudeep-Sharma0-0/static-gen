import os
import shutil


def generate_public(src, dest):
    if src == "static" and dest == "public":
        delete_public(dest)
        print("Copying files from 'static' dir to 'public' dir...")

    files = os.listdir(src)

    for file in files:
        if os.path.isfile(f"{src}/{file}"):
            copied_file = shutil.copy(f"{src}/{file}", f"{dest}/")
            print("Copied file: ", copied_file)
        if os.path.isdir(f"{src}/{file}"):
            print("Creating dir: ", f"{dest}/{file}")
            os.mkdir(f"{dest}/{file}")
            generate_public(f"{src}/{file}", f"{dest}/{file}")


def delete_public(dest):
    if os.path.exists(dest):
        dirs = os.listdir(dest)
        if len(dirs) > 0:
            print(f"Deleting '{dest}' dir...")
            shutil.rmtree(dest)
    print(f"Creating '{dest}' dir...")
    os.mkdir(dest)
