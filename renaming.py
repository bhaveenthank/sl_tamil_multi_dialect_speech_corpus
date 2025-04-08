import os

def rename_files_in_batches(directory, batch_size, names):
    """
    Renames files in batches with specific names.
    """
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sort files for consistent ordering
    files.sort()

    # Check if there are enough names for the batches
    total_batches = (len(files) + batch_size - 1) // batch_size
    if len(names) < total_batches:
        print(f"Error: Not enough names provided. You need at least {total_batches} names.")
        return

    # Rename files in batches
    for batch_index in range(total_batches):
        # Get the start and end index for the current batch
        start_index = batch_index * batch_size
        end_index = start_index + batch_size
        batch_files = files[start_index:end_index]

        # Get the name for this batch
        batch_name = names[batch_index]

        # Rename each file in the batch
        for file_index, filename in enumerate(batch_files):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Create the new filename
            new_filename = f"{batch_name}_{file_index + 1}{file_extension}"
            
            # Get the full paths for old and new filenames
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            print(f"Renamed '{filename}' to '{new_filename}'")

while (True):
    # Specify the directory, batch size, and names
    directory = input("Enter the directory path: ")
    number = input("Enter the number of the specimen: ")
    startNumb = int(input("Enter the number where the specimen starts: "))
    names = list()
    for i in range(5):
        word = str(number+"_Colombo_Male_"+str(startNumb))
        names.append(word)
        startNumb += 1
    print(names)
    # Call the rename_files_in_batches function
    rename_files_in_batches(directory, 5, names)
