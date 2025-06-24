---
layout: project
title: "VobChat"
summary: "A conversational AI dashboard for exploring historical and statistical data through natural language interaction"
github: "https://github.com/icg-innovation/vobchat"
tags: [python, ai, dash, postgresql, langchain, geospatial]
---

## Overview

VobChat is a conversational AI dashboard that enables users to explore historical and statistical data through natural language interaction. It combines a chat interface with interactive maps and visualizations, allowing users to query geographic and statistical data from the Vision of Britain database using natural language.

## Key Features

- **Natural Language Interface**: Query complex geospatial and statistical data using conversational AI
- **Interactive Maps**: Real-time geographic visualization with Leaflet integration
- **Dynamic Visualizations**: Plotly-based charts that respond to conversational queries
- **Workflow Engine**: LangGraph-based conversational workflow management
- **Real-time Updates**: Server-Sent Events (SSE) for live workflow feedback
- **State Persistence**: Redis-based checkpointing for conversation continuity

## Technology Stack

### Core Components
- **Frontend**: Plotly Dash with Bootstrap components
- **Workflow Engine**: LangGraph for conversational workflow management
- **LLM Integration**: Ollama (DeepSeek-R1) for intent extraction
- **Database**: PostgreSQL with PostGIS for geospatial data
- **Real-time Communication**: Server-Sent Events (SSE)
- **State Management**: Redis-based checkpointing

### Architecture Highlights

- **Intent-Based Routing**: User inputs are processed by LLM for intent extraction and classified into predefined categories
- **Node-based Processing**: Each intent maps to specific workflow nodes
- **Multi-step Data Collection**: Supports complex queries involving place selection, theme selection, and data visualization
- **State Synchronization**: Maintains synchronized state across workflow, frontend, map, and visualization components

## Workflow System

The application uses a sophisticated workflow system with:
- Centralized state management using TypedDict
- Enum-based intent classification (AddPlace, RemovePlace, AddTheme, etc.)
- Redis-based state persistence for crash recovery
- Interrupt handling for user interactions

## Use Cases

- Historical data exploration
- Geographic statistical analysis
- Time-series data visualization
- Interactive research tool for Vision of Britain database
- Educational tool for historical geography

## Development

The project demonstrates advanced patterns in:
- Conversational AI integration
- Real-time web applications
- Geospatial data processing
- Complex state management
- Microservices architecture