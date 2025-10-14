# Sai

from customtkinter import *
from PIL import Image
from tkinter import filedialog
from main import predict

app = CTk()
app.geometry("800x600")
app.title("Skylit_V1")
app.resizable(True, True)

set_appearance_mode("Dark")  # initial mode

# Keep global references to images
side_image = CTkImage(Image.open("./Images/main_page.jpg"), size=(400, 600))
light_icon = CTkImage(Image.open("./Images/rainy-day_D.png"), size=(20, 20))
dark_icon = CTkImage(Image.open("./Images/rainy-day_W.png"), size=(20, 20))

button = None
switch = None
image_label = None
upload_button = None
quit_button = None

def get_theme_colors():
    current = get_appearance_mode()
    if current == "Light":
        return "#000000", "#dcf1ff", "#74faff", light_icon
    else:
        return "#ffffff", "#1a1a1a", "#5ae2ff", dark_icon

def update_theme():
    text_color, hover_color, border_color, icon = get_theme_colors()
    if button:
        button.configure(text_color=text_color, hover_color=hover_color, border_color=border_color, image=icon)
    if upload_button:
        upload_button.configure(text_color=text_color, hover_color=hover_color, border_color=border_color)
    if quit_button:
        quit_button.configure(text_color=text_color, border_color=border_color)
    app.update()

def toggle_theme():
    set_appearance_mode("Dark" if get_appearance_mode() == "Light" else "Light")
    update_theme()

def quit_program():
    app.destroy()

def upload_image():
    global image_label
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    if file_path:
        img = CTkImage(Image.open(file_path), size=(200, 200))
        if image_label:
            image_label.configure(image=img)
            image_label.image = img
        else:
            image_label = CTkLabel(master=frame, text="", image=img)
            image_label.image = img
            image_label.place(relx=0.5, rely=0.35, anchor="center")

        # model prediction here
        label, confidence = predict(file_path)
        if label:
            result_text = f"Prediction: {label} ({confidence:.2f}%)"
        else:
            result_text = "Prediction failed"

        # Display prediction
        CTkLabel(master=frame, text=result_text,
                 font=("Arial", 15, "bold")).place(relx=0.5, rely=0.65, anchor="center")


def main():
    global button, switch, frame

    # Left side image
    CTkLabel(master=app, text="", image=side_image).pack(expand=True, side="left")

    # Right frame
    frame = CTkFrame(master=app, width=500, height=600)
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    # Main button
    text_color, hover_color, border_color, icon = get_theme_colors()
    CTkButton(master=frame, text="Detect Weather", fg_color="transparent", text_color=text_color, corner_radius=32, hover_color=hover_color,
              font=("Bonheur Royale", 20, "bold"), width=150, height=40, border_color=border_color, border_width=1, image=icon,
              compound="left", command=upload_image).place(relx=0.5, rely=0.8, anchor="center")

    # Theme switch
    switch = CTkSwitch(master=frame, text="Theme", font=("Bonheur Royale", 18, "normal"), command=toggle_theme)
    switch.place(relx=0.2, rely=0.05, anchor="center")

    # Quit button
    CTkButton(master=frame,
              text="Quit",
              fg_color="transparent",
              text_color=text_color,
              font=("Bonheur Royale", 15, "bold"),
              width=100,
              border_width=1,
              border_color=border_color,
              corner_radius=32,
              command=quit_program).place(relx=0.5, rely=0.95, anchor="center")

main()
app.mainloop()