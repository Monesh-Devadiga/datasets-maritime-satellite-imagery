# Satellite Imagery Dataset

This directory contains references and dataset documentation for satellite imagery used in the Smart Maritime Surveillance and Safety System.

## Dataset Overview
The project uses two publicly available Kaggle datasets for maritime vessel detection and classification.

Source:
https://www.kaggle.com

### 1. Vessels in Aerial Images
Purpose:
* Ship and vessel detection
* YOLO-based object detection
* Bounding-box annotation

The dataset contains labeled RGB aerial and satellite images with vessel bounding-box annotations.
<!--Source:
https://www.kaggle.com/datasets/siddharthkumarshah/ships-in-aerial-images-->

### 2. Satellite Imagery of Ships
Purpose:
* Ship and non-ship binary classification
* CNN-based image classification
* Model training and evaluation

The dataset contains 4,292 labeled RGB satellite images, including 1,022 ship images for binary classification.

<!--Source:
https://www.kaggle.com/datasets/apollo2506/satellite-imagery-of-ships-->

## Dataset Statistics

| Dataset                    | Purpose                      | Images |
| -------------------------- | ---------------------------- | -----: |
| Vessels in Aerial Images   | Vessel detection             |  4,922 |
| Satellite Imagery of Ships | Ship classification          |  4,292 |
| Combined datasets          | Detection and classification | 6,473* |

* The combined count follows the dataset description used in the project research documentation. The two datasets contain overlapping image sources or subsets, so their raw image counts should not be treated as a simple sum.

## Applications
The datasets support the following components of the project:
* Vessel detection using YOLO
* Ship and non-ship classification using CNN models
* Satellite image preprocessing
* Maritime surveillance
* Vessel identification from aerial imagery
* Deep learning model evaluation

## Recommended Directory Structure

```text
    ├── box-marked-img
    ├── no ship-water
    └── ships
        └── README.md
```

The original datasets are hosted on Kaggle. Store dataset files locally or through the approved dataset download method rather than committing large raw datasets to GitHub.

## Dataset Sources

* Vessels in Aerial Images with YOLO Bounding-Box Annotations
* Satellite Imagery of Ships

Both datasets are publicly available through Kaggle. Refer to the original dataset pages for licensing, attribution and usage conditions.

<!-- ## Citation
If you use these datasets in research or publications, cite the original Kaggle dataset authors and follow their stated licensing requirements. -->
---------------------------------------------------------------------------------------------------------------------
Created By: 
  [@Monesh Devadiga](https://github.com/Monesh-Devadiga)
