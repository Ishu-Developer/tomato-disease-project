import streamlit as st
import numpy as np
import cv2
from preprocessing.image_processor import (
    resize_image,
    apply_median_filter,
    enhance_contrast,
)

st.set_page_config(
    page_title="Tomato Disease Detection",
    page_icon="🍅",
    layout="wide",
)

st.title("🍅 Tomato Disease Detection")
st.write(
    "Upload a tomato leaf image to view the original image "
    "and its OpenCV-preprocessed version."
)

st.info(
    "This is an image-processing prototype. Disease predictions "
    "will be added after the trained model is integrated."
)

uploaded_file = st.file_uploader(
    "Choose a tomato leaf image",
    type=["jpg", "jpeg", "png"],
)

st.subheader("Preprocessing Options")

denoise = st.checkbox(
    "Apply Median Filtering (Noise Reduction)",
    value=False,
)

improve_contrast = st.checkbox(
    "Apply Contrast Enhancement (CLAHE)",
    value=False,
)

if uploaded_file is not None:
    try:
        file_bytes = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)
        original_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if original_bgr is None:
            st.error("Could not read this image. Please upload a valid image.")
        else:
            processed_bgr = original_bgr.copy()

            if denoise:
                processed_bgr = apply_median_filter(processed_bgr)

            if improve_contrast:
                processed_bgr = enhance_contrast(processed_bgr)

            processed_bgr = resize_image(processed_bgr, size=(224, 224))

            original_rgb = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2RGB)
            processed_rgb = cv2.cvtColor(processed_bgr, cv2.COLOR_BGR2RGB)

            left, right = st.columns(2)

            with left:
                st.subheader("Original Image")
                st.image(original_rgb, width=400)
                st.caption(
                    f"Dimensions: {original_bgr.shape[1]} × "
                    f"{original_bgr.shape[0]} pixels"
                )

            with right:
                st.subheader("Preprocessed Image")
                st.image(processed_rgb, width="stretch")
                st.caption("Resized to 224 × 224 pixels")

            st.success("Image preprocessing completed successfully.")

    except Exception as error:
        st.error(f"Image processing failed: {error}")