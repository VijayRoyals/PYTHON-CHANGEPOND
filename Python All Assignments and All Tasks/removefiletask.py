import os

def delete_file(file_path):
    """Delete the file at the specified path."""
    try:
    
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

    file_path = input("Enter the path of the file to delete: ")
    delete_file(file_path)

if __name__ == "__main__":
    main()
