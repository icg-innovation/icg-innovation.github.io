---
layout: project
title: EODT4Crises - Road Detection from Satellite Imagery
display: true
completed: true
featured: true
featured_order: 1
summary: Interactive web application for detecting roads from satellite imagery using computer vision with satellite data integration.
github: https://github.com/icg-innovation/EODT4Crises
paper:
funding: [Supported by ESA][https://business.esa.int/projects/eodt4crises]
grant:
image: /assets/images/projects/road_detection/eodt4crises_logo.jpg
tags: [python, javascript, machine learning, computer vision, web application]
authors: ["Arthur Tolley", "Becky Canning"]
funders: [esa]
collaborators: [helyx]
carousel_images:
  - "/assets/images/projects/road_detection/example_1.png"
  - "/assets/images/projects/road_detection/example_2.png"
  - "/assets/images/projects/road_detection/example_3.png"
  - "/assets/images/projects/road_detection/example_4.png"
  - "/assets/images/projects/road_detection/example_5.png"
---

## Overview

EODT4Crises is a comprehensive web-based platform for automated road detection and mapping from satellite imagery. Built in partnership with Helyx and funded by ESA, this tool combines state-of-the-art machine learning with an intuitive web interface to enable rapid road network extraction from multiple satellite data sources. The platform features an interactive Leaflet.js-based frontend with a Python backend, supporting real-time analysis and visualization of road infrastructure for applications in crisis response, and infrastructure monitoring.

<div id="road-detection-carousel"></div>

<script src="/assets/js/carousel.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  const roadDetectionImages = [
    { 
      src: '/assets/images/projects/road_detection/example_1.png', 
      alt: 'Road detection example showing satellite imagery and detected road network' 
    },
    { 
      src: '/assets/images/projects/road_detection/example_2.png', 
      alt: 'Road detection interface and visualization' 
    },
    { 
      src: '/assets/images/projects/road_detection/example_3.png', 
      alt: 'Satellite imagery analysis results' 
    },
    { 
      src: '/assets/images/projects/road_detection/example_4.png', 
      alt: 'Road network extraction example' 
    },
    { 
      src: '/assets/images/projects/road_detection/example_5.png', 
      alt: 'EODT4Crises application interface' 
    }
  ];
  
  new ImageCarousel('road-detection-carousel', roadDetectionImages, {
    width: '800px',
    height: '800px',
    caption: 'Road detection application imagery and results',
    autoPlay: false,
    showDots: true,
    showArrows: true
  });
});
</script>

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
