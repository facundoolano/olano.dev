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
<code>maintainer &gt; author</code>
</p>
</div>

I think this model can be extended to software development beyond code-writing, and used as a rule of thumb when characterizing problems and making decisions.


## Code is used more than read

An obvious but often forgotten one: software should have a purpose, it's supposed to provide a service to some user:

<div class="org-center">
<p>
<code>user &gt; maintainer &gt; author</code>
</p>
</div>

This has a lot of well-known implications:

-   it doesn't matter how well written or maintainable the code is, nor how sophisticated the technology, if it doesn't fulfill its purpose and provides a good user experience,
-   instead of guessing or asking what the user needs, it's best to put the program in front of them early and frequently.

This is a strong mental model, just keeping users in mind can get us pretty far. This is approximately how I learned the job and how I understood it for the first half of my career.

Before proceeding, let's group authors and maintainers, since the distinction won't be useful in broader contexts:

<div class="org-center">
<p>
<code>user &gt; dev</code>
</p>
</div>


## Code is run more than read

When I say `run` I don't just mean executing a program, I mean operating it in production, with all that that entails: deploying, upgrading, observing, auditing, monitoring, fixing, decommissioning, etc.

This is something that took me a while to fully grasp because, at least in my experience and that of the people I know, most of the software being developed doesn't never really gets to production, at least not at the expected scale. Most software is built on assumptions that never get tested.

<div class="org-center">
<p>
<code>user &gt; ops &gt; dev</code>
</p>
</div>

When you run software in production, the KISS mantra takes on a new dimension. It's not just about code anymore, it's a little bit about architecture and infra, but mostly about reducing the moving parts and understanding their failure modes. It's about shipping stuff and making sure it works even while it breaks. It's about using [boring tech](https://mcfunley.com/choose-boring-technology) in [radically simple](https://www.radicalsimpli.city/) ways.


## Also, there's a business

the assumption was that something useful and with a good ux was going to have business value. this was about right for consumer and enterprise software.

but maybe not necessarily so much for most software today. what about costs and budgets? what about stakeholders, investors

<div class="org-center">
<p>
<code>biz &gt; user &gt; ops &gt; dev</code>
</p>
</div>


## Smells

Software is all about trade-offs, about making choices, prioritizing, <maximizing the benefits to be attained with limited resources. We can use the previous model to identify common cases of misprioritizations or lack of perspective (a.k.a. *missing the big picture*).


### Ignoring maintainers

<div class="org-center">
<p>
<del><code>maintainer</code></del> <code>&gt; author</code> <br />
<code>author &gt; maintainer</code>
</p>
</div>

This is where we started. This is clever and lazy code that turns into spaghetti and haunted forests, this is unnecessary performance optimizations.


### Ignoring operations

<div class="org-center">
<p>
<del>ops</del> &gt; dev
</p>
</div>

<Software that gets developed but it rarely (or never) gets to production. I call this *imaginary software*. Charity Majors calls it living a lie [LINK].


### Underestimating operations

<div class="org-center">
<p>
dev &gt; ops
</p>
</div>

More commonly software does get deployed but it wasn't designed with its operation in mind. This it "works on my machine". This is overly complicated software with lots of moving parts, fancy databases for small data loads, small-team owned microservice ecosystems, etc. This is when the people that design the thing aren't the same that get woken up at night when it breaks.


### Ignoring users

<div class="org-center">
<p>
biz &gt; <del>user</del> &gt; ops &gt; dev
</p>
</div>

Perhaps a different kind of imaginary software, the one that doesn't have users or even doesn't know what users could look like. But it scales.

This is software that doesn't solve a problem or solves the wrong problem, even nobody's problem. This is also taking some cool tech and hammering everything with it until something resembling a use case comes up.


### Underestimating users

<div class="org-center">
<p>
biz &gt; ops &gt; dev &gt; user
</p>
</div>

software that has users but doesn't observe how they use it, or what they need

software that sacrifizes user experience

software that drops features when updating its UI


### Underestimating business

<div class="org-center">
<p>
dev &gt; biz
</p>
</div>


### Ignoring business

<div class="org-center">
<p>
<del>biz</del> &gt; user &gt; ops &gt; dev
</p>
</div>

<That's when you pretend the business, or that costs don't matter turning a profit, doesn't really matter that's how you get retrofitted business models (you know, spying on people for ads) and enshittified platforms the funny thing about late capitalism is that it's not only coders having this misconception. it's actually CEOs and (central banks?) everyone in between. But we software folk should know better


## An elephant

This one hits hard:

<div class="org-center">
<p>
biz &gt; user
</p>
</div>

<attention grabbing it's not only social media anymore, it's travel agencies, delivery apps, even the Windows start menu (!)

<div class="org-center">
<p>
{biz, user} &gt; ops &gt; dev
</p>
</div>

<doubling down (?) on the ethical discipline. like doctors, that are supposed to put patients first regardless of the hospital needing to turn a profit

<section class="footnotes" markdown=1>
## Notas

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Granted, it can be taken too far. TODO graydon hoare recent take

</section>