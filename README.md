# Lung X-ray Classification: Normal vs Pneumonia (Using TorchVision)

This project uses deep learning techniques to classify chest X-ray images as **Normal** or **Pneumonia**. We leverage **TorchVision** pre-trained models (like **ResNet**, **VGG**, and **DenseNet**) and fine-tune them on a dataset of lung X-ray images for binary classification.

The project is organized into a pipeline that covers the entire machine learning workflow from data ingestion to model deployment.

## Project Overview

This project classifies lung X-ray images into two categories: **Normal** and **Pneumonia** using deep learning models. It fine-tunes pre-trained models like **ResNet**, **VGG**, and **DenseNet** for the binary classification task. The pipeline includes data processing, model training, evaluation, and deployment.

## Features

- **Image Classification**: Classifies X-ray images into two categories: **Normal** or **Pneumonia**.
- **Data Augmentation**: Implements random rotations, flipping, and color jitter using TorchVision.
- **Model Fine-tuning**: Fine-tunes pre-trained models (e.g., ResNet) on the X-ray dataset.
- **Model Visualization**: Visualizes training accuracy, loss, and confusion matrix.
- **Logging and Monitoring**: Tracks training progress, logs, and metrics.

## Requirements

Ensure you have the following Python packages installed:

- Python 3.11+
- PyTorch
- TorchVision
- NumPy
- Pillow
- tqdm
- logging
- BentoMl

You can install the dependencies with:

```bash
pip install -r requirements.txt
