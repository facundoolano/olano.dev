---
layout: post
title: "Reclaiming the Web with a personal reader"
date: 2023-12-08
tags: [software, programación]
lang: en
---

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

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

As a user, I had some ideas of what I was trying to accomplish.

Rather than the email inbox metaphor I've most commonly seen used as RSS reader interfaces, I wanted something that felt like the Twitter or Mastodon home feed. That is: rather than [a backlog](https://danq.me/2023/07/29/rss-zero/) to clear every day, I wanted to get [a renewed stream](https://www.oliverburkeman.com/river) of interesting articles every time I opened the app. The feed would include articles from blogs, magazines, news sites and link aggregators, mixed with status updates and notifications from my Mastodon account (I eventually extended it to include my home feeds from Goodreads and Github). The parsing for those sources should be customizable to ensure a consistent look and feel, regardless of what I got back from their RSS feeds or their APIs.

Although I planned to ingest Mastodon updates and links from aggregator sites, I wasn't really interested in implementing a fully-fledged indie reader to react and comment to items within my app. I didn't really mind opening another tab to comment, nor that my "content" would then be scattered across different sites.

I also knew that I'd eventually need some sort of reader view, like the one in Firefox, to avoid jumping off the app to read, and to skip paywalls and annoying consent popups.

That's what I started with, but as soon as I had the most basic features in place, development would continue driven by *what felt right* and *what felt missing* as a user. My short-term goal was to answer, as soon as possible, this question: could this eventually become my primary (or sole) source of information in the Web? If not, I'd drop the project right away. Otherwise, I could move onto whatever was missing to realize that vision.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

As a developer, I wanted to test the ideas I'd been ruminating on for over year.

although I haven't formulated it in those terms yet, I wanted to apply the rationale that I recently described in another post: user > ops > dev.

<it was paramount that this didn't turn into a learning project or, worse, a portfolio project. This was about reconnecting with what I love about software development. While it was a leisure project, the fun wouldn't come from *building something* but from *using something I had built*.

-   I wanted to put the user first. and in this case the user would be me. I would be dogfooding, a sort of self-portrait.
    -   I had a working hypothesis: even if I wanted this to be useful for other people, I had a better shot at doing it by over-fitting (?) it to my quirks and preferences than by keeping it generic to cover what I could speculate would be the average user's requirements

-   this meant for example I could postpone fundamental features like user auth, since I knew I was going to be the single user for a while; validations, since I knew what not to do and I didn't care if I blew things up; web UI for infrequent operations that I could handle at the terminal.
-   likewise doing overly-specific stuff like streamlining support to send articles to kindle from early on

-   withe same rationale, I new I was able to code my way out of problems, so rather than trying to come up with a generic one-size-fits-all rss parser or a complex UI to parametrize parsing instructions. I just wrote a code structure that allowed me to easily override, in the python source, how I wanted specific sites to be parsed. This gave me arbitrary customizability without complicated code, and it naturally extended to parsing arbitrary sites that didn't expose an RSS feed. (albeit assuming the cost of writing scrapers that will eventually fail when the source changes)

-   I wanted for the thing to be easy to deploy and operate. This would have pointed me, I think, to golang. But I'm not a golang developer, and although I could have used this as an excuse to learn it, I explicitly decided not to: I didn't want to shift the goal into making it a learning project (much less a portfolio-building project). I've done that in the past, and I know it drives the development in a different direction.
    -   I wanted to go in the direction that reduced the time it took me to put the functionality in front of the user (me), to see how the app felt and be able to iterate on features and user experience. Because that's where it was going to be decided if the app would end up being useful at all, and a worthy to keep investing in its development.
    -   because of this I decided to go with python, at the expense of it being more difficult to deploy and run (because of dependency issues, and lack of good native concurrency support)

-   I didn't need a scalable database. sqlite was good enough, and it simplified project setup
-   likewise, while I needed some sort of concurrency and periodic tasks support, I didn't want to introduce a separate worker process, nor a dependency on redis, nor I wanted to rely on cronjobs (which I felt made the local dev and prod deploy experiences diverge too much). I found the minihuey task runner, which more or less fit the bill.
    -   I had to force it a bit, the code I ended up with is a bit of brittle, but it's another case of putting ops first.
    -   again, the ideal would have been to have goroutines deal with concurrency and periodic tasks, but I sacrificed that option in favor of using a known stack to iterate faster.

-   I also didn't see much benefit to implement the protocols and separation of concerns of indie readers. I much preferred a monolitic app, since I was doing all the development myself, especially one that I could easily deploy

-   needless to say, this had to be a web app
    -   because using html and the browser was the reasonable way to use the same interface on all my devices, and because a server was the easiest way to keep the state synchronized between them.
-   I drew heavily from the choose boring tech and radical simplicity mindset. I wanted a web app yes, with some dynamic bits, but I wanted to lean on the browser native features as much as possible.
    -   htmx. felt picking up web dev where I left off 10 years ago

perhaps the most controversial decision I made, one that made me feel *dirty* but that I still stand by and think was the right call, was to not having tests for the app.

-   it's no use for me as a design tool (my take is that this is extremely subjective and it just not the way my head works)
-   unit tests didn't provide much value in making the software robust. most errors come from the integration and UI, things that would by definition be excluded from unit tests.
-   admittedly, UI and integration tests would add up a lot of value to the project, in terms of its long-term maintenance and preventing regressions when adding new features
-   but, in the context of this being a project for a single user which was me, I knew I could live with bugs and preferred to just move fast to try features
-   At heart, this was more of a prototype than a long term development. but they meant slowing the development cycle down, and in some cases investing in testing features I would just try and end up removing in the short term.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

for a while I used the thing in my desktop then I set it up in a raspberry pi in my local network. that forced me not to postpone much longer running the thing in a production like server. it also enabled me to use the app from my cellphone, which in turn gave me a reason to work on the mobile version of the UI.

after some time I got to a point were the app was useful enough for me that I missed it when I was out of home. This pushed me to rent a vps and (for the first time in my career) finally buy a domain to run the thing, still for personal use.

And since now I had my own domain and server, why not setup a small personal page and move my blogpost out of github pages, getting a bit closer to the indie web ideal?

having it in a server also pushed me to finally add multi-user support (since I'd need some sort of authentication anyway), so added a couple of friends in there as beta testers.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

There's an amazing zen-flow sort of thing that happens when developers use their own tools on a daily basis. Not just testing it, but actually experimenting it as an end user. There's no better catalyst for ideas and experimentation, no better prioritization driver than having to face the bugs, annoyances and limitations of an application first-hand.

-   problem of mixed frequencies
-   drove me to auto mark as read
-   drove me to no manual archive/delete

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

perpetual state of half-brokenness, much like me emacs editor configuration. an ergonomic half-brokenness that's hard to justify from a productivity standpoint but that it's fulfilling because it's using my own tool in my own terms, and learning and reflecting about my craft in the process.

and I can say that I succeeded in enabling a virtuous cycle of web surfing and learning, staying up to date with the outlets I care about, being able to add new ones with little friction, and having always some fresh interesting food for thought, with less noise, less unwanted garbage and less toxicity than traditional social media.

<br/>
<hr/>

*The feedi project is available [on GitHub](https://github.com/facundoolano/feedi).*