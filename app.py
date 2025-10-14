# Sai

from customtkinter import *
from PIL import Image
from tkinter import filedialog, StringVar

# ========== GUI FUNCTIONS ==========
def quit_program():
    app.destroy()

def login():
    user_name = entry_name.get().lower()
    user_pass = entry_pas.get()

    # Dummy login check
    if user_name == "test" and user_pass == "1234":
        login_message.configure(text="Logged IN", text_color="green")
        main_page()
    else:
        login_message.configure(text="Invalid credentials", text_color="red")

def main_page():
    frame.pack_forget()
    global main_view
    main_view = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    main_view.pack_propagate(0)
    main_view.pack(expand=True, side="right")

    CTkLabel(master=main_view, text="Main Menu", text_color="#016dff",
             anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    CTkButton(master=main_view, text="EchoCare", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=lambda: print("EchoCare clicked")).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="MedExtract", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=medextract_window).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="Quit", fg_color="transparent",
              font=("Arial Bold", 8), text_color="black", width=8, border_width=2,
              border_color='black', corner_radius=32,
              command=quit_program).pack(anchor="se", pady=(0, 20), padx=(0, 20))

def medextract_window():
    main_view.pack_forget()
    extract_view = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    extract_view.pack_propagate(0)
    extract_view.pack(expand=True, side="right")

    language_name_to_code = {
        "English": "en",
        "Tamil": "ta",
        "Hindi": "hi",
        "Telugu": "te",
        "Malayalam": "ml"
    }

    CTkLabel(master=extract_view, text="OCR Translate", text_color="#016dff",
             anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))

    CTkLabel(master=extract_view, text="Select Language", text_color="#000000",
             anchor="w", font=("Arial", 12)).pack(anchor="w", padx=(25, 0), pady=(5, 0))

    lang_option = StringVar(value="Tamil")
    lang_dropdown = CTkOptionMenu(master=extract_view, values=list(language_name_to_code.keys()), variable=lang_option)
    lang_dropdown.pack(padx=20, pady=(0, 10))

    def browse_image():
        path = filedialog.askopenfilename()
        if not path:
            return
        # GUI placeholder: show filename
        original_text_box.delete("0.0", END)
        translated_text_box.delete("0.0", END)
        original_text_box.insert("0.0", f"Loaded: {path}")
        translated_text_box.insert("0.0", f"Translated text will appear here...")

    CTkButton(master=extract_view, text="Upload Image", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=browse_image).pack(pady=12, padx=10)

    CTkLabel(master=extract_view, text="Original Text", text_color="#000000",
             anchor="w", font=("Arial", 12)).pack(anchor="w", padx=(25, 0))
    original_text_box = CTkTextbox(master=extract_view, width=250, height=100)
    original_text_box.pack(padx=20, pady=5)

    CTkLabel(master=extract_view, text="Translated Text", text_color="#000000",
             anchor="w", font=("Arial", 12)).pack(anchor="w", padx=(25, 0))
    translated_text_box = CTkTextbox(master=extract_view, width=250, height=100)
    translated_text_box.pack(padx=20, pady=5)

    CTkButton(master=extract_view, text="Back", fg_color="transparent",
              font=("Arial Bold", 10), text_color="black", width=100,
              border_width=2, border_color='black', corner_radius=8,
              command=lambda: [extract_view.pack_forget(), main_page()]).pack(pady=(10, 0))

# ========== GUI SETUP ==========
app = CTk()
app.geometry("600x480")
app.title("MedBridge_V1")
app.resizable(0, 0)

side_img = CTkImage(Image.open("./Images/main_page.jpg"), size=(300, 480))
user_icon = CTkImage(Image.open("./Images/rainy-day_D.png"), size=(20, 20))
password_icon = CTkImage(Image.open("./Images/rainy-day_W.png"), size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#016dff",
         anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign into your Account.", text_color="#7E7E7E",
         anchor="w", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))
CTkLabel(master=frame, text="  Username:", text_color="#016dff",
         anchor="w", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
entry_name = CTkEntry(master=frame, width=225, fg_color="#EEEEEE",
                      border_color="#016dff", border_width=1, text_color="#000000",
                      placeholder_text="Ex: Mark")
entry_name.pack(anchor="w", padx=(25, 0))
CTkLabel(master=frame, text="  Password:", text_color="#016dff",
         anchor="w", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
entry_pas = CTkEntry(master=frame, width=225, fg_color="#EEEEEE",
                     border_color="#016dff", border_width=1, text_color="#000000",
                     show="*", placeholder_text="ex: 9624")
entry_pas.pack(anchor="w", padx=(25, 0))
login_message = CTkLabel(master=frame, text="", text_color="red",
                         anchor="w", font=("Arial Bold", 12))
login_message.pack(anchor="w", pady=(10, 0), padx=(25, 0))
CTkButton(master=frame, text="Login", fg_color="#016dff",
           font=("Arial Bold", 12), text_color="#ffffff", width=225,
           command=login).pack(anchor="w", pady=(25, 0), padx=(25, 0))
CTkButton(master=frame, text="Quit", fg_color="transparent",
           font=("Arial Bold", 8), text_color="black", width=8, border_width=2,
           border_color='black', corner_radius=32,
           command=quit_program).pack(anchor="se", pady=(30, 20), padx=(0, 50))

app.mainloop()

"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from plyer import camera
import tensorflow as tf
import numpy as np
from PIL import Image as PILImage

class WeatherLens(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Upload or Capture Weather Image")
        self.img = KivyImage()
        btn = Button(text="Capture Photo", on_press=self.capture)
        layout.add_widget(self.img)
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout

    def capture(self, instance):
        camera.take_picture(filename='photo.jpg', on_complete=self.predict_weather)

    def predict_weather(self, path):
        interpreter = tf.lite.Interpreter(model_path="weather_model.tflite")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        img = PILImage.open(path).resize((224, 224))
        img = np.expand_dims(np.array(img, dtype=np.float32)/255.0, axis=0)

        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])
        labels = ["Sunny", "Cloudy", "Rainy", "Snowy"]
        pred = labels[int(np.argmax(output))]

        self.label.text = f"Predicted Weather: {pred}"
        self.img.source = path

WeatherLens().run()
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from plyer import camera

from main import predict

class WeatherLens(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Upload or Capture Weather Image")
        self.img = KivyImage()
        btn = Button(text="Capture Photo", on_press=self.capture)
        layout.add_widget(self.img)
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout

    def capture(self, instance):
        camera.take_picture(filename='photo.jpg', on_complete=self.predict_weather)

    def predict_weather(self, path):
        pred_label, probs = predict(path)
        self.label.text = f"Predicted Weather: {pred_label}"
        self.img.source = path

WeatherLens().run()
