# checks the last number used (info saved in the last_number.txt file) and starts from the next one
# renames files to the format 'YYYYMMDD_XXXX.jpg' where XXXX represents the four digit number
# moves renamed files to the 'renamed' folder
# supports only JPG files

import os


def get_last_number(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return int(file.read())
    return 0

def update_last_number(filename, number):
    with open(filename, "w") as file:
        file.write(str(number))

def rename_move_images(directory):
    renamed_folder = "photos/renamed"

    if not os.path.exists(renamed_folder):
        os.mkdir(renamed_folder)

    file_list = os.listdir(directory)
    file_list.sort()

    if not any(filename.endswith('.jpg') for filename in file_list):
        print("No JPG files found in the folder. Upload files to the folder and try again.")

    last_number = get_last_number("last_number.txt") + 1

    for filename in file_list:
        if filename.endswith('.jpg'):
            date_part, extension = filename.split('_', 1)
            new_filename = f"{date_part}_{str(last_number).zfill(4)}.jpg"
            src = os.path.join(directory, filename)
            dst = os.path.join(renamed_folder, new_filename)
            
            os.rename(src, dst)
            last_number += 1

    update_last_number("last_number.txt", last_number - 1)

    # "last_number -1" is to ensure the correct last number, because the for loop adds 
    # one extra number after the last loop run.
    
def print_last_number():
    filename = "last_number.txt"
    last_number_used = get_last_number(filename)
    print(f'Last photo number: {last_number_used}')


if __name__ == "__main__":
    images_directory = "/home/karolina/6000steps/photos"
    rename_move_images(images_directory)
    print_last_number()
