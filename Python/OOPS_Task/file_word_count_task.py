import os
def count_string_frequency(file_name, search_string):
    if(os.path.exists(file_name)):
        with open(file_name, 'r') as file:
            contents = file.read()
            frequency = contents.lower().count(search_string.lower())
            return frequency
    else:
        print(f"Error: The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name: ")
    search_string = input("Enter the string to search for: ")

    frequency = count_string_frequency(file_name, search_string)
    if frequency is not None:
        print(f"The frequency of '{search_string}' in '{file_name}' is: {frequency}")

if __name__ == "__main__":
    main()
