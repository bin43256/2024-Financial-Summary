from extract_transform import extractAndTransformData
import os

# Check the current working directory
print('test_again')
print(os.getcwd())

# Check if the directory exists
file_path = '/app/data/'

if os.path.isdir(file_path):
    print(f"{file_path} exists and is a directory.")
    # List files in the directory
    file_list = os.listdir(file_path)
    print(f"Files in {file_path}: {file_list}")
    
    # Pass the list of files to the function
    extractAndTransformData(file_list)
else:
    print(f"{file_path} does not exist or is not a directory.")

