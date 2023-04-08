import mimetypes

# Prompt the user for the name of a file
filename = input("Please enter the name of a file: ")

# Get the file's extension (suffix) using the split() method and the dot (.) as the separator
# Then convert the extension to lowercase for case-insensitive comparison
extension = filename.split(".")[-1].lower() if "." in filename else ""

# Get the media type of the file using the mimetypes module
media_type = mimetypes.types_map.get(
    "." + extension, "application/octet-stream")

# Output the media type of the file
print(f"The media type of {filename} is {media_type}.")
