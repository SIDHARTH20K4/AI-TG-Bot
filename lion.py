from diffusers import StableDiffusionImg2ImgPipeline
import torch
from PIL import Image

# Load the Stable Diffusion model
pipe = StableDiffusionImg2ImgPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32)  # Use float32 for CPU
pipe = pipe.to("cpu")  # Use CPU instead of CUDA

# Load the base image as a PIL Image
try:
    base_image = Image.open("base_image.jpg").convert("RGB")  # Ensure the image is in RGB format
except Exception as e:
    print(f"Error loading image: {e}")
    exit()

# Define a neutral prompt
prompt = "A cartoon-style character preparing food in a kitchen, maintaining the original character's appearance and style."

# Generate the image
try:
    output_image = pipe(
        prompt=prompt,
        image=base_image,  # Pass the PIL Image directly
        strength=0.75,  # Controls how much the base image is modified
        guidance_scale=0.5  # Controls how closely the output follows the prompt
    ).images[0]
except Exception as e:
    print(f"Error generating image: {e}")
    exit()

# Save the output image
try:
    output_image.save("output_image.png")
    print("Image generated successfully and saved to output_image.png")
except Exception as e:
    print(f"Error saving image: {e}")