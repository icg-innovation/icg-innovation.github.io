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
  {% assign featured_funders = site.data.funders | where: "featured", true %}
  {% assign featured_collaborators = site.data.collaborators | where: "featured", true %}
  {% assign featured_partners = featured_funders | concat: featured_collaborators %}
  {% for partner in featured_partners %}
    <a href="{{ partner.url }}" class="logo-item" target="_blank" rel="noopener noreferrer" title="{{ partner.name }}">
      <img src="{{ partner.logo | relative_url }}" alt="{{ partner.name }} Logo">
    </a>
  {% endfor %}
</div>

[Learn more about our partnerships →](/funding/)

## Get in Touch

Interested in collaborating or learning more about our work? [Contact us](/about/) or explore our [GitHub repositories](https://github.com/icg-innovation).