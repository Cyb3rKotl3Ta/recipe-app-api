import os

def rename_images_with_counter(directory):
    # Initialize the counter
    counter = 1

    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file is an image with the given extensions
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Get the file extension
            extension = os.path.splitext(filename)[1]
            # Define the new name using the counter
            new_name = f"{counter}{extension}"
            # Get the full path for the old and new names
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} to {new_path}")
            # Increment the counter
            counter += 1

# Specify the directory containing the images
directory_path = 'G:\\Josefina\\ZZZHOYOVERSE'

# Call the function
rename_images_with_counter(directory_path)
