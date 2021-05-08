import os
import csv

base_path = os.getcwd()

dimension = open("Dimension.csv", 'w', newline='')
writer = csv.writer(dimension)
writer.writerow(['File/Directory Name', 'Gb ','Dimension - MB', 'Dimension - byte', 'Path'])
dimension.close()


def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


for file in os.listdir(base_path):
    file_dir_path = os.path.join(base_path, file)
    totalDim = (get_directory_size(file_dir_path))

    documents = open("Dimension.csv", 'a', newline='')
    writer = csv.writer(documents)
    writer.writerow(
        [str(file), str((totalDim / (1024 * 1024 * 1024)))[:8],str((totalDim / (1024 * 1024)))[:8], int(str(totalDim)[:12]),
         str(file_dir_path)])
    documents.close()
