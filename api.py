import openai
import requests
from PIL import Image
from io import BytesIO

# Set OpenAI API key
openai.api_key = ""
def generate_image_with_dalle(prompt):
    """
    Use DALL-E to generate an image based on a prompt.
    """
    try:
        # Generate the image
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            quality="standard",
            size="1024x1024"
        )
        
        # Extract the URL from the response
        if hasattr(response, 'data') and response.data:
            return response.data[0].url
        elif 'data' in response and response['data']:
            return response['data'][0]['url']
        else:
            print("No image URL found in the response.")
            return None
            
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return None

def download_image(url, save_path=None):
    """Download image from URL and optionally save to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        image = Image.open(BytesIO(response.content))
        
        if save_path:
            image.save(save_path)
        
        return image
    except Exception as e:
        print(f"Error downloading image: {str(e)}")
        return None

def process_image(base_image_description, user_prompt):
    """
    Process the base image description and user prompt to generate an image.
    Returns the path to the generated image.
    """
    # Combine the base image description and user prompt
    refined_prompt = f"{base_image_description} The character is {user_prompt}, actively using its well-defined hands and legs. The image should be in a cartoon style, with vibrant colors and a playful atmosphere. Ensure the creature's horns are clearly visible and match the description above. Do not include long ears or any features not described here."
    
    # Generate the image
    result_url = generate_image_with_dalle(refined_prompt)
    
    if result_url:
        # Download and save the generated image
        output_path = "output_image.png"
        download_image(result_url, output_path)
        return output_path
    
    return None

# Example usage (for testing outside of Telegram)
if __name__ == "__main__":
    # Detailed description of the base image
    base_image_description = """
    The image features a cartoon-style creature with a round, fluffy, and slightly irregular body. 
    The creature is predominantly light blue with subtle shading that adds depth and a soft texture. 
    Its body is slightly asymmetrical, giving it a dynamic, bouncy appearance. 

    The creature has two well-defined, short arms with small hands, each with four fingers and a thumb, positioned in a way that shows they are functional and capable of holding objects. 
    The hands are detailed, with visible fingers and a soft, rounded appearance. 
    The creature also has two short, stubby legs with small feet, each with three toes, tucked beneath its rounded body. 
    The legs are positioned to show they are capable of supporting the creature's weight and movement.

    Its face is highly expressive and friendly, characterized by large, round, black eyes with small white highlights that give them a glossy, reflective appearance. 
    The creature’s mouth is wide open in a cheerful expression, revealing a pink tongue and four small, sharp teeth—two on the upper row and two on the lower row.

    Two curved, slightly translucent white horns protrude from the sides of its head, each with a soft gradient towards the base, blending seamlessly into the blue fur. 
    The creature's ears are small and rounded, blending into the overall fluffy silhouette. 
    Small, curved black lines near its limbs and face add definition and movement.

    Surrounding the creature are small, white bubble-like elements floating in the air, enhancing the sense of movement as if it is joyfully jumping or floating. 
    The background is a solid, pastel blue that complements the creature’s color while maintaining a clean and minimalistic aesthetic.

    A faint, oval-shaped shadow is visible beneath the creature, giving the impression that it is hovering or bouncing slightly above the ground.
    """
    
    # User prompt
    user_prompt = "cooking a tasty dish"
    
    print(f"Processing image with prompt: {user_prompt}")
    result = process_image(base_image_description, user_prompt)
    
    if result:
        print(f"Image generated successfully and saved to {result}")
    else:
        print("Failed to generate image")