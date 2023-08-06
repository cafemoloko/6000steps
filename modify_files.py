# fetches files and resized them by 75%
# creates thumbnails from the resized images

# TODO and issues: 
# thumbnails are not square (250x250 px). Height is 250 px, width depends on the resized image width 
# some photos might end up rotated 90 degrees clockwise
# "to_resize" folder is temporary. The input directory for the files to be resized should be "renamed"
 

from PIL import Image
import os


def get_last_number():
    if os.path.exists('last_number.txt'):
        with open('last_number.txt', 'r') as f:
            last_number = int(f.read())
        return last_number
    else:
        return 0

def resize_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_list = os.listdir(input_dir)
    file_list.sort()

    for filename in file_list:
        if filename.endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                original_width, original_height = img.size

                # Resize by 75%
                new_width = int(original_width * 0.25)
                new_height = int(original_height * 0.25)

                resized_img = img.resize((new_width, new_height))
                resized_img.save(output_path)

def create_thumbnails(input_dir, output_dir, thumbnail_size=(250, 250)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    last_number = get_last_number()
    incremented_number = last_number + 1

    file_list = os.listdir(input_dir)
    file_list.sort()

    for filename in file_list:
        if filename.endswith(f'{incremented_number}.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                img.thumbnail(thumbnail_size)
                img.save(output_path)
                print(f'Thumbnail created for: {filename}')

if __name__ == "__main__":

    # Paths to the directories containing photos to be resized
    input_directory = "/home/karolina/6000steps/photos/to_resize"
    resized_output_directory = "/home/karolina/6000steps/photos/resized"

    # Paths to the directories containing photos to create thumbnails for
    resized_input_directory = "/home/karolina/6000steps/photos/resized"
    thumbnails_output_directory = "/home/karolina/6000steps/photos/thumbnails"

    resize_images(input_directory, resized_output_directory)
    create_thumbnails(resized_input_directory, thumbnails_output_directory)
    
    
