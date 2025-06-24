---
layout: default
title: Projects
---

# Projects

Explore our research software projects supporting cosmology and astrophysics research.

<div class="projects-container">
{% for project in site.projects %}
  <div class="project-card">
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    {% if project.image %}
      <img src="{{ project.image | relative_url }}" alt="{{ project.title }}" class="project-image">
    {% endif %}
    <p class="project-summary">{{ project.summary }}</p>
    <div class="project-details">
      {% if project.tags %}
        <div class="project-tags">
          {% for tag in project.tags %}
            <span class="tag">{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
      <div class="project-links">
        {% if project.github %}
          <a href="{{ project.github }}" class="btn">View on GitHub</a>
        {% endif %}
        {% if project.paper %}
          <a href="{{ project.paper }}" class="btn">Read Paper</a>
        {% endif %}
        {% if project.docs %}
          <a href="{{ project.docs }}" class="btn">Documentation</a>
        {% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>

{% if site.projects.size == 0 %}
<p>Projects coming soon! We're currently documenting our research software.</p>
{% endif %}