"""Reusable image preprocessing functions for tomato disease detection."""

from pathlib import Path

import cv2
import numpy as np


DEFAULT_IMAGE_SIZE = (224, 224)


def load_image(image_path: str | Path) -> np.ndarray:
    """Load an image from disk in OpenCV BGR format."""
    path = Path(image_path)

    if not path.is_file():
        raise FileNotFoundError(f"Image file not found: {path}")

    image = cv2.imread(str(path))

    if image is None:
        raise ValueError(f"Could not decode image: {path}")

    return image


def resize_image(
    image: np.ndarray,
    size: tuple[int, int] = DEFAULT_IMAGE_SIZE,
) -> np.ndarray:
    """Resize an image to (width, height)."""
    if not isinstance(image, np.ndarray) or image.size == 0:
        raise ValueError("Input image must be a non-empty NumPy array.")

    width, height = size

    if width <= 0 or height <= 0:
        raise ValueError("Image width and height must be positive.")

    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def apply_median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """Reduce some image noise using a median filter."""
    if not isinstance(image, np.ndarray) or image.size == 0:
        raise ValueError("Input image must be a non-empty NumPy array.")

    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer of at least 3.")

    return cv2.medianBlur(image, kernel_size)


def enhance_contrast(image: np.ndarray) -> np.ndarray:
    """Apply CLAHE to the LAB lightness channel."""
    if not isinstance(image, np.ndarray) or image.size == 0:
        raise ValueError("Input image must be a non-empty NumPy array.")

    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lightness, channel_a, channel_b = cv2.split(lab_image)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8),
    )
    enhanced_lightness = clahe.apply(lightness)

    enhanced_lab = cv2.merge(
        (enhanced_lightness, channel_a, channel_b)
    )

    return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)


def preprocess_image(
    image_path: str | Path,
    size: tuple[int, int] = DEFAULT_IMAGE_SIZE,
    denoise: bool = False,
    improve_contrast: bool = False,
) -> np.ndarray:
    """Load, optionally enhance, and resize an image.

    Returns a BGR image with dimensions (height, width, 3).
    Optional enhancements are disabled by default.
    """
    image = load_image(image_path)

    if denoise:
        image = apply_median_filter(image)

    if improve_contrast:
        image = enhance_contrast(image)

    return resize_image(image, size)