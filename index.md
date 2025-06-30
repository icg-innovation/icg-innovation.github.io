---
layout: default
title: Research Software Engineering @ ICG
---

## Welcome to ICG Research Software Engineering!

We are the Research Software Engineering team at the Institute of Cosmology and Gravitation (ICG), University of Portsmouth. We develop cutting-edge software solutions to support cosmological and astrophysical research.

## Featured Projects

<div class="projects-grid">
{% assign featured_projects = site.projects | where: "featured", true | sort: "featured_order" %}
{% for project in featured_projects limit:4 %}
  {% include project_tile.html %}
{% endfor %}
</div>

[View all projects →](/projects/)

## Latest Blog Posts

<div class="blog-preview">
{% for post in site.posts limit:3 %}
  <article class="blog-item">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
    <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
  </article>
{% endfor %}
</div>

[View all blog posts →](/blog/)

## Funders & Collaborators

<p>Our work is made possible through the support of leading funding agencies and collaborations with world-class institutions.</p>

<div class="logo-grid logo-grid--home">
  <a href="https://www.ukri.org/" class="logo-item" target="_blank" rel="noopener noreferrer" title="UK Research and Innovation">
    <img src="/assets/images/logos/ukri_logo.png" alt="UKRI Logo">
  </a>
  <a href="https://stfc.ukri.org/" class="logo-item" target="_blank" rel="noopener noreferrer" title="Science and Technology Facilities Council">
    <img src="/assets/images/logos/stfc_logo.png" alt="STFC Logo">
  </a>
  <a href="https://erc.europa.eu/" class="logo-item" target="_blank" rel="noopener noreferrer" title="European Research Council">
    <img src="/assets/images/logos/erc_logo.png" alt="European Research Council Logo">
  </a>
  <a href="https://www.port.ac.uk/" class="logo-item" target="_blank" rel="noopener noreferrer" title="University of Portsmouth">
    <img src="/assets/images/logos/uop_logo.png" alt="University of Portsmouth Logo">
  </a>
  <!-- Add or remove logos as needed for the homepage -->
</div>

[Learn more about our partnerships →](/funding/)

## Get in Touch

Interested in collaborating or learning more about our work? [Contact us](/about/) or explore our [GitHub repositories](https://github.com/icg-innovation).