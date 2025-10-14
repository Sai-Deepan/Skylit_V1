# Skylit: Weather Detection & Analysis App

**Skylit** is a lightweight, user-friendly desktop application that enables real-time weather detection and analysis using images. With a sleek GUI, Skylit allows users to upload weather images, detect conditions, and view predictions with confidence scores. It is built with a focus on simplicity, speed, and cross-platform usability.

---

## Features

* Detect weather conditions from images (Rain, Snow, Fog, Dew, etc.).
* Interactive GUI built with **Custom Tkinter**.
* Confidence percentage display for predictions.

---

## Project Structure

* `main.py` – Core weather prediction logic using TensorFlow Lite.
* `app.py` – Custom Tkinter GUI integrating image upload, prediction, and theme switching.
* `Dataset/` – Directory containing the trained `.tflite` model.
* `Images/` – GUI assets such as icons, sample images, and side images.

---

## Project Images

**Skylit GUI:**

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/42ddb0af-b75e-462b-b7ee-343b633650d8" />


<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/30935f88-4387-4774-a172-8976e3306f31" />


<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/117e4403-a861-4780-9d22-1460b981c1ab" />

---

## Tech Stack

### Frontend (User Interaction)

* **Custom Tkinter** — GUI framework for interactive desktop UI
* **Pillow (PIL)** — Image processing for display in the GUI

### Backend (Core Logic & Model)

* **Python 3.10+** — Main programming language
* **TensorFlow Lite** — Lightweight weather detection model
* **NumPy** — Numerical computations and array manipulation

---

## Getting Started

### Prerequisites

* Python 3.10+
* Required Python packages listed in `requirements.txt`

---

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Skylit.git
   cd Skylit
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the TFLite model is in the `Dataset/` directory.

---

### Usage

* **Run the GUI:**

  ```bash
  python app.py
  ```

* **Upload Image for Weather Detection:**
  Click the **“Detect Weather”** button, select your weather image, and view the predicted condition along with confidence scores.

* **Switch Themes:**
  Use the toggle to switch between **Light** and **Dark** modes.

---

## Supported Weather Conditions

* Dew
* Fog
* Rain
* Snow

*(Expandable with more weather types if retraining the model.)*

---

## Why Skylit?

Skylit brings ML-powered weather detection to your desktop in a simple and interactive way. It is designed for users who want quick and accurate analysis of weather conditions from images, with an easy-to-use interface.

---

## Roadmap

* Expand supported weather types.
* Improve model accuracy and speed.
* Add real-time webcam capture for weather detection.
* Develop web and mobile versions of Skylit.
* Include historical weather logging and analysis.

---

## Contributors

* Deepan Sai ([skdeepan.sai@gmail.com](mailto:skdeepan.sai@gmail.com))
  
---

## Contact & Support

For questions, issues, or contributions, please open an issue on GitHub or contact the contributors.

Thank you for using **Skylit** 

Do you want me to do that?



