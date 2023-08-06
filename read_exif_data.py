# fetches Exif Data from jpg files


import os
import csv
from PIL import Image


csv_filename = "metadata_from_photos.csv"
csv_exists = os.path.exists(csv_filename)

if not csv_exists:
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        header = [
            "image_id", "image type", "width", "height", "camera brand",
            "camera model", "exposure time", "exposure program", "aperture value",
            "ISO speed rating", "flash fired", "metering mode", "focal length",
            "software", "created on"
        ]
        csv_writer.writerow(header)

def process_image(file_path):
    with Image.open(file_path) as img:
        exif_data = img._getexif() if img._getexif() else {}
        image_id = os.path.splitext(os.path.basename(file_path))[0].split('_')[-1]
        
        image_type = os.path.splitext(file_path)[-1][1:]
        width, height = img.size
        
        camera_brand = exif_data.get(271, "N/A")
        camera_model = exif_data.get(272, "N/A")
        exposure_time = exif_data.get(33434, "N/A")
        exposure_program = exif_data.get(34850, "N/A")
        aperture_value = exif_data.get(37378, "N/A")
        iso_speed_rating = exif_data.get(34855, "N/A")
        flash_fired = exif_data.get(37385, "N/A")
        metering_mode = exif_data.get(37383, "N/A")
        focal_length = exif_data.get(37386, "N/A")
        software = exif_data.get(305, "N/A")
        created_on = exif_data.get(306, "N/A")
        
        with open(csv_filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                image_id, image_type, width, height, camera_brand,
                camera_model, exposure_time, exposure_program, aperture_value,
                iso_speed_rating, flash_fired, metering_mode, focal_length,
                software, created_on
            ])

folder_path = 'photos/to_resize'
jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

for jpg_file in jpg_files:
    file_path = os.path.join(folder_path, jpg_file)
    process_image(file_path)

print(f"Exif data extracted and written to {csv_filename} file.")
