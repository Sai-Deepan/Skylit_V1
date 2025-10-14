# Sai

from customtkinter import *
from PIL import Image
from tkinter import filedialog

app = CTk()
app.geometry("710x600")
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

def open_image():
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
            image_label.place(relx=0.5, rely=0.65, anchor="center")

def main():
    global button, switch

    # Left side image
    CTkLabel(master=app, text="", image=side_image).pack(expand=True, side="left")

    # Right frame
    frame = CTkFrame(master=app, width=300, height=480)
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    # Main button
    text_color, hover_color, border_color, icon = get_theme_colors()
    button = CTkButton(master=frame,
                       text="Detect Weather",
                       fg_color="transparent",
                       text_color=text_color,
                       corner_radius=32,
                       hover_color=hover_color,
                       font=("Bonheur Royale", 20, "bold"),
                       width=150,
                       height=40,
                       border_color=border_color,
                       border_width=1,
                       image=icon,
                       compound="left")
    button.place(relx=0.5, rely=0.4, anchor="center")

    # Theme switch
    switch = CTkSwitch(master=frame, text="", command=toggle_theme)
    switch.place(relx=0.5, rely=0.2, anchor="center")

    #Upload Image
    def open_image():
        global image_label
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
        )
        if file_path:
            # Load and display image
            img = CTkImage(Image.open(file_path), size=(200, 200))
            if image_label:
                image_label.configure(image=img)
                image_label.image = img  # prevent garbage collection
            else:
                image_label = CTkLabel(app, text="", image=img)
                image_label.image = img
                image_label.pack(pady=20)

    CTkButton(app, text="Upload Image", command=open_image).pack(pady=40)

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
              command=quit_program).place(relx=0.5, rely=0.8, anchor="center")

main()
app.mainloop()

"""

def main_page():


    CTkLabel(master=main_view, text="Main Menu", text_color="#016dff",
             anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    CTkButton(master=main_view, text="Skylit", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=lambda: print("EchoCare clicked")).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="Skylit", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="Quit", fg_color="transparent",
              font=("Arial Bold", 8), text_color="black", width=8, border_width=2,
              border_color='black', corner_radius=32,
              command=quit_program).pack(anchor="se", pady=(0, 20), padx=(0, 20))

def sky_search():
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
"""