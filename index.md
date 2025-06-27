---
layout: default
title: Research Software Engineering @ ICG
---

## Welcome to ICG Research Software Engineering!

We are the Research Software Engineering team at the Institute of Cosmology and Gravitation (ICG), University of Portsmouth. We develop cutting-edge software solutions to support cosmological and astrophysical research.

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

## Featured Projects

<div class="projects-grid">
{% for project in site.projects limit:3 %}
  <div class="project-tile">
    <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
    <p>{{ project.summary }}</p>
    <div class="project-links">
      {% if project.github %}
        <a href="{{ project.github }}" class="btn btn-sm">GitHub</a>
      {% endif %}
      {% if project.paper %}
        <a href="{{ project.paper }}" class="btn btn-sm">Paper</a>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

[View all projects →](/projects/)

## Funders & Collaborators

<div class="partners-section">
  <h3>Our work is supported by:</h3>
  <div class="partners-grid">
    <!-- Funders will be added here -->
    <p>UKRI, STFC, European Research Council, and more...</p>
  </div>
  
  <h3>We collaborate with:</h3>
  <div class="partners-grid">
    <!-- Collaborators will be added here -->
    <p>Leading research institutions worldwide in cosmology and astrophysics</p>
  </div>
</div>

[Learn more about our partnerships →](/funding/)

## Get in Touch

Interested in collaborating or learning more about our work? [Contact us](/about/) or explore our [GitHub repositories](https://github.com/icg-innovation).