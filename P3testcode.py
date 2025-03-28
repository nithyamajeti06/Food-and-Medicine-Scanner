# Import necessary libraries
import tkinter as tk
import cv2
import predict 
from PIL import Image, ImageTk

# Set font and colors
myFont = "Gill Sans MT"
textColor = "black" 
backgroundColor = 'white'

# Function to start camera
def start_camera():
    global cap
    cap = cv2.VideoCapture(0)  # Open camera
    show_frame()

# Function to show frame from camera
def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.config(image=imgtk)
        camera_label.after(10, show_frame)  # Refresh frame

# Function to take picture
def take_picture():
    ret, frame = cap.read()
    cap.release()
    if ret:
        img_path = "captured_image.jpg"
        cv2.imwrite(img_path, frame)
        process_image(img_path)
    else:
        show_output_screen("Failed to capture image.")

# Function to process image
def process_image(img_path):
    prediction_result = predict.predict(img_path) 
    output_text = f"Picture taken successfully!\nPrediction: {prediction_result}"
    show_output_screen(output_text)

# Function to show output screen
def show_output_screen(output):
    camera_frame.pack_forget()
    output_label.config(text=output)
    output_frame.pack(expand=True)

# Function to go back to home screen
def go_home():
    output_frame.pack_forget()
    home_frame.pack(expand=True)

# Function to open camera screen
def open_camera_screen():
    home_frame.pack_forget()
    camera_frame.pack(expand=True)
    start_camera()

# Function to close app
def close_app():
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Camera")
root.geometry("1200x900")
root.bind("<space>", lambda event: take_picture())
root.attributes('-fullscreen', True)

# Home Screen
home_frame = tk.Frame(root, bg=backgroundColor)
home_frame.pack(expand=True)
root.config(background=backgroundColor)
tk.Label(home_frame, text="TAKE A PICTURE OF YOUR PRODUCT", bg=backgroundColor, font=(myFont, 30, "bold"), fg=textColor).pack(pady=20)
tk.Button(home_frame, text="Open Camera", command=open_camera_screen, font=(myFont, 50, "bold"), bg="green", fg=textColor, padx=20, pady=10, relief=tk.RAISED, borderwidth=3).pack(pady=10)
tk.Button(home_frame, text="Close screen", command=close_app, font=(myFont, 20, "bold"), bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3).pack(pady=10)

# Camera Screen
camera_frame = tk.Frame(root)
camera_label = tk.Label(camera_frame)
camera_label.pack()
tk.Button(camera_frame, text="Capture", command=take_picture, font=(myFont, 20, 'bold'), bg="#FF5733", fg="white", padx=20, pady=10, relief=tk.RAISED, borderwidth=3).pack(pady=10)
tk.Label(camera_frame, text="CLICK SPACE OR CAPTURE", bg='white', font=(myFont, 30, "bold"), fg=textColor).pack(pady=20)
tk.Button(camera_frame, text="Close screen", command=close_app, font=(myFont, 20, "bold"), bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3).pack(pady=10)

# Output Screen
output_frame = tk.Frame(root)
output_label = tk.Label(output_frame, text="", font=(myFont, 20, 'bold'))
output_label.pack(pady=20)
tk.Button(output_frame, text="Back to home", command=go_home, font=(myFont, 30, 'bold'), bg="green", fg="white", padx=30, pady=15, relief=tk.RAISED, borderwidth=4).pack()
tk.Button(output_frame, text="Close screen", command=close_app, font=(myFont, 20, "bold"), bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3).pack(pady=10)

# Run the application
root.mainloop()

