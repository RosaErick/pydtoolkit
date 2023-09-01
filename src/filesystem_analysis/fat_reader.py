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