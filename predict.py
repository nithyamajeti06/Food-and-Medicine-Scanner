# Importing libraries
import tensorflow as tf
import numpy as np
import pyttsx3  # Text-to-Speech
from PIL import Image

# Adding the model
model = tf.keras.models.load_model("food_model.h5")

# Creating a dictionary for the class names
class_names = {0: "Ketchup Chips", 
               1: "Classic Oreos", 
               2: "Vitamin B12 Medicine", 
               3: "Tylenol", 
               4: "Advil", 
               5: "Baby Carrots", 
               6: "Potatoes",
               7: "Tomatoes", 
               8: "Strawberries", 
               9: "Mac and Cheese", 
               10: "Ripe Bananas", 
               11: "Underripe Banana", 
               12: "Overripe Banana", 
               13: "Vitamin D3 Medicine", 
               14: "Red Onions", 
               15: "White Onions",
               16: "Yellow Onions",
               17: "Peanut Butter",
               18: "Green Grapes",
               19: "Purple Grapes",
               20: "Pancake Mix",
               21: "Spinach",
               22: "Arugula",
               23: "Mushroom Can",
               24: "Chickpea Can",
               25: "Corn Can" }

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to enhance the image
def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))  # Resize to match model input
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def predict(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    class_index = np.argmax(predictions)  # Get class with highest probability
    item_name = class_names.get(class_index, "Unknown item")  

    # To say the result
    engine.say(f"This is a {item_name}")
    engine.runAndWait()

    # Return the predicted item name
    return item_name
