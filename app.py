# Web app deployed using streamlit
import streamlit as st
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

# Title and Sidebar
st.title('Potato Leaf Health Detection!')
with st.sidebar:
    st.header('Data requirements')
    st.caption('Upload a clear image of a single potato leaf.')
    with st.expander('Supported Image Formats'):
        st.markdown('.png')
        st.markdown('.jpeg')
        st.markdown('.jpg')
    st.divider()
    st.caption("<p style = 'text-align:center'>Developed by Krishna</p>", unsafe_allow_html=True)

# Button state handling
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False}

def clicked(button):
    st.session_state.clicked[button] = True

st.button("Let's get started", on_click=clicked, args=[1])

# Load Model and Class Names
model = tf.keras.models.load_model("saved_models/4", compile=False)
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
IMAGE_SIZE = (256, 256)  # Model's expected input size

# Prediction Logic
if st.session_state.clicked[1]:
    uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        try:
            # Read binary data and open image
            image = Image.open(BytesIO(uploaded_file.getvalue()))
            st.image(image, caption="Uploaded Leaf Image")

            # Resize and convert to numpy array
            image_resized = image.resize(IMAGE_SIZE)
            image_np = np.array(image_resized)

            # Ensure correct shape (add batch dimension)
            img_batch = np.expand_dims(image_np, 0)

            # Make prediction
            predictions = model.predict(img_batch)
            predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
            confidence = np.max(predictions[0])

            # Display Prediction
            result_html = f"""
            <div style="
                background-color:green;
                padding:20px;
                border-radius:10px;
                box-shadow:2px 2px 10px rgba(0,0,0,0.1);
                text-align:center;
                margin-top:20px;
            ">
                <h3 style="color:#333;">Predicted Health Status</h3>
                <p style="font-size:20px;"><strong>Class:</strong> {predicted_class}</p>
                <p style="font-size:20px;"><strong>Confidence:</strong> {float(confidence)}</p>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)

            # st.header('Predicted Health Status')
            # st.write(f"Class: **{predicted_class}**")
            # st.write(f"Confidence: **{float(confidence)}**")

        except Exception as e:
            st.error(f"Error processing the uploaded image: {e}")