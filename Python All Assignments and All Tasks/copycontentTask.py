import os
 
def write_file(file_name):
    if os.path.exists(file_name):
        print("You already have this file")
    else:
        with open("Task1(a).py", "r") as exit_data:
            data_file = exit_data.read()
        with open(file_name, "w") as written_data:
            final_file = written_data.write(data_file)
        print(final_file)
 
def get_file_name():
    file_name = input("Enter the File name: ")
    return file_name

def main():
    copy_name = get_file_name()
    write_file(copy_name)
 
if __name__ == "__main__":
    main()
