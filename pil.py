from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_exif(file_path):
    try:
        # Open image file
        image = Image.open(file_path)
        exif_data = image._getexif()
        
        if exif_data is not None:
            metadata = {}
            
            for tag, value in exif_data.items():
                # Convert tag numbers to human-readable names
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value
            
            return metadata
        else:
            print(f"No EXIF metadata found for {file_path}")
            return None
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
        return None

def display_exif_info(metadata):
    if metadata:
        print("Extracted EXIF Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")

# Example usage
file_path = "image.jpg"  # Replace with the actual image file path
metadata = extract_exif(file_path)
display_exif_info(metadata)
