---
layout: default
submenu: [["download", "/resume.pdf"]]
title: Facundo Olano
head_title: Resume
---

I'm a software engineer from Buenos Aires, Argentina, with over 15 years of experience in the industry.
During the first part of my career, I worked as a Python and Django web developer while completing my Software Engineering degree.
Later, I specialized in backend development, service-oriented architectures, and distributed systems, using various technologies and programming languages (Python, Node.js, Clojure, Erlang, Rust).

Because I think that software development is primarily a human activity, I place a high value on communication and knowledge sharing. I try to bring a business perspective to software discussions and provide technical insight to non-engineers. I tend to assume a leadership role in the teams I integrate, leading by example and from experience rather than title.

More than technology or scale, my interest is in using simple tools to solve problems for users, working at organizations with healthy environments and sustainable business models.

### Contact

- [facundo.olano@gmail.com](mailto:facundo.olano@gmail.com)
- [GitHub](https://github.com/facundoolano)
- [LinkedIn](https://www.linkedin.com/in/facundoolano/)

### Education

**Software Engineering**, Universidad de Buenos Aires
  <br/> <small><span class="date">2006 - 2013</span></small>

### Experience

{% for job in site.data.work %}
{% if job.title %}<b>{{job.title}}</b>,{% endif %} {{job.org}}
  {% unless job.positions %}<br/>{% endunless %}<small><span class="date">{{job.date}}</span></small>

  {% for position in job.positions %}
  - {%if position.title %}<b>{{position.title}}</b>{% endif %}{%if position.org%}, {{position.org}} {% endif %}
    <br/><small><span class="date">{{position.date}}</span></small>
    <br/>{{ position.description }}<br/>{% assign techs = position.tech | split:"," %}

    {% if techs%}<small><span class="tags"> {% for tech in techs %}#{{tech | replace: " ", ""}} {% endfor %}</span></small>{%endif%}
    {% else %}
  {% endfor %}
  {{job.description }}

{% assign techs = job.tech | split:"," %}
{% if techs.size > 0 %}<small><span class="tags"> {% for tech in techs %}#{{tech | replace: " ", ""}} {% endfor %}</span></small>{%endif%}

{% unless forloop.last %}
---
{% endunless %}
{% endfor %}
