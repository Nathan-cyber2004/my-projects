## AI Image Classifier

A web-based image classification application built with Streamlit and TensorFlow that uses a pretrained MobileNetV2 deep learning model to identify objects in uploaded images.

Users can upload an image and receive the top 3 predicted labels along with confidence scores in real time.

# Features

Upload images in JPG, JPEG, or PNG format

Real-time image classification using a pretrained CNN (MobileNetV2)

Displays top 3 predictions with confidence scores

Clean, interactive Streamlit UI

Model caching for faster performance

# How It Works

The app loads a pretrained MobileNetV2 model trained on the ImageNet dataset.

The user uploads an image through the Streamlit interface.

The image is:

Resized to 224 × 224

Preprocessed using MobileNetV2’s preprocessing pipeline

The model performs inference on the image.

The top 3 predictions are decoded into human-readable labels and displayed with confidence scores.

# Technologies Used

Python

Streamlit – Web application framework

TensorFlow / Keras – Deep learning model and inference

MobileNetV2 – Pretrained convolutional neural network

OpenCV – Image resizing

NumPy – Numerical operations

Pillow (PIL) – Image handling

# Installation

Clone the repository:

git clone https://github.com/your-username/ai-image-classifier.git
cd ai-image-classifier


Install dependencies:

pip install streamlit tensorflow opencv-python pillow numpy

# Running the App
streamlit run file_name.py


Once running, open the provided local URL in your browser.

# Project Structure
ai-image-classifier/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
└── requirements.txt (optional)

# Example Output
Predictions:
• golden_retriever: 0.82
• Labrador_retriever: 0.11
• cocker_spaniel: 0.04

# Limitations

Model is limited to the ImageNet dataset (1,000 classes)

Predictions may be inaccurate for:

Low-quality images

Uncommon or abstract objects

Not intended for production or safety-critical use

# Future Improvements

Display confidence bars for predictions

Support webcam or real-time classification

Add Grad-CAM visual explanations

Deploy publicly using Streamlit Cloud

Allow switching between different pretrained models

# License

This project is for educational and portfolio purposes.

# Author

Developed by Nathan Pereira
Computer Science student with interests in AI, Robotics, and Game Development
