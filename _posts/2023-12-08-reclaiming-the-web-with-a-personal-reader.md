---
layout: post
title: "Reclaiming the Web with a personal reader"
date: 2023-12-08
tags: [software, programación]
lang: en
---


## Background

Last year I experienced the all too common career burnout. I had a couple of bad projects in a row, yes, but more generally I became disillusioned with the software industry. There was a disconnection between what I used to like about the job, what I was good at, and what the software job market wanted to buy from me (given my experience, my location and the world economy).

I did the usual thing: I slowed down, quit my job, started therapy. I revised my habits: eat better, exercise, meditate. I tried to stay away from programming and software-related reading for a while. Because I didn't like the effect it had on me, but also encouraged by its apparent enshittification, I quit Twitter, the last social media outlet I was still plugged into.

Not working was one thing, but overcoming the productivity mandate &#x2014;the feeling that I had to make the best of my time off, that I was "recharging" to make a comeback&#x2014; was another. During this detox period I read *How to do Nothing*, a sort of artistic manifesto disguised as a self-help book that deals with some of these issues. The author Jenny Odell mentions Mastodon when discussing alternative online communities. I had heard about Mastodon, had seen some colleagues move over there, but never really looked at it. I thought it was a good time to try it.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

I noticed a few things after some weeks on Mastodon.

First, it felt refreshing to be back in control of my feed, to receive strictly chronological updates instead of having some algorithm tracking my moves in order to sell me stuff.

Second, not only wasn't I interested in micro-blogging myself, but I didn't care for most of the updates from the people I was following. I realized that I had been using Twitter, and now Mastodon, as an information hub rather than a social network. I was following bots to get updates from media and link aggregators; I was following people to get notified when they blogged. Mastodon wasn't the right tool for that job.

Third, there were many people going through a similar process as me, one of discomfort with the software industry and the state of the Web. Some of them were looking back at the old times for inspiration: playing with [RSS](https://atthis.link/blog/2021/rss.html), bulletin board systems, [digital gardens](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/) and Web rings; some imagined an [open](https://knightcolumbia.org/content/protocols-not-platforms-a-technological-approach-to-free-speech) and [independent](https://www.jvt.me/posts/2019/10/20/indieweb-talk/) Web of the future.

Things really clicked for me when I learned about the ideas of the IndieWeb, particularly the notion of [social readers](https://aaronparecki.com/2018/04/20/46/indieweb-reader-my-new-home-on-the-internet). Trying Mastodon had been nice, but what I needed to reconnect with the good side of the Web was a feed reader, one I could adjust arbitrarily to my preferences.

There are plenty of great RSS readers out there, and I did briefly try a few of them, but this was the perfect excuse for me to get back in touch with software development. I was going to build my own personal reader.


## Goals

**As a user**, I had some ideas of what I was trying to accomplish.

Rather than the email inbox metaphor I've most commonly seen used as RSS reader interfaces, I wanted something that felt like the Twitter or Mastodon home feed. That is: rather than [a backlog](https://danq.me/2023/07/29/rss-zero/) to clear every day, I wanted to get [a renewed stream](https://www.oliverburkeman.com/river) of interesting articles every time I opened the app. The feed would include articles from blogs, magazines, news sites and link aggregators, mixed with status updates and notifications from my Mastodon account (I eventually extended it to include my home feeds from Goodreads and Github). The parsing for those sources should be customizable to ensure a consistent look and feel, regardless of what I got back from their RSS feeds or their APIs.

Although I planned to ingest Mastodon updates and links from aggregator sites, I wasn't really interested in implementing a fully-fledged indie reader to react and comment to items within my app. I didn't really mind opening another tab to comment, nor that my "content" would then be scattered across different sites.

I also knew that I'd eventually need some sort of reader view, like the one in Firefox, to avoid jumping off the app to read, and to skip paywalls and annoying consent popups.

That's what I started with, but as soon as I had the most basic features in place, development would continue driven by *what felt right* and *what felt missing* as a user. My short-term goal was to answer, as soon as possible, this question: could this eventually become my primary (or sole) source of information in the Web? If not, I'd drop the project right away. Otherwise, I could move onto whatever was missing to realize that vision.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

**As a developer**, I wanted to test some of the ideas I'd been ruminating on for over a year. Although I hadn't yet formulated it in those terms, I wanted to apply what I expressed in [another post](../2023-11-30-code-is-run-more-than-read) as `user > ops > dev`. This meant that when prioritizing tasks or making design trade-offs, I would choose ease of operation (local setup, server deploys, software updates, etc.) over development convenience. And I would put user experience above everything else.

Since this was going to be an app for personal use and I had no intention on turning it into anything else, putting the user first meant dogfooding: <putting myself as a user, my needs, first>. Even if I wanted this to eventually be useful to other people, I presumed I had a better chance at achieving it by designing the app ergonomically for me than by aiming to satisfy some ideal user.

It was very important to me that this didn't turn into a learning project or, worse, a portfolio project. It wasn't about productivity, it was about reconnecting with the joy software development. While it was a leisure project, the pleasure shouldn't come from *building something* but from *using something I had built*.

Assuming me as the single target audience meant that I could postpone whatever I didn't need right away (e.g. user authentication), that I could tackle specialized features early (e.g. send to Kindle support ), that I could assume programming knowledge (e.g. leaving parser customization to code rather than implementing a complex generic interface or resigning myself to a generic implementation).


## Design

After settling on that first set of requirements, I needed to make some early technical decisions.


### User Interface

Although this was going to be a personal tool, and I wanted it to work on a local-first setup, I knew that if it worked well I'd want to access it from my phone (in addition to my laptop). This meant that I needed to make this a Web application:

-   Using the browser and HTML was the cost-effective way to implement a single client that worked in both devices.
-   HTML/CSS are the fronted tool I'm most familiar with.
-   Having a server would allow me to keep the state (e.g. the list of feeds) synchronized between devices.

I wanted the Web UI to be somewhat dynamic, but I definitely didn't want maintain a separate front-end application, learn a new front-end framework or reimplement what the browser already provided. Following the [boring tech](https://mcfunley.com/choose-boring-technology) and [radical simplicity](https://www.radicalsimpli.city/) advice, I looked into server-side rendering libraries. I ended up using a combination of [htmx](https://htmx.org/) and its companion [hyperscript](https://htmx.org/), which felt like picking up web development where I'd left off a decado ago, when I moved to the backend.


### Architecture

Simple operations meant that I wanted the app to be easy to deploy on linux environment but also easy to setup locally, with minimal infrastructure components, without requiring docker, etc.

A "proper" indie web reader, at least [as described by Aaron Parecki](https://aaronparecki.com/2018/03/12/17/building-an-indieweb-reader), is separated into multiple components, each implementing different protocols (micropub, microsub, webmention). This enforces the separation of concerns between content fetching, parsing, displaying and publishing. I felt that, for my use case, this architecture would complicate development and especially operations without buying me as a user. Since I was doing all development myself, I preferred to build a monolithic Web application.

Although I default to Postgres for most of my projects, the small scale of this one made it a perfect fit for sqlite, which had the benefit of simplifying database setup and operations.

Apart from serving the web application, I needed some way to periodically poll the feeds for content. The basic option would have been to set up a script run by cron, but that seemed inconvenient, particularly for non-server setups. I'd used task runners like celery in the past, but that would have required a couple of extra components: another service to run alongside the app and a data system (e.g. Redis) to act as a broker. Could I get away with running the background tasks in the same process as the web server? That largely depended on the concurrency support of the programming language I chose, which brings me to the next section.


### Programming language

At least from my superficial understanding of it, Go seemed like the best fit for this project: a simple general-purpose language, garbage-collected but fast enough, with a solid concurrency model and, most importantly for my requirements, one that produced easy to deploy binaries. The big problem is that I never wrote a line of Go, and while I understand it's easy to pick up, I didn't want to lose focus by turning this into a language learning project.

Among the languages I was already fluent with, I needed to chose the one I expected to be most productive with, the one that let me built a quick prototype to decide whether this looked like something worth pursuing. So I chose Python.

The bad side of using Python was that I had to deal with its environment and dependency quirks, particularly its reliance on the host OS libraries. Additionally, it meant I'd have to get creative if I wanted to avoid adding extra components for the periodic tasks. After some research I ended up using [an extension of the Huey library](https://huey.readthedocs.io/en/latest/contrib.html#mini-huey) that runs them inside a greenlet of the main application process.

The good side of using Python was that I could leverage its rich libraries for for the HTTP server and client, feed parsing, scraping, and database access.


### Testing (or lack thereof)

Perhaps the most controversial aspect of the project was that I didn't bother writing tests for it. In a sense, it made me feel *dirty*, but I think it was the right call given what I was trying to accomplish.

Test don't work for me as a design tool. While I see the value in TDD and think everyone should give a try, I don't feel it's a general purpose methodology, one that's necessarily applicable to any project by any person. I've found that the point of view enforced by TDD is not a good match for how I prefer to reason about code to solve a problem.

TDD considerations aside, unit tests <are good to verify that the logic works as expected and that we don't introduce bugs when making refactors, so it's a good asset (a good investment) for project maintenance.> Given that I was going to experiment, adding, removing and rearranging features, tests would break often and require more effort than the value they provided in the short term. I didn't mind introducing little logic bugs; I was going to use the app myself so I expected that most significant bugs would surface over time.

In my experience, integration tests tend to provide more value than unit tests, in terms of confidence that the application works. <In this particular project>, the bulk of the work (and the majority of the bugs) came either from integrations with external data sources or from the user interface. And while I could have caught some bugs earlier and prevented some regressions if I had integration tests, implementing those required an effort (e.g. serving arbitrary RSS feeds locally for testing different scenarios) that just wasn't worth upfront. Now that the application is stable, though, adding integration tests sounds like a good investment.


## Development

There's an amazing zen-flow sort of thing that happens when developers use their own tools on a daily basis. Not just testing it but actually experimenting it as an end user. There's no better catalyst for ideas and experimentation, no better prioritization driver than having to face the bugs, annoyances and limitations of an application first-hand.

<after adding the basic building blocks and some trial and error with UI arrangement and controls, I <settled> on this usage pattern: open app, scroll feed, open what I want to read now, pin what I want to read later, favorite what I want to bookmark for future reference.

[desktop screenshot]

-   mozilla readability for reader view, npm dependency. side effect of producing a better send 2 kindle result than the native library

-   problem of mixed frequencies. basic solution: folders
-   drove me to auto mark as read
-   drove me to no manual archive/delete

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

for a while I left the app running on a terminal tab of my laptop, and I used it while I developed.

then I set it up in a raspberry pi in my local network. that forced me not to postpone much longer running the thing in a production like server. it also enabled me to use the app from my cellphone, which in turn gave me a reason to work on the mobile version of the UI.

[mobile screenshot]

after some time I got to a point were the app was useful enough for me that I missed it when I was out of home. This pushed me to rent a vps and (for the first time in my career) finally buy a domain to run the thing, still for personal use. And since now I had my own domain and server, why not setup a small personal page and move my blogpost out of github pages, getting a bit closer to the indie web ideal?

having it in a server also pushed me to finally add multi-user support (since I'd need some sort of authentication anyway), so added a couple of friends in there as beta testers.


## Conclusion

It took me about 3 months of (relaxed) work to put together my personal reader, which I named [feedi](https://github.com/facundoolano/feedi). I can say I succeeded in reconnecting with software development, and also in building something that I like to use every day. Far from a finished product, it feels a bit like my Emacs editor setup: a perpetually half-broken tool that can nevertheless become second nature, hard to justify from a productivity standpoint but fulfilling because it's built in my own terms.

I've been using feedi as my "front page of the internet" for a few months now. More than just a convenience, a personal reader puts me in control of the type of information I consume, more consciously in the lookout for interesting blogs and magazines, better positioned for discovery and even surprise.