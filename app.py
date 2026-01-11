import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

st.set_page_config(page_title="Plant Disease Detection", layout="centered")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("plant_disease_model.h5")

model = load_model()

# Load class indices
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse mapping: index → class name
idx_to_class = {v: k for k, v in class_indices.items()}

st.title("🌿 Plant Disease Detection System")
st.write("Upload a plant leaf image to detect disease")

uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=400)  # changed use_column_width to width

    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    class_name = idx_to_class[class_idx]
    confidence = np.max(prediction) * 100  # convert to percentage

    # Determine Healthy or Unhealthy
    if "healthy" in class_name.lower():
        status = "Healthy ✅"
        disease = "None"
    else:
        status = "Unhealthy ❌"
        disease = class_name.replace("_", " ").replace("___", " - ")

    # Display results
    st.success(f"**Status:** {status}")
    if disease != "None":
        st.info(f"**Disease:** {disease}")
    st.info(f"**Confidence:** {confidence:.2f}%")
