import os

# Path to the folder containing your markdown files
folder_path = "G:/Keerthi/NLP/Natyashastra/Natyashastra/docs"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a markdown file
    if filename.endswith(".md"):
        # Define the new file name with .html extension
        new_filename = filename.replace(".md", ".html")
        
        # Get full path of the current and new file
        current_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(current_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
