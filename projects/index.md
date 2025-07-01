---
layout: default
title: Projects
---

# Projects

Explore our research software projects supporting cosmology and astrophysics research.

<div class="projects-grid">
{% assign display_projects = site.projects | where_exp: "item", "item.display != false" %}
{% for project in display_projects %}
  {% include project_tile.html %}
{% endfor %}
</div>

{% if site.projects.size == 0 %}
<p>Projects coming soon! We're currently documenting our research software.</p>
{% endif %}