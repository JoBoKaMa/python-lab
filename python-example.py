#!/usr/bin/python3
import os
import sys

def list_directory_contents(path='.'):
    try:
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = '.'
    
    # Call the function to list the directory contents
    list_directory_contents(directory_path)
