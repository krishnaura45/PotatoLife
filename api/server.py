# Importing libraries
from fastapi import FastAPI,File,UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
app=FastAPI()

MODEL = tf.keras.models.load_model("saved_models/4", compile=False)
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")  # specifying entry/end point

# To check if our server is alive or stopped 
async def ping():    
    return "Hello, the server is live now"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))    # reading pillow image as a numpy array
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Predicts the class of potato leaf i.e. whether it is healthy or diseased.

    Args:
        file : A single potato leaf image in jpg/png format
        e.g. {sample_leaf.jpg}

    Returns:
        json response containing predicted class along with confidence score
    """
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)   # adding extra dimension to image
    
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8000)
