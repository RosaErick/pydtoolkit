import pytsk3

class FATReader:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img_info = pytsk3.Img_Info(image_path)
        self.fs_info = pytsk3.FS_Info(self.img_info)
        
    def list_directory(self, dir_path="/"):
        directory = self.fs_info.open_dir(path=dir_path)
        for entry in directory:
            print(entry.info.name.name)

    def get_file_metadata(self, file_path):
            file = self.fs_info.open(file_path)
            metadata = {
            "name": file.info.name.name,
            "size": file.info.meta.size,
            "created_time": file.info.meta.crtime,
            "accessed_time": file.info.meta.atime,
            "modified_time": file.info.meta.mtime,
            # Add other metadata attributes as required
        }
            return metadata
        

def carve_files(self, output_directory):
    
    img = pytsk3.Img_Info(self.image_path)

    # Initialize some variables
    start_sector = 0
    end_sector = img.info.media_size // img.info.block_size
    is_jpeg = False
    jpeg_data = b""

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    
    file_count = 0

    for sector in range(start_sector, end_sector):
        # Read the sector
        offset = sector * img.info.block_size
        data = img.read_random(offset, img.info.block_size)

        # Search for JPEG start signature
        if data.startswith(b'\xFF\xD8'):
            is_jpeg = True
            jpeg_data = b""
        
        # If inside a JPEG, accumulate data
        if is_jpeg:
            jpeg_data += data

        # Search for JPEG end signature
        if data.endswith(b'\xFF\xD9'):
            is_jpeg = False
            file_count += 1
            
            # Save the JPEG data
            with open(f"{output_directory}/carved_{file_count}.jpg", 'wb') as f:
                f.write(jpeg_data)

    print(f"Carved {file_count} JPEG files.")
