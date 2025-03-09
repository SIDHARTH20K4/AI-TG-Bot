import requests
from io import BytesIO
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
API_TOKEN = "YOUR_HUGGING_FACE_API_TOKEN"

def load_image(path_to_image):
    image = Image.get(path_to_image).convert('RGB')
    return image

def generate_image(prompt,base_image_url,output = "output.png"):
    base_image = load_image(base_image_url)
    base_image = base_image.resize((512,512))

    image_bytes = BytesIO()
    base_image.save(image_bytes, format = "PNG")
    image_bytes = image_bytes.getvalue()

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs": prompt,
        "image": image_bytes,
        "parameters": {
            "strength": 0.75,  # Controls how much the base image is modified
            "guidance_scale": 7.5,  # Controls how closely the output follows the prompt
            "num_inference_steps": 50,  # Number of denoising steps
        },
    }

    response = requests.post(API_URL,)