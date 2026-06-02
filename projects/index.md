---
layout: default
title: Projects
---

# Projects

Explore our research and outreach projects.

{% assign display_projects = site.projects | where_exp: "item", "item.display != false" %}
{% assign active_projects = display_projects | where_exp: "item", "item.completed != true" %}
{% assign completed_projects = display_projects | where: "completed", true %}

## Current Projects

<div class="projects-grid">
{% for project in active_projects %}
  {% include project_tile.html %}
{% endfor %}
</div>

{% if completed_projects.size > 0 %}
## Completed Projects

<div class="projects-grid">
{% for project in completed_projects %}
  {% include project_tile.html %}
{% endfor %}
</div>
{% endif %}

{% if display_projects.size == 0 %}
<p>Projects coming soon! We're currently documenting our research software.</p>
{% endif %}