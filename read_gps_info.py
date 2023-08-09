# fetches GPS information from jpg files

import os
import csv
from PIL import Image
from PIL.ExifTags import TAGS

def get_geolocation(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data is not None:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                if tag_name == 'GPSInfo':
                    return value
    return None

if __name__ == "__main__":
    folder_path = "/home/karolina/6000steps/photos/backup"
    csv_filename = "geolocation.csv"

    csv_exists = os.path.exists(csv_filename)

    with open(csv_filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        if not csv_exists:
            header = ["filename", "Latitude", "Longitude", "Altitude", "Date/Time", "GPSInfo"]
            csv_writer.writerow(header)

        jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

        for jpg_file in jpg_files:
            image_path = os.path.join(folder_path, jpg_file)
            gps_info = get_geolocation(image_path)

            if gps_info:
                latitude = gps_info.get(2)
                longitude = gps_info.get(4)
                altitude = gps_info.get(6)
                date_time = gps_info.get(29)
                gps_info_str = ", ".join([f"{TAGS.get(key, key)}: {gps_info[key]}" for key in gps_info])

                row = [jpg_file, latitude, longitude, altitude, date_time, gps_info_str]
                csv_writer.writerow(row)
                print(f"Geolocation data written for {jpg_file}.")
            else:
                print(f"No GPS information found in {jpg_file}.")
                
    print(f"Geolocation data written to {csv_filename} file.")


    
