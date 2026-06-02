---
layout: project
title: Enhancing Maritime Safety
display: true
featured: true
featured_order: 3
summary: RSE support for an EPSRC maritime safety project using stereo imaging, wave reconstruction, and computer vision to support safer seakeeping decisions.
github: https://github.com/xangma/stereoocean
paper:
funding: Supported by EPSRC project EP/X035778/1
image: /assets/images/projects/enhancing-maritime-safety/example-render.png
grant: https://gtr.ukri.org/projects?ref=EP%2FX035778%2F1
article:
docs: https://stereoocean.github.io/
tags: [research software, computer vision, stereo imaging, wave reconstruction, maritime safety]
authors: ["Xan Morice-Atkinson", "Obinna Umeh"]
funders: [epsrc]
collaborators: [uop]
---

## Overview

The EPSRC-funded [Enhancing Maritime Safety](https://stereoocean.github.io/) project at the University of Portsmouth focuses on stereo imaging, 4D wave reconstruction, computer vision, and experimental validation to support safer seakeeping decisions for maritime operations.

Public outputs are being prepared as separate manuscripts.

## RSE Contribution

### Data pipeline

Enhancements and optimisations made to [Blender](https://github.com/xangma/blender/tree/ocean-lod-v5.1.1), including the development of level of detail (LOD) functionality for the Ocean Modifier. The creation of a custom [stereoocean data pipeline](https://github.com/xangma/stereoocean) for creating stereo images of the ocean surface from Blender simulations, which are then used for training and validating computer vision models.

![Example stereoocean render](/assets/images/projects/enhancing-maritime-safety/example-render.png)

*Example stereoocean render.*

### Computer vision model

Development of a computer vision model for disparity map prediction from stereo images. The model is trained and validated using the stereo images generated from Blender simulations.

## Links

### Information

- [Enhancing Maritime Safety project site](https://stereoocean.github.io/)
- [EPSRC project EP/X035778/1](https://gtr.ukri.org/projects?ref=EP%2FX035778%2F1)

### Software

- [Blender ocean LOD changes](https://github.com/xangma/blender/tree/ocean-lod-v5.1.1)
- [stereoocean data pipeline](https://github.com/xangma/stereoocean)

### Papers

In preparation, to be added when available.
