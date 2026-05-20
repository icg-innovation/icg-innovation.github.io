---
layout: default
title: About Us
---

## Our Teams

{% for team_data in site.data.team.teams %}
  {% assign team_key = team_data[0] %}
  {% assign team = team_data[1] %}
  
  <div class="team-section">
    <h3>{{ team.name }}</h3>
    <p class="team-description">{{ team.description }}</p>
    
    <div class="team-grid{% if team_key == 'previous' %} team-grid--previous{% endif %}">
    {% for member in team.members %}
      {% assign slug = member.slug %}
      <div class="team-member{% if team_key == 'previous' %} team-member--previous{% endif %}">
        {% if team_key == 'previous' %}
          <!-- Simple card for previous members: just name, role, and current position -->
          <h4>{{ member.name }}</h4>
          <p class="team-role">{{ member.role }}</p>
          {% if member.current_position and member.current_position != "" %}
            <p class="team-current-position">{{ member.current_position }}</p>
          {% endif %}
          <a href="/author/{{ slug }}/" class="team-member-link--stretched" aria-label="View projects for {{ member.name }}"></a>
        {% else %}
          <!-- Full card for current members -->
          {% if member.image %}
            <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
          {% else %}
            <div class="team-photo-placeholder"></div>
          {% endif %}
          <h4>{{ member.name }}</h4>
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
            {% if member.email and member.email != "" %}
              <a href="mailto:{{ member.email }}">Email</a>
            {% endif %}
            {% if member.pure_url and member.pure_url != "" %}
              <a href="{{ member.pure_url }}" target="_blank" rel="noopener noreferrer">Pure Profile</a>
            {% endif %}
            {% if member.orcid and member.orcid != "" %}
              <a href="https://orcid.org/{{ member.orcid }}" target="_blank" rel="noopener noreferrer">ORCID</a>
            {% endif %}
          </div>
          <a href="/author/{{ slug }}/" class="team-member-link--stretched" aria-label="View profile for {{ member.name }}"></a>
        {% endif %}
      </div>
    {% endfor %}
    </div>
  </div>
{% endfor %}

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
