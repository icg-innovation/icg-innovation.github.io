---
layout: default
title: Blog
---

# Blog

Stay updated with the latest news, tutorials, and insights from the ICG Research Software Engineering team.

<div class="blog-list">
{% for post in site.posts %}
  <article class="blog-entry">
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="post-meta">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      {% if post.author %} • {{ post.author }}{% endif %}
      {% if post.categories %} • {{ post.categories | join: ", " }}{% endif %}
    </p>
    <p>{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
    <a href="{{ post.url | relative_url }}" class="read-more">Read more →</a>
  </article>
{% endfor %}
</div>

{% if site.posts.size == 0 %}
<p>No blog posts yet. Check back soon!</p>
{% endif %}