import os

# Get the current working directory
current_directory = os.getcwd()

# Specify the relative path to a file or directory within the current working directory
relative_path = 'my_file.txt'

# Join the current directory path with the relative path
absolute_path = os.path.join(current_directory, relative_path)

print(f"Absolute Path: {absolute_path}")

