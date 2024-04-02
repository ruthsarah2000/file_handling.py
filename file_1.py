'''
Problem Statement:
Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory 
path and then display the contents.
'''
import os

def list_directory_contents(path):
    try:
        
        if os.path.exists(path):
           
            contents = os.listdir(path)
            print(f"Contents of directory '{path}':")
            for item in contents:
                print(item)
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)


'''
Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user for a directory path and 
then print each file's name and size within that directory.
'''
import os

def report_file_sizes(directory):
    try:
       
        if os.path.exists(directory) and os.path.isdir(directory):
            print(f"Files in directory '{directory}':")
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    print(f"{file_name}: {file_size} bytes")
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = input("Enter the directory path: ")
report_file_sizes(directory_path)

'''
Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' 
files and three '.py' files, the script should report "TXT: 5" and "PY: 3".
'''
import os

def count_file_extensions(directory):
    try:
       
        if os.path.exists(directory) and os.path.isdir(directory):
          
            extension_counts = {}

           
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                   
                    _, extension = os.path.splitext(file_name)
                    extension = extension.lower()

                   
                    extension_counts[extension] = extension_counts.get(extension, 0) + 1

           
            for extension, count in extension_counts.items():
                print(f"{extension.upper()}: {count}")
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = input("Enter the directory path: ")

count_file_extensions(directory_path)
