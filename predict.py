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

items_info = {
        "Ketchup Chips": "Consists of 150 calories per 15 chips and potential allergy warnings is it contains mustard, milk, wheat",
        "Classic Oreos": "Consists of 160 calories per 3 cookies and may contain peanuts",
        "Vitamin B12 Medicine": "Vitamin B12 provides which is used to support energy production, nerve function, and red blood cell formation",
        "Tylenol": "Tylenol is commonly used to relieve headaches, reduce fever, and ease muscle pain",
        "Advil": "Advil is commonly used to reduce inflammation, relieve pain, and lower fever",
        "Baby Carrots": "Consists of 35 calories per 100 grams",
        "Potatoes": "Consists of 87 calories per 100 grams",
        "Tomatoes": "Consists of 18 calories per 100 grams",
        "Strawberries": "Consists of 33 calories per 100 grams",
        "Mac and Cheese": "Consists of 164 calories per 100 grams and potential allergy warnings is it contains dairy, gluten and egg",
        "Unripened bananas": "Consists of 92 calories per 100 grams",
        "Ripe Bananas": "Consists of 89 calories per 100 grams",
        "Overripe Bananas": "90-100 calories per 100 grams",
        "Vitamin D Medicine": "Vitamin D helps the body absorb calcium, supporting bone health and immune function",
        "Red Onions": "Consists of 36.3 calories per 100 grams",
        "White Onions": "Consists of 131 calories per 100 grams",
        "Yellow Onions": "Consists of 132 calories per 100 grams",
        "Purple Grapes": "Consists of 71 calories per 100 grams",
        "Green Grapes": "Consists of 69 calories per 100 grams",
        "Pancake Mix": "Consists of 227 calories per 100 grams and watch out for milk, wheat and egg proteins",
        "Spinach": "Consists of 23 calories per 100 grams",
        "Arugula": "Consists of 25 calories per 100 grams",
        "Chickpea Can": "Consists of 120 calories per 130 grams",
        "Corn Can": "Consists of 60-70 calories per 125 grams",
        "Mushroom Can": "Consists of 22 calories per 100 grams"
}

def know_more(product):
    #print(product)
    #print(items_info.keys())
    if product in items_info:
        info = items_info[product]
        engine.say(info)
        engine.runAndWait()

    else:
        engine.say("No information found")
        engine.runAndWait()

