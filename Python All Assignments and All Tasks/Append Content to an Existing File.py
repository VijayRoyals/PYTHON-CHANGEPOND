import os

def append_to_file(file_path, content):
    """Append content to an existing file."""
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')
            print(f"Content appended to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path of the file to append to: ")
    content = input("Enter the content to append: ")
    append_to_file(file_path, content)

if __name__ == "__main__":
    main()
