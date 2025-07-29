# Food-and-Medicine-Scanner
This project is created for visually impaired users to help identify different foods and medicines. The project is still in development and aims to provide user with other additional information about the product the user scans like the nutritional info and potential allergy warnings. 

## 🔍 Items Detected by ScAnalyze

| Category         | Detected Items                                                                              |
|------------------|---------------------------------------------------------------------------------------------|       
| 🍽️ Packaged Foods | Ketchup Chips, Classic Oreos, Mac and Cheese, Pancake Mix                                  |
| 🥕 Vegetables     | Baby Carrots, Potatoes, Tomatoes, Spinach, Arugula, Red Onions, White Onions, Yellow Onions| 
| 🍌 Fruits         | Strawberries, Ripe Bananas, Underripe Banana, Overripe Banana, Green Grapes, Purple Grapes |
| 🥫 Canned Goods   | Mushroom Can, Chickpea Can, Corn Can                                                       |
| 💊 Medications    | Tylenol, Advil, Vitamin B12 Medicine, Vitamin D3 Medicine                                  |
| 🥜 Others         | Peanut Butter                                                                              |


# Clone the repositiory 
git clone https://github.com/yourusername/Food-and-Medicine-Scanner.git

# Navigate into the project folder
cd Food-and-Medicine-Scanner

# Create a virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt

# Run the scanner
python predict.py
