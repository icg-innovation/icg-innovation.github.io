---
layout: project
title: Road Detection EODT
display: true
featured: true
featured_order: 2
summary: Detecting roads from satellite imagery using state-of-the-art computer vision models.
github: https://github.com/icg-rse/new-simulation-tool
paper: https://road_paper.com
funding: Supported by Arthur Tolley
grant: https://grant.com
image: /assets/images/projects/road_detection/detection.png
tags: [python, machine learning, computer vision]
authors: ["Arthur Tolley"]
funders: [esa]
collaborators: [helyx]
---

## Overview

This project focuses on the automated detection and segmentation of road networks from high-resolution satellite imagery. By leveraging state-of-the-art deep learning models, specifically Convolutional Neural Networks (CNNs), we aim to create accurate and up-to-date road maps. This technology has critical applications in urban planning, disaster response, autonomous navigation, and infrastructure monitoring.

## Key Features

- **High-Resolution Segmentation**: Utilizes advanced models like U-Net to produce precise road masks.
- **Scalable Processing**: A robust pipeline for pre-processing and tiling large satellite images for efficient analysis.
- **Vectorization**: Post-processing techniques to convert pixel-based masks into clean, usable road network vector data (e.g., GeoJSON).
- **Performance Evaluation**: Includes modules to calculate key performance metrics like Intersection over Union (IoU).

## Technology Stack

- **Core Language**: Python
- **Deep Learning Framework**: PyTorch
- **Geospatial Libraries**: GeoPandas, Rasterio
- **Computer Vision**: OpenCV
- **Data Handling**: NumPy, Pandas
