---
layout: default
title: About Us
---

# About the ICG RSE Team

## What We Do

- **Software Development**: Creating robust, scalable software solutions for research projects
- **Data Analysis Tools**: Building tools for processing and analyzing large astronomical datasets
- **High-Performance Computing**: Optimizing code for HPC environments and parallel computing
- **Machine Learning**: Implementing ML techniques for astronomical data analysis
- **Visualization**: Developing tools to visualize complex cosmological data
- **Training & Support**: Providing software training and support to researchers

## Our Expertise

- Scientific Python (NumPy, SciPy, Astropy)
- High-performance languages (C++, Fortran, Julia)
- Parallel computing (MPI, OpenMP, CUDA)
- Machine learning frameworks
- Web technologies for data visualization
- Version control and collaborative development
- Software testing and continuous integration

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
    {% if member.research_interests %}
      <p class="team-interests">
        <strong>Research Interests:</strong> {{ member.research_interests | join: ", " }}
      </p>
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

## Join Our Team

We're always looking for talented software engineers and researchers who are passionate about applying their skills to advance our understanding of the universe. Check back for open positions or contact us to express your interest.

## Contact Us

For collaborations, questions, or more information about our work:

Email: [icg-rse-group@port.ac.uk](mailto:icg-rse-group@port.ac.uk)

GitHub: [github.com/icg-innovation](https://github.com/icg-innovation)