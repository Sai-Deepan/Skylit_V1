# Sai
"""
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="./Dataset/model_unquant.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare image
def preprocess_image(img_path):
    img = Image.open(img_path).resize((224, 224))
    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Run inference
def predict(img_path):
    input_data = preprocess_image(img_path)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    return output

result = predict("./test_weather.jpg")
print("Raw output:", result)

labels = ["Dew", "Fog", "Rain", "Snow"]
for i, label in enumerate(labels):
    print(f"{label}: {result[0][i]*100:.2f}%")

predicted_index = int(np.argmax(result))
print("Predicted Weather:", labels[predicted_index])"""

import tensorflow as tf
import numpy as np
from PIL import Image

# Load TFLite model once (singleton)
interpreter = tf.lite.Interpreter(model_path="./Dataset/model_unquant.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

labels = ["Dew", "Fog", "Rain", "Snow"]

def preprocess_image(img_path):
    img = Image.open(img_path).resize((224, 224))
    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict(img_path):
    input_data = preprocess_image(img_path)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    predicted_index = int(np.argmax(output))
    return labels[predicted_index], output[0]  # return label + raw probabilities
