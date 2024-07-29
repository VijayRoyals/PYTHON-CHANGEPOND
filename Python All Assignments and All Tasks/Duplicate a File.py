import shutil
import os

def duplicate_file(source_path, destination_path):
    """Duplicate a file by copying it to a new location."""
    try:
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
            print(f"File duplicated from '{source_path}' to '{destination_path}'.")
        else:
            print(f"Source file '{source_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_path = input("Enter the path of the file to duplicate: ")
    destination_path = input("Enter the path for the duplicated file: ")
    duplicate_file(source_path, destination_path)

if __name__ == "__main__":
    main()
