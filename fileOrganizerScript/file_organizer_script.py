import os
import shutil


def organize_files():
    # Define the directory to organize
    directory = input("Enter the directory path to organize: ")

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Create a dictionary to hold file types and their corresponding directories
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar.gz'],
        'Scripts': ['.py', '.js', '.sh']
    }

    # Create directories for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)

        # Move the file to the corresponding folder based on its extension
        moved = False
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                break

        # If the file type is unknown, move it to an "Others" folder
        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))

    print("Files have been organized successfully.")


if __name__ == "__main__":
    organize_files()