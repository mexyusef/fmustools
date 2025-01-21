# pip install --user Pillow piexif

from PIL import Image
import piexif

class ImageMetadata:
    def __init__(self, file_path):
        self.file_path = file_path
        self.image = Image.open(file_path)
        self.exif_data = self._get_exif_data()

    def _get_exif_data(self):
        exif = self.image._getexif()
        if exif is not None:
            return {piexif.TAGS[ExifIFD][tag]: value
                    for tag, value in exif.items()
                    if tag in piexif.TAGS[ExifIFD]}
        return {}

    def read_metadata(self, tag):
        return self.exif_data.get(tag)

    def update_metadata(self, tag, value):
        self.exif_data[tag] = value
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}
        for k, v in self.exif_data.items():
            exif_dict["Exif"][piexif.TAGS[ExifIFD].get(k)] = v
        exif_bytes = piexif.dump(exif_dict)
        self.image.save(self.file_path, "jpeg", exif=exif_bytes)

    def delete_metadata(self, tag):
        if tag in self.exif_data:
            del self.exif_data[tag]
            self.update_metadata(tag, None)

    def create_metadata(self, tag, value):
        self.update_metadata(tag, value)

    def print_metadata(self):
        print("Metadata for:", self.file_path)
        for tag, value in self.exif_data.items():
            print(f"{tag}: {value}")
