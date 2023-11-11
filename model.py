from dotenv import load_dotenv
import os
import requests
import io
from PIL import Image
import uuid
load_dotenv()

#Get models
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
apiKey = "Bearer " + os.environ["SDAPI_TOKEN"]

headers = {"Authorization": apiKey}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "A cat wear a red dress and hold a lolipop",
})
# You can access the image with PIL.Image for example

image_name = str(uuid.uuid4())
image = Image.open(io.BytesIO(image_bytes))
save_img = image.save(f'{image_name}.jpeg')