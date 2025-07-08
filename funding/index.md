---
layout: default
title: Funding & Collaborators
---

# Funding Sources & Collaborators

## Our Funders

Innovation at the ICG is supported by various funding bodies.

<div class="logo-grid">
  {% for funder in site.data.funders %}
    <a href="{{ funder.url }}" class="logo-item" target="_blank" rel="noopener noreferrer" title="{{ funder.name }}">
      <img src="{{ funder.logo | relative_url }}" alt="{{ funder.name }} Logo">
    </a>
  {% endfor %}
</div>

## Collaborating Institutions

We collaborate with organisations worldwide.

<div class="logo-grid">
  {% for collaborator in site.data.collaborators %}
    <a href="{{ collaborator.url }}" class="logo-item" target="_blank" rel="noopener noreferrer" title="{{ collaborator.name }}">
      <img src="{{ collaborator.logo | relative_url }}" alt="{{ collaborator.name }} Logo">
    </a>
  {% endfor %}
</div>

## Get Involved

Interested in collaborating with us? Please [contact us](/about/) to discuss potential partnerships.