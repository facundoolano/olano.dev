---
layout: post
title: "Code is run more than read, code is used more than run"
date: 2023-11-28 07:19:01
tags: [software]
lang: en
---


## Code is read more than written

The phrase by is now common programmer knowledge<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>, a reminder that the person first writing a piece of code shouldn't buy convenience at the expense of the people that will have to read and modify it later. More generally, *code is read more than written* conveys the idea that it's usually a good mid and long-term investment to make the code maintainable, for example by writing tests and documentation, by keeping it simple, etc. It's about having perspective about the software development cycle.

Let's express this idea more succinctly as:

<div class="org-center">
<p>
<code>maintainer &gt; author</code>
</p>
</div>

I think this model can be extended to software development beyond code-writing, and used as a rule of thumb to identify problems and make decisions.


## Code is used more than read

An obvious but often forgotten one: software should have a purpose, it's supposed to provide a service to some user. It doesn't matter how well written or maintainable the code is, nor how sophisticated the technology it uses, if it doesn't fulfill its purpose and provides a good experience to the user. Instead of guessing or asking what users need, it's best to put the program in front of them early and frequently and to incorporate what we learn in the process:

<div class="org-center">
<p>
<code>user &gt; maintainer &gt; author</code>
</p>
</div>

Or, since we won't need to distinguish between developers anymore:

<div class="org-center">
<p>
<code>user &gt; dev</code>
</p>
</div>

This is a strong mental model, just keeping the users in mind during development can get us pretty far. This is approximately how I learned the job and how I understood it for the first half of my career.


## Code is run more than read

When I say `run` I don't just mean executing a program, I mean operating it in production, with all that that entails: deploying, upgrading, observing, auditing, monitoring, fixing, decommissioning, etc. As Dan McKinley puts it in [*Choose Boring Technology*](https://mcfunley.com/choose-boring-technology):

> It is basically always the case that the long-term costs of keeping a system working reliably vastly exceed any inconveniences you encounter while building it.

We can incorporate this idea to our little expression:

<div class="org-center">
<p>
<code>user &gt; ops &gt; dev</code>
</p>
</div>

This is something that took me a while to fully grasp because, in my experience, a lot of the software being built never really gets to production, at least not at a significant scale. Most software is built on assumptions that never get tested. When you do run software in production, the KISS mantra takes on a new dimension. It's not just about code anymore, it's a little bit about architecture and infra, but mostly about reducing the moving parts and understanding their failure modes. It's about shipping stuff and making sure it works even while it breaks.


## Follow the money

I said that keeping the users in mind during development can get us very far. This works under the assumption that software that's useful and works well, software of value to users, will bring money to the business. It's a convenient abstraction for developers: we do a good job so we don't need to worry about the business details. And it mostly works, especially for consumer and enterprise software.

But at some point that abstraction proves to be an oversimplification, and we can benefit from incorporating a business perspective:

<div class="org-center">
<p>
<code>biz &gt; user &gt; ops &gt; dev</code>
</p>
</div>

The most obvious example is budget: we don't have infinite resources to satisfy the user needs, we need to measure costs and benefits. There's marketing, there's deadlines. There are stakeholders and investors. There's personal interests and politics at play. Sometimes we'll have to work on what generates revenue, not what pleases the user. More on this later.


## Smells

We arrived at a little model that expresses the relative importance of factors involved in <software development>, one that can perhaps help us to see the big-picture. Now I want to look at some common software development dysfunctions, and check how they relate to the model.


### Ignoring or underestimating maintainers

<div class="org-center">
<p>
<del><code>maintainer</code></del> <code>&gt; author</code> <br />
<code>author &gt; maintainer</code>
</p>
</div>

This is where we started. This is clever and lazy code that turns into spaghetti and haunted forests, this is premature optimizations, this is only-fred-touches-that-module.


### Ignoring operations

<div class="org-center">
<p>
<del>ops</del> &gt; dev
</p>
</div>

This is software that's built but rarely (or never) gets to production. I call this *imaginary software*. Charity Majors [calls it](https://twitter.com/mipsytipsy/status/1308641574448803840?lang=es) living a lie.


### Underestimating operations

<div class="org-center">
<p>
dev &gt; ops
</p>
</div>

More frequently, software does get deployed but it wasn't designed with operating it as a priority. This is overly complicated software with lots of moving parts, fancy databases for small data loads, small-team-owned microservice ecosystems. This is "works on my machine". This is when the people that design the thing aren't the same that get woken up at night when it breaks.


### Ignoring users

<div class="org-center">
<p>
biz &gt; <del>user</del> &gt; ops &gt; dev
</p>
</div>

Perhaps a different kind of imaginary software, the one that doesn't have users or even doesn't know what users could look like. (But scales). This is software that doesn't solve a problem or solves the wrong problem, even nobody's problem. This is taking some cool tech and hammering everything with it until something resembling a use case comes up.


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