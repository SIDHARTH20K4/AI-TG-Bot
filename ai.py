from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch

# Loading the Stable Diffusion image-to-image model

def load_model():
    model = StableDiffusionImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1-base",
        torch_dtype=torch.float32,
        safety_checker=None
    )

    model = model.to("cuda" if torch.cuda.is_available() else "cpu")
    return model

def generate_image(prompt, base_image_path, model, output_path="output.png"):
    print(f"Generating image from prompt: {prompt}")
    
    # Load the base image
    base_image = Image.open(base_image_path).convert("RGB")
    base_image = base_image.resize((512, 512))  # Resize to match model requirements

    # Generate the image
    image = model(
        prompt=prompt,
        image=base_image,
        guidance_scale=3.0,
        num_inference_steps=100,
    ).images[0]

    # Save the generated image
    image.save(output_path)
    print(f"Image saved at {output_path}")

if __name__ == "__main__":
    model = load_model()

    base_image_path = "base_image.jpg"
    prompt = "A cartoon character with a round body, big eyes, and a cheerful expression, wearing a red hat and blue overalls, looking angry"

    generate_image(prompt, base_image_path, model, "output.png")