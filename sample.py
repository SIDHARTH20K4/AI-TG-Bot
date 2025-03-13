from PIL import Image

# Use a raw string or double backslashes
asd = r"C:\Users\91812\Desktop\AI-TG-Bot\asd.jpg"

# Open the image file
base_image = Image.open(asd)

# Resize the image
base_image = base_image.resize((721, 430))

# Save the resized image
output_path = r"C:\Users\91812\Desktop\AI-TG-Bot\resized_asd.jpg"  # Specify the output path
base_image.save(output_path)
