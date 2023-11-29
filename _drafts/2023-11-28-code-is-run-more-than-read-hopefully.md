---
layout: post
title: "Code is run more than read, code is used more than run"
date: 2023-11-28 07:19:01
tags: [software]
lang: en
---


## Code is read more than written

This phrase is by now common programmer knowledge<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>, a reminder that the person first writing a piece of code shouldn't buy convenience at the expense of the people that will have to read it and modify it. More generally, *code is read more than written* conveys the idea that it's usually a good mid and long-term investment to make the code maintainable, for example by writing tests and documentation, by keeping it simple, etc.

Let's express this more succinctly as:

<div class="org-center">
<p>
maintainer &gt; author
</p>
</div>

I think this model can be extended to software development beyond code-writing, and used as a rule of thumb when characterizing problems and making decisions.


## Code is used more than read

An obvious one: software has a purpose, it's supposed to provide a service to some user:

<div class="org-center">
<p>
user &gt; maintainer &gt; author
</p>
</div>

This has a lot of well-known implications:

-   it doesn't matter how well written or maintainable the code is, nor how sophisticated the technology, if it doesn't serve its purpose with a good user experience,
-   don't assume (or ask) what the user needs, put the program in front of the user as early and frequently as possible.

This is a strong mental model, it can get us pretty far. This is approximately how I learned the job and how I understood it for the first half of my career.


## Code is run more than read

When I say `run` I don't just mean executing a program, I mean operating it in production, with all that that entails: deploying, upgrading, observing, auditing, monitoring, fixing, decommissioning, etc.

<div class="org-center">
<p>
user &gt; operator &gt; maintainer &gt; author
</p>
</div>

This is something that took me a while to fully grasp because, at least in my experience and that of the people I know, most of the software being developed doesn't get to production, at least not at the expected scale. Most software is built on top of assumptions that never get tested.

<when you run software in production, the KISS mantra takes on a new dimension. It's not just about code, it's about architecture and infra, it's about reducing the moving parts and understanding their failure modes, it's about shipping stuff and making sure it works even while it breaks.


## Also, there's a business

the assumption was that something useful and with a good ux was going to have business value. this was about right for consumer and enterprise software.

but maybe not necessarily so much for most software today. what about costs and budgets? what about stakeholders, investors

<div class="org-center">
<p>
biz &gt; user &gt; operator &gt; maintainer &gt; author
</p>
</div>


## Smells

Software is all about trade-offs, about making choices, prioritizing, <maximizing the benefits to be attained with limited resources. We can use the previous model to identify common cases of misprioritizations or lack of perspective (a.k.a. *missing the big picture*). [[work on what matters](https://staffeng.com/guides/work-on-what-matters/) ?]


### Ignoring the maintainers

<div class="org-center">
<p>
<del>maintainer</del> &gt; author <br />
author &gt; maintainer
</p>
</div>

We know these, this is where we started. This is clever and lazy code that turns into spaghetti and haunted forests, this is unnecessary performance optimizations.


### Ignoring operations

<div class="org-center">
<p>
<del>operator</del> &gt; maintainer &gt; author
</p>
</div>

<Software that gets developed but it rarely (or never) gets to production. I call this *imaginary software*. Charity Major's calls it living a lie [LINK].


### Underestimating operations

<div class="org-center">
<p>
author &gt; operator
</p>
</div>

More commonly software does get deployed but it wasn't designed with its operation in mind. This overly complicated software with lots of moving parts, fancy databases for small data loads, small-team owned microservice ecosystems, etc.


### Ignoring the user

<div class="org-center">
<p>
biz &gt; <del>user</del> &gt; operator &gt; maintainer &gt; author
</p>
</div>

Perhaps another kind of imaginary software, the one that doesn't have users or even doesn't know what users could look like. But it scales.

this is also taking some cool new tech and hammering everything with it until <something resembling a <use case | user need | business model> materializes <below it


### Underestimating the user

<div class="org-center">
<p>
maintainer &gt; author &gt; user
</p>
</div>


### underestimating the business

<div class="org-center">
<p>
maintainer &gt; author &gt; biz
</p>
</div>


### Ignoring the business

<div class="org-center">
<p>
<del>biz</del> &gt; user &gt; operator &gt; maintainer &gt; author
</p>
</div>

<That's when you pretend the business, or that costs don't matter turning a profit, doesn't really matter that's how you get retrofitted business models (you know, spying on people for ads) and enshittified platforms the funny thing about late capitalism is that it's not only coders having this misconception. it's actually CEOs and (central banks?) everyone in between. But we software folk should know better


## The elephant

This one hits hard:

<div class="org-center">
<p>
biz &gt; user
</p>
</div>

<attention grabbing it's not only social media anymore, it's travel agencies, delivery apps, even the Windows start menu (!)

<div class="org-center">
<p>
{biz, user} &gt; operator &gt; maintainer &gt; author
</p>
</div>

<doubling down (?) on the ethical discipline. like doctors, that are supposed to put patients first regardless of the hospital needing to turn a profit

<section class="footnotes" markdown=1>
## Notas

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Granted, it can be taken too far. TODO graydon hoare recent take

</section>