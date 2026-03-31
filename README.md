# Deep Learning-Based PCB Defect Detection and Classification

## Overview

This project presents an automated system for detecting and classifying defects in Printed Circuit Boards (PCBs) using image data. The primary approach leverages deep learning for robust and scalable defect detection, while an additional experimental pipeline explores classical image processing techniques.

Manual inspection of PCBs is time-consuming and prone to error. This project aims to improve inspection accuracy, efficiency, and consistency through automated methods.

---

## Problem Statement

The objective is to detect and classify PCB defects from images into multiple categories, including six defect types and a non-defective class, using a reliable and generalizable approach.

---

## Objectives

* Develop an automated PCB defect detection system
* Achieve high performance in terms of accuracy, precision, recall, and F1-score
* Build a reproducible data processing and training pipeline
* Evaluate and compare multiple approaches for defect detection

---

## Defect Classes

The system identifies the following defect types:

* Missing Hole
* Mouse Bite
* Open Circuit
* Short Circuit
* Spur
* Spurious Copper

---

## Dataset

* Public PCB Defects dataset (Kaggle)
* Contains labeled images with corresponding annotations
* Includes multiple defect classes and non-defective samples
* Used for training, validation, and testing

---

## Primary Approach: Deep Learning Pipeline

### Overview

The primary solution uses a YOLOv8-based object detection model to identify and localize PCB defects in images.

### Pipeline

1. **Dataset Preparation**

   * Organize images and annotation files
   * Parse Pascal VOC (XML) annotations

2. **Annotation Processing**

   * Extract bounding box and class information
   * Convert annotations to YOLO format

3. **Preprocessing**

   * Resize images to a fixed resolution (640×640)
   * Normalize and enhance images by converting it into grayscale and increase contrast

4. **Dataset Splitting**

   * Split data into training, validation, and testing sets

5. **Cross Validation**

   * Apply K-Fold cross validation for improved robustness

6. **Model Training**

   * Train YOLOv8 model on PCB defect dataset
   * Fine-tune pretrained weights

7. **Evaluation**

   * Evaluate using:

     * Accuracy
     * Precision
     * Recall
     * F1-score
     * Mean Average Precision (mAP)

8. **Inference**

   * Perform detection on unseen and custom PCB images

---

## Code Structure

* `exploring.py` – Dataset validation and structure analysis
* `annotations.py` – XML parsing and annotation extraction
* `visualization.py` – Bounding box visualization
* `preprocessing.py` – Image resizing and annotation scaling
* `split_data.py` – Dataset splitting and YOLO format conversion
* `kfold.py` – K-Fold dataset generation
* `training.py` – Cross-validation training pipeline
* `model.py` – Final model training
* `predict.py` – Inference and evaluation

---

## Alternative Approach: Rule-Based Image Processing (Experimental)

### Overview

An experimental pipeline was developed using classical image processing techniques to detect PCB defects based on domain-specific characteristics.

This approach does not rely on machine learning and instead uses geometric and intensity-based analysis.

### Missing Hole Detection

The implemented method focuses on detecting missing hole defects using the following approach:

* Convert images to grayscale and apply Gaussian filtering
* Detect circular pad structures using Hough Circle Transform
* Extract pixel intensity values from:

  * The pad region
  * The central region (expected hole location)
* Compare intensity differences:

  * A valid hole appears darker than the surrounding pad
  * If not, it is classified as a missing hole defect

Detected defects are highlighted with bounding boxes on the original image.

### Current Status

* Successfully implemented for Missing Hole detection
* Not extended to other defect classes

### Limitations

* Not scalable across all defect types
* Sensitive to image noise and variations
* Requires manual tuning of parameters

### Significance

* Provides interpretability and domain insight
* Demonstrates an alternative to data-driven methods
* Useful in scenarios with limited labeled data

---

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Mean Average Precision (mAP)

---

## Results

The deep learning model demonstrates strong performance in detecting and classifying multiple PCB defect types. The experimental pipeline shows promising results for missing hole detection using classical techniques.

---

## Technology Stack

* Python
* YOLOv8
* OpenCV
* NumPy
* Pandas
* Matplotlib

---

## Project Structure

```bash
├── data/                # Dataset
├── models/              # Trained models
├── notebooks/           # Experiments and analysis
├── src/                 # Source code
├── results/             # Outputs and evaluation metrics
├── README.md
```

---

## Future Work

* Extend rule-based pipeline to additional defect types
* Improve robustness under varying lighting conditions
* Deploy the system for real-time industrial inspection
* Develop a web-based or API-based interface

---

## Team

* Kritharth T
* Abhinav Shailesh Chavan
* Digvijay Singh Goil

---
