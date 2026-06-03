---
layout: project
title: Zooniverse Panoptes Aggregation
display: true
featured: false
featured_order:
summary: A general purpose toolbox for analyzing the data from a Zooniverse citizen science project
github: https://github.com/zooniverse/aggregation-for-caesar
paper: https://zenodo.org/records/18863801
funding:
grant:
image:
tags: [Python, Data Science, Citizen Science]
authors: ["Coleman Krawczyk", "Molly Burkmar", "Joe Jackson"]
funders: []
collaborators: [uop, zooniverse, oxford, adler, minnesota]
---

## Overview

The Zooniverse is the world’s leading citizen science platform, connecting researchers with more than 2.8 million volunteers to enable data classification and analysis across disciplines from astrophysics to the humanities. Since 2009, the Zooniverse has hosted over 500 projects from hundreds of researchers around the world.

Zooniverse projects require multi-user classification to produce research-quality data, meaning that once volunteers have processed project data, research teams must engage in reconciliation methods to determine consensus results. Panoptes Aggregation is a general-purpose Python data processing toolbox that can be used with any Zooniverse project, first released in 2017.

## Key Features

- Auto configuration: Can read in you Zooniverse project's workflow export and produce the needed configuration files with reasonable defaults
- Consensus calculation: Can read in your Zooniverse project's classification export and create csv files with the consensus results for each subject on the project
- Offline processing: Panoptes Aggregation can be run either locally using python, the command line interface, or the GUI.  Standalone installers are provided for Windows and Mac.
- Real-time processing: Panoptes Aggregation can be used with the Zooniverse's real-time data processing system called Caesar.  This can alow the consensus values to be monitored in real-time and trigger various events such as early retirement.
- Documentation available: [full documentation available](https://aggregation-caesar.zooniverse.org/docs)
- Use to power our text transcription project data analysis tool [ALI/CE](https://alice.zooniverse.org/)

## Technology Stack

- Python 3.9+
- Flask
- Docker
- unittests
