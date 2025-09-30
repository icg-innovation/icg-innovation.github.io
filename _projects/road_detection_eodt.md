---
layout: project
title: EODT4Crises - Road Detection from Satellite Imagery
display: true
featured: true
featured_order: 2
summary: Interactive web application for detecting roads from satellite imagery using computer vision with satellite data integration.
github: https://github.com/icg-innovation/EODT4Crises
paper:
funding: Supported by ESA
grant:
image: /assets/images/projects/road_detection/eodt4crises_logo.jpg
tags: [python, javascript, machine learning, computer vision, web application]
authors: ["Arthur Tolley", "Becky Canning"]
funders: [esa]
collaborators: [helyx]
---

## Overview

EODT4Crises is a comprehensive web-based platform for automated road detection and mapping from satellite imagery. Built in partnership with Helyx and funded by ESA, this tool combines state-of-the-art machine learning with an intuitive web interface to enable rapid road network extraction from multiple satellite data sources. The platform features an interactive Leaflet.js-based frontend with a Python backend, supporting real-time analysis and visualization of road infrastructure for applications in crisis response, and infrastructure monitoring.

<div class="image-carousel" style="position: relative; width: 800px; height: 800px; margin: 2rem auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <div class="carousel-container" style="position: relative; width: 100%; height: 100%; overflow: hidden;">
    <div class="carousel-slide active" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 1; transition: opacity 0.5s ease-in-out;">
      <img src="/assets/images/projects/road_detection/example_1.png" alt="Road detection example showing satellite imagery and detected road network" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <div class="carousel-slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.5s ease-in-out;">
      <img src="/assets/images/projects/road_detection/example_2.png" alt="EODT4Crises project logo" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <div class="carousel-slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.5s ease-in-out;">
      <img src="/assets/images/projects/road_detection/example_3.png" alt="EODT4Crises project logo" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <div class="carousel-slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.5s ease-in-out;">
      <img src="/assets/images/projects/road_detection/example_4.png" alt="EODT4Crises project logo" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <div class="carousel-slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.5s ease-in-out;">
      <img src="/assets/images/projects/road_detection/example_5.png" alt="EODT4Crises project logo" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
  </div>

  <!-- Navigation arrows -->
  <button class="carousel-prev" onclick="changeSlide(-1)" style="position: absolute; top: 50%; left: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">‹</button>
  <button class="carousel-next" onclick="changeSlide(1)" style="position: absolute; top: 50%; right: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">›</button>

  <!-- Dots indicator -->
  <div class="carousel-dots" style="position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 10;">
    <span class="dot active" onclick="currentSlide(1)" style="width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.8); cursor: pointer; transition: background 0.3s;"></span>
    <span class="dot" onclick="currentSlide(2)" style="width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer; transition: background 0.3s;"></span>
  </div>
</div>

<figcaption style="text-align: center; margin-top: 0.5rem; font-style: italic; color: #666; font-size: 0.9em;">Road detection application imagery and results</figcaption>

<script>
let slideIndex = 1;

function changeSlide(n) {
  showSlide(slideIndex += n);
}

function currentSlide(n) {
  showSlide(slideIndex = n);
}

function showSlide(n) {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.dot');

  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }

  slides.forEach(slide => slide.style.opacity = '0');
  dots.forEach(dot => dot.classList.remove('active'));

  if (slides[slideIndex - 1]) {
    slides[slideIndex - 1].style.opacity = '1';
  }
  if (dots[slideIndex - 1]) {
    dots[slideIndex - 1].style.background = 'rgba(255,255,255,0.8)';
  }

  // Update non-active dots
  dots.forEach((dot, index) => {
    if (index !== slideIndex - 1) {
      dot.style.background = 'rgba(255,255,255,0.4)';
    }
  });
}

// Hover effects
document.querySelectorAll('.carousel-prev, .carousel-next').forEach(btn => {
  btn.addEventListener('mouseenter', () => {
    btn.style.background = 'rgba(0,0,0,0.7)';
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.background = 'rgba(0,0,0,0.5)';
  });
});

document.querySelectorAll('.dot').forEach(dot => {
  dot.addEventListener('mouseenter', () => {
    if (!dot.classList.contains('active')) {
      dot.style.background = 'rgba(255,255,255,0.6)';
    }
  });
  dot.addEventListener('mouseleave', () => {
    if (!dot.classList.contains('active')) {
      dot.style.background = 'rgba(255,255,255,0.4)';
    }
  });
});
</script>

<style>
.image-carousel .carousel-prev:hover,
.image-carousel .carousel-next:hover {
  background: rgba(0,0,0,0.7) !important;
}

.image-carousel .dot:hover {
  background: rgba(255,255,255,0.6) !important;
}

.image-carousel .dot.active {
  background: rgba(255,255,255,0.8) !important;
}
</style>

## Key Features

### Interactive Web Interface
- **Leaflet.js-based Map**: Interactive web mapping interface with smooth pan, zoom, and layer management
- **Real-time Road Detection**: On-demand road extraction using the SAM_road model directly in the browser
- **OpenStreetMap Integration**: Overlay and compare detected roads with existing OSM road networks
- **Multi-layer Visualization**: Toggle between different data layers and analysis results

### Multi-Source Satellite Data Integration
- **Google Earth Engine (GEE)**: Access to Landsat, Sentinel, and other satellite archives
- **Maxar**: Access to sub-meter resolution satellite data for detailed analysis
- **Local File Upload**: Support for user-provided satellite imagery and GeoTIFF files

### Advanced Road Detection
- **SAM_road Model**: Leverages the Segment Anything Model adapted specifically for road detection
- **Automated Vectorization**: Converts detected road masks into clean vector geometries (GeoJSON, Shapefile)

## Technology Stack

### Frontend
- **Leaflet.js**: Interactive web mapping library for smooth map interactions
- **HTML/CSS/JavaScript**: Modern web technologies for responsive user interface

### Backend
- **Python**: Core processing engine for machine learning and geospatial operations
- **SAM_road**: Specialized road detection model based on Segment Anything Model
- **Flask/FastAPI**: Web framework for API endpoints and data processing

## Applications & Use Cases

### Crisis Response & Emergency Management
- **Rapid Assessment**: Quickly assess road network damage after natural disasters
- **Evacuation Planning**: Identify accessible routes for emergency response
- **Humanitarian Aid**: Support logistics planning for aid delivery

## Project Partnership

This project represents a successful collaboration between academic research and industry expertise:

- **Helyx**: Parallel development for mapping of power-network infrastructure.
- **European Space Agency (ESA)**: Funding and supporting the development of this Earth observation tool

The partnership leverages ESA's commitment to developing practical applications of satellite Earth observation data, combining cutting-edge AI research with real-world deployment challenges to create a tool that can make a meaningful impact in crisis response and infrastructure monitoring.
