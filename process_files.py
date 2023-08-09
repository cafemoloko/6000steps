import os
import shutil
from PIL import Image
from utils import get_last_number, update_last_number

class FileProcessor:
    def __init__(self):
        self.new_files_dir = "/home/karolina/6000steps/photos"
        self.backup_dir = "/home/karolina/6000steps/photos/backup"
        self.resized_dir = "/home/karolina/6000steps/photos/resized"
        self.thumbnails_dir = "/home/karolina/6000steps/photos/thumbnails"

    def rename_files(self):
        file_list = os.listdir(self.new_files_dir)
        file_list.sort()

        if not any(filename.endswith('.jpg') for filename in file_list):
            print("No JPG files found in the folder. Upload files to the folder and try again.")

        last_number = get_last_number() + 1

        for filename in file_list:
            if filename.endswith('.jpg'):
                date_part = filename.split('_', 1)[0] 
                new_filename = f"{date_part}_{str(last_number).zfill(4)}.jpg"
                src = os.path.join(self.new_files_dir, filename)
                dst = os.path.join(self.new_files_dir, new_filename)
                
                os.rename(src, dst)  
                last_number += 1

        update_last_number(last_number - 1)
        print("All files have been renamed.")

    def resize_files(self):
        if not os.path.exists(self.resized_dir):
            os.makedirs(self.resized_dir)

        file_list = os.listdir(self.new_files_dir)
        file_list.sort()

        for filename in file_list:
            if filename.endswith('.jpg'):
                input_path = os.path.join(self.new_files_dir, filename)
                output_path = os.path.join(self.resized_dir, filename)

                with Image.open(input_path) as img:
                    original_width, original_height = img.size

                    new_height = 1200
                    aspect_ratio = original_width / original_height
                    new_width = int(new_height * aspect_ratio)

                    resized_img = img.resize((new_width, new_height))
                    resized_img.save(output_path)
                    print(f'Resized: {filename}')

    def create_thumbnails(self):
        if not os.path.exists(self.thumbnails_dir):
            os.makedirs(self.thumbnails_dir)

        file_list = os.listdir(self.new_files_dir)
        file_list.sort()

        for filename in file_list:
            if filename.endswith('.jpg'):
                input_path = os.path.join(self.new_files_dir, filename)
                output_filename = f"thumbnail_{filename}"
                output_path = os.path.join(self.thumbnails_dir, output_filename)

                with Image.open(input_path) as img:
                    img.thumbnail((250, 250))
                    img.save(output_path)
                    print(f'Thumbnail created for: {filename}')

    def create_backup(self):
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

        file_list = os.listdir(self.new_files_dir)
        file_list.sort()

        for filename in file_list:
            if filename.endswith('.jpg'):
                src = os.path.join(self.new_files_dir, filename)
                dst = os.path.join(self.backup_dir, filename)
                
                shutil.copy(src, dst)  
                print("Copying files to backup folder...")

        print("Created a backup of all files.")

    def cleanup(self):
        file_list = os.listdir(self.new_files_dir)
        for filename in file_list:
            if filename.endswith('.jpg'):
                file_path = os.path.join(self.new_files_dir, filename)
                os.remove(file_path)
                print("Cleaning up...")
        print("All done and cleaned!")

    def process_files(self):
        self.rename_files()
        self.resize_files()
        self.create_thumbnails()


if __name__ == "__main__":
    file_processor = FileProcessor()
    file_processor.process_files()
    file_processor.create_backup()
    file_processor.cleanup()
