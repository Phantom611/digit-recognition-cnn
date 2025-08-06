import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# Load model
model = load_model("digit_recognition_cnn.h5")

# App title
st.title("🧠 Handwritten Digit Recognition")
st.write("Upload a **28x28 grayscale** image of a digit (0-9).")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("L")  # Grayscale
    image = ImageOps.invert(image)  # Invert colors (white digit on black)
    image = image.resize((28, 28))

    # Display image
    st.image(image, caption="Uploaded Digit", width=150)

    # Preprocess
    img_array = np.array(image).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)
    confidence = np.max(prediction)

    # Display result
    st.success(f"Predicted Digit: **{predicted_digit}** with confidence {confidence:.2f}")
