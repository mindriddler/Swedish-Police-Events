import os


def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print("Removed events.json")
    else:
        print("file not found")
