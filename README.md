# Deep Learning-Based PCB Defect Classification

## Overview

This project presents a deep learning-based system for the automated detection and classification of defects in Printed Circuit Boards (PCBs) using image data.

Manual inspection of PCBs is often time-consuming and prone to human error. The objective of this project is to develop an efficient and reliable solution that improves accuracy, consistency, and scalability in defect detection.

---

## Problem Statement

The goal is to classify PCB image patches into multiple categories, including six defect types and a non-defective class, using deep learning techniques.

---

## Objectives

### Primary Objectives

* Develop a multi-class image classification model for PCB defect detection
* Achieve high performance in terms of:

  * Accuracy
  * Precision
  * Recall
  * F1-score
* Design a reproducible data pipeline including:

  * Data preprocessing
  * Normalization
  * Data augmentation

---

## Defect Classes

The model classifies PCB images into the following categories:

* Missing Hole
* Mouse Bite
* Open Circuit
* Short Circuit
* Spur
* Spurious Copper
* Non-Defective

---

## Dataset

* Source: Public PCB Defects Dataset (Kaggle)
* The dataset contains labeled images corresponding to multiple defect categories and non-defective samples
* The data is structured to support direct use in training, validation, and testing workflows

---

## Methodology

### Data Preprocessing

* Image resizing
* Normalization
* Data augmentation (e.g., rotation, flipping)

### Model Development

* Convolutional Neural Networks (CNN)
* Optional use of transfer learning architectures such as ResNet or VGG

### Training

* Model training on labeled data
* Validation using a separate validation dataset

### Evaluation

* Performance evaluation on unseen test data using standard metrics

---

## Evaluation Metrics

The model performance is assessed using the following metrics:

* Accuracy
* Precision
* Recall
* F1-score

---

## Expected Outcomes

* A trained deep learning model capable of accurately classifying PCB defects
* Consistent performance across all defect categories
* A reproducible and scalable machine learning pipeline

---

## Technology Stack

* Python
* PyTorch or TensorFlow
* OpenCV
* NumPy
* Pandas
* Matplotlib

---

## Project Structure

```bash
├── data/                # Dataset files
├── models/              # Trained model files
├── notebooks/           # Jupyter notebooks
├── src/                 # Source code
├── results/             # Evaluation outputs and metrics
├── README.md
```

---

## Team

* Member 1
* Member 2
* Member 3

---

## Future Work

* Development of a real-time PCB defect detection system
* Deployment as a web-based application
* Integration with industrial inspection systems

---

## License

This project is intended for academic and research purposes.
