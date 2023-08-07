# checks the last number used (info saved in the last_number.txt file) and starts from the next one
# renames files to the format 'YYYYMMDD_XXXX.jpg' where XXXX represents the four digit number
# moves renamed files to the 'renamed' folder
# supports only JPG files

import os
from utils import get_last_number, update_last_number, print_last_number


def rename_move_images(directory):
    renamed_folder = "photos/renamed"

    if not os.path.exists(renamed_folder):
        os.mkdir(renamed_folder)

    file_list = os.listdir(directory)
    file_list.sort()

    if not any(filename.endswith('.jpg') for filename in file_list):
        print("No JPG files found in the folder. Upload files to the folder and try again.")

    last_number = get_last_number() + 1

    for filename in file_list:
        if filename.endswith('.jpg'):
            date_part, extension = filename.split('_', 1)
            new_filename = f"{date_part}_{str(last_number).zfill(4)}.jpg"
            src = os.path.join(directory, filename)
            dst = os.path.join(renamed_folder, new_filename)
            
            os.rename(src, dst)
            last_number += 1

    update_last_number(last_number - 1)


if __name__ == "__main__":
    images_directory = "/home/karolina/6000steps/photos"
    rename_move_images(images_directory)
    print_last_number()
