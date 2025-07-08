---
layout: default
title: About Us
---

## Our Team

<div class="team-grid">
{% for member in site.data.team.members %}
  {% assign slug = member.slug %}
  <div class="team-member">
    {% if member.image %}
      <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
    {% else %}
      <div class="team-photo-placeholder"></div>
    {% endif %}
    <h3>{{ member.name }}</h3>
    <p class="team-role">{{ member.role }}</p>
        {% if member.research_interests and member.research_interests.size > 0 %}
          <div class="team-interests">
            {% for interest in member.research_interests %}
              <span class="tag">{{ interest }}</span>
            {% endfor %}
          </div>
    {% endif %}
    {% if member.bio %}
      <p class="team-bio">{{ member.bio }}</p>
    {% endif %}
    <div class="team-links">
      {% if member.email %}
        <a href="mailto:{{ member.email }}">Email</a>
      {% endif %}
      {% if member.pure_url %}
        <a href="{{ member.pure_url }}" target="_blank">Pure Profile</a>
      {% endif %}
      {% if member.orcid %}
        <a href="https://orcid.org/{{ member.orcid }}" target="_blank">ORCID</a>
      {% endif %}
    </div>
    <a href="/author/{{ slug }}/" class="team-member-link--stretched" aria-label="View profile for {{ member.name }}"></a>
  </div>
{% endfor %}
</div>

<div class="pure-integration-note">
  <p><em>Team profiles are integrated with the <a href="https://researchportal.port.ac.uk/">University of Portsmouth Pure Research Portal</a></em></p>
</div>

## What We Do

- **Research Software Engineers**:
- **Innovation Projects**:
- **Public Engagement and Outreach**:

## Contact Us

For collaborations, questions, or more information about our work:

RSEs Email: [icg-rse-group@port.ac.uk](mailto:icg-rse-group@port.ac.uk)

Innovation GitHub: [github.com/icg-innovation](https://github.com/icg-innovation)
