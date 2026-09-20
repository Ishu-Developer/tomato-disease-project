# Tomato Disease Detection Using Image Processing

## College MINI Project

* Project Type: College MINI Project
* Domain: Image Processing / Computer Vision
* Team Size: 2
* Repository: Ishu-Developer/tomato-disease-project

Project Objective

This project is a tomato leaf image classification system designed to identify three conditions from tomato leaf images:

1. Early Blight
2. Healthy
3. Late Blight

The project focuses primarily on **Image Processing / Computer Vision**, with Machine Learning / Deep Learning used as a supporting technique for image classification.

The final application is intended as an AI-assisted image-based screening prototype, not as professional agricultural diagnosis.

## Dataset Work Completed
<br>
For the current MINI Project scope, three classes were selected:
<br>

| Class       | Total Images |
|---|---|
|Early Blight | 1,000        |
| Healthy     | 1,591        |
|Late Blight  | 1,909        |
| Total       | 4,500        |

All 4,500 selected images are being used in the project dataset.
<br>

### Dataset Split

The dataset has been divided into three separate subsets:

| Class | Train | Validation | Test | Total
|--|--|--|--|--|
| Early Blight| 700 | 150 | 150 | 1,000 |
| Healthy | 1,114 | 239 | 238 | 1,591 |
| Late Blight | 1,336 | 286 | 287 | 1,909 |
| Total | 3,150 | 675 | 675 | 4,500 |

The split is approximately 70% Training / 15% Validation / 15% Testing.
<br>
Meaning of the folders
1. train/ — images used for model learning.
2. validation/ — images used during model development and tuning.
3. test/ — held-out images used for final evaluation.
The three subsets must remain independent to avoid data leakage.

## Work Completed So Far
* Selected the final project scope of three tomato-leaf classes.
* Prepared a total of 4,500 images.
* Created the Training, Validation, and Test split.
* Maintained separate class folders.
* Prepared the project for the Image Processing and ML stages.

Next Steps

1. Image Processing / Preprocessing

The next development stage will use image-processing techniques such as:

* Image loading
* Image resizing
* Noise reduction / filtering
* Image enhancement
* Contrast improvement where appropriate
* Pixel normalization
* Visualization of before/after preprocessing results

**OpenCV will be used for the main image-processing work.**

2. Dataset Analysis

We will inspect:

* Image dimensions
* Image quality
* Class distribution
* Sample images from each class

**Effects of preprocessing**

3. Model Development

A suitable image-classification model will be selected and trained using the prepared dataset.
<br>
The model development stage will include:

1. Training
2. Validation
3. Model improvement
4. Final model saving

4. Model Evaluation

The final model will be evaluated on the test set using appropriate metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

No performance metrics will be reported until the model has actually been trained and evaluated.

## Technology Stack

**Python**
* OpenCV
* NumPy
* Pandas
* Matplotlib
* PyTorch
* Streamlit
* Jupyter Notebook
* Git / GitHub
* VS Code

## Project Status

* Current Stage: Dataset preparation completed
* Dataset: 4,500 images
* Classes: 3
* Train: 3,150 images
* Validation: 675 images
* Test: 675 images

Next Stage: Image Processing / OpenCV preprocessing