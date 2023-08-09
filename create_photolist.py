# creates txt file to fetch all filenames (for photo gallery)

import os

directory_path = './photos/thumbnails'
output_file = 'photo_list.txt'

try:
    filenames = [filename for filename in os.listdir(directory_path) if filename.endswith('.jpg')]
    file_content = '\n'.join(filenames)
    output_file_path = os.path.join(directory_path, output_file)

    with open(output_file_path, 'w') as f:
        f.write(file_content)

    print('File list saved to', output_file_path)

except Exception as e:
    print('Error:', e)

