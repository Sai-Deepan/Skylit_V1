# Sai

import tensorflow as tf
import numpy as np
from PIL import Image

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="./Dataset/model_unquant.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

labels = ["Dew", "Fog", "Rain", "Snow"]

# Prepare image
def preprocess_image(img_path):
    img = Image.open(img_path).convert("RGB").resize((224, 224))
    img = Image.open(img_path).resize((224, 224))
    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Run inference
def predict(img_path):
    try:
        input_data = preprocess_image(img_path)
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])
        output = tf.nn.softmax(output).numpy()
        predicted_index = int(np.argmax(output))
        predicted_label = labels[predicted_index]
        confidence = output[0][predicted_index] * 100
        return predicted_label, confidence

    except Exception as e:
        print("Prediction failed:", e)
        return None, 0