---
layout: project
title: UoP Covid Track and Trace
display: true
completed: true
featured: false
featured_order:
summary: A custom database to store UoP student and staff covid test results
github:
paper:
funding:
grant:
image:
tags: [Database, Python, Data Science]
authors: ["Coleman Krawczyk", "Jascha Schewtschenko", "Max Foxley-Marrable", "Elizabeth Swann", "Michal Gnacik"]
funders:
collaborators: [uop]
---

## Overview

During the covid-19 lock down UoP ran on-campus testing centers to monitor the spread of the virus on campus.  After testing people were given to choice to opt-in to having there data stored in a custom database that was used to identify any "hot spots" on campus.  Daily reports were generated and send to the university executive board so they could make informed decisions in response to the virus.

## Key Features

- Custom database to store test results in compliance with all data safety regulations
- Ability to cross match students who were living on campus to identify if any students halls needed additional testing
- Address mapping for students or staff not living on campus
- A summary statists page that was emailed to the university executive board each day
- Daily database backups created
- Automatic integration with Google Forms for data insertion

## Technology Stack

List the main technologies, programming languages, frameworks, and tools used:

- Python 3.8
- Flask
- Leaflet
- Dash
- PostgreSQL
- Docker
