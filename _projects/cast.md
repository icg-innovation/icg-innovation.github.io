---
layout: project
title: "CAST: Competitive Angling as a Scientific Tool"
display: true
featured: false
featured_order:
summary: "Using citizen science data from sea angling competitions to inform fisheries management and develop AI-based fish species identification and length estimation."
github:
paper:
funding: "Funded by the UK Department for Environment, Food and Rural Affairs (DEFRA) under the Fisheries Industry Science Partnerships (FISP) scheme"
grant: https://www.gov.uk/government/publications/fisp-projects
image: /assets/images/logos/cast-logo.png
tags: [Python, Deep Learning, Computer Vision, Marine Science, Citizen Science]
authors: ["Obinna Umeh"]
funders: [defra]
collaborators: [uop]
---

## Overview

CAST ("Competitive Angling as a Scientific Tool") is a citizen science project that leverages data collected at recreational sea angling competitions to generate novel insights into data-poor fish species in the Solent. By partnering with the annual Sea Angling Classic competition, the project gathers morphological and ecological data on five target species:

- **Bass** (*Dicentrarchus labrax*)
- **Bream** (*Spondyliosoma cantharus*)
- **Skates & Rays** (*Raja* spp.)
- **Smoothhound** (*Mustelus* spp.)
- **Tope** (*Galeorhinus galeus*)

The project aims to provide fisheries managers with reliable, cost-effective data on the distribution, life stages, and habitat preferences of these species — data that is currently lacking and essential for sustainable fisheries management.

For more information, visit the [CAST project website](https://castproject.co.uk/).

## Computer Vision Work

A core component of the ICG-RSE contribution to CAST is the development of an automated computer vision system designed to reduce the time fish spend out of water during data collection — a key animal welfare consideration in catch-and-release angling.

### Species Classification

A deep neural network was trained on images collected by anglers at competition events to automatically classify fish into the target species categories. The model learns visual features including colouration, body shape, and morphological patterns to distinguish between species — a challenging task given the variability in image conditions (lighting, angle, background) in a field setting.

### Fish Length Estimation

Alongside classification, the system estimates the total body length of each fish directly from the angler-submitted photographs. Accurate length measurement is critical for assessing fish age and maturity, which are key inputs to stock assessment models.

### Goals

- Eliminate the need for manual identification and measurement at the point of capture
- Reduce handling time and associated stress on fish
- Enable scalable, standardised data collection that can be replicated at other angling events
- Provide a reusable AI pipeline with applications beyond the CAST project

## Technology Stack

- **Language**: Python
- **Framework**: Deep Learning (Convolutional Neural Networks)
- **Domain**: Computer Vision — image classification and regression (length estimation)
- **Data**: Angler-submitted photographs from sea angling competition events

## Funders & Partners

CAST is funded by DEFRA under the Fisheries Industry Science Partnerships (FISP) scheme (£569,361). The project is led by the University of Portsmouth in collaboration with the [Southern Inshore Fisheries and Conservation Authority (IFCA)](https://www.southern-ifca.gov.uk/) and [Angling Spirit](https://www.anglingspirit.com/), organiser of the Sea Angling Classic competition.
