---
layout: default
title: Facundo Olano
sections: [["mailto:facundo.olano@gmail.com", "@gmail"], ["https://www.linkedin.com/in/facundoolano/", "@linkedin"], ["/work/resume.pdf", "resume.pdf"]]
---

I'm a software engineer from Buenos Aires, Argentina, with over 15 years of experience in the industry.
During the first part of my career, I worked as a Python and Django web developer while completing my Software Engineering degree.
Later, I specialized in backend development, service-oriented architectures, and distributed systems, using various technologies and programming languages (Python, Node.js, Clojure, Erlang, Rust).

Because I think that software development is primarily a human activity, I place a high value on communication and knowledge sharing. I try to bring a business perspective to software discussions and provide technical insight to non-engineers. I tend to assume a leadership role in the teams I integrate, leading by example and from experience rather than title.

More than technology or scale, my interest is in using simple tools to solve problems for users, working at organizations with healthy environments and sustainable business models.

I currently write on [my blog](/blog) and maintain many [open-source projects](/projects).

<br/>
### Education

**Software Engineering**, Universidad de Buenos Aires
  <br/> <small><span class="date">2006 - 2013</span></small>

<br/>
### Experience

{% for job in site.data.work %}
{% assign techs = job.tech | split:"," %}
<b>{{job.title}}</b>, {{job.org}}
  <br/> <small><span class="date">{{job.date}}</span></small>

  {{job.description }}

  <small><span class="date"> {% for tech in techs %}#{{tech | replace: " ", ""}} {% endfor %}</span></small>

{% unless forloop.last %}
---
{% endunless %}

{% endfor %}


<br/>
