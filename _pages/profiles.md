---
layout: page
title: people
permalink: /people/
title: people
description: members of the lab
nav: true
nav_order: 7

categories: [Prof, PostDoc, PhD, MSE, Undergrad, Visiting]

---

<div>
<div class="projects">
{% for category in page.categories %}

  <a id="{{ category }}" href=".#{{ category }}">
    <h2>{{ category }}</h2>
  </a>

  {% assign categorized_people = site.people | where: "category", category | where: "current", true %}
  {% assign sorted_people = categorized_people | sort: "year" %}
  <div class="grid">
  {% for person in sorted_people %}
    {% include person.liquid %}
  {% endfor %}
  </div>

  <hr>

  
{% endfor %}
</div>

{% assign alumni = site.people | where: "current", false %}
{% assign sorted_alumni = alumni | sort: "year" %}
<div class="projects">
  <a id="alumni" href=".#alumni">
      <h2>Alumni</h2>
  </a>
  <div class="container">
    {% for person in sorted_alumni %}
      {% include person.liquid %}
    {% endfor %}
  </div>
</div>

</div>