---
layout: post
title: "Reclaiming the web with a personal reader"
date: 2023-12-08
tags: [software, programación]
lang: en
---

Last year I experienced the all too common software professional burnout. I had a couple of bad projects in a row, yes, but more generally I was increasingly dissatisfied with the software industry. There was a disconnection between what I used to like about the job, what I was good at, and what <the market offered to pay me for> &#x2014;given my experience, my location and the overall economy.

I did the usual thing: I slowed down, quit my job, started therapy. I reviewed my habits: eat better, exercise, meditate. Because I didn't like the effect it had on me, but also encouraged by its apparent enshittification, I quit Twitter, the last big social media app I was still consuming. I tried to stay away from programming and reading about software for a while.

Not working was one thing, but overcoming the productivity mandate &#x2014;the feeling that I had to make the best of my time off, or that I was "recharging" in preparation for a comeback&#x2014;, was another. During this period I read *How to do Nothing*, a sort of artistic activism manifesto disguised as a self-help book, which deals exactly with these things. The author mentions Mastodon when discussing alternative online communities. I had heard about Mastodon, had seen some colleagues move over there, but never really looked at it, and I thought that now was the right time to try it.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

A few things I noticed after some weeks using Mastodon:

-   It was refreshing to be in control of the feed again, without mediators trying to sell me stuff
-   I had been using twitter as an information hub of sorts. I wasn't that much interested in its microblogging aspects, and it was the same case for Mastodon. <I'm not into posting updates, IO don't like the attention high of comments and retweets>.I was interested in following interesting people to learn when they posted on their blogs, not what they had for breakfast. I was adding bots to get updates from media and link aggregators.
-   <There were many people there going through a similar process as me (not surprising). Some of them reached to the old web and its technologies for inspiration. Things like RSS and BBS, digital gardens, web rings. People <preaching> for a the old web, or the slow, or the indie web

Things really clicked for me when I read about the ideas of the indie web, and particularly about their notion indie readers. Trying Mastodon had been nice, but what I needed to reconnect with the part I missed about the web was a feed reader, ideally one I could adjust to my preferences.

There are plenty of great RSS readers out there, and I did briefly try a few of them, but this was too tempting a project to get back in touch with programming and software development. I was going to build my own personal reader.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

As a user, I had some ideas of what I wanted to accomplish.

-   twitter like stream
    -   stream, not inbox metaphor

-   I also wanted to incorporate some features of note taking apps, particularly from Google keep, the one I (reluctantly) use more often. I wanted to have stuff like pinned and archived items, tags, favorites.

-   I wanted something that allowed me to uniformly mix blogs, link aggregators and my mastodon feed. (I eventually extended this to ingesting other notification streams like Goodreads and Github)
    -   different sources would have to be customizable to have a good and consistent look and feel regardless of what each source would publish in their rss or api

-   I didn't need much of the indie reader social features. I didn't mind an extra click if I wanted to react to or comment on a post

-   I knew I'd eventually want to have some sort of reader mode to avoid jumping off the app, dealing with paywalls and annoying consent popups

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

As a developer, I wanted to <put to practice> a lot of the things I'd been thinking and writing about for the past year.

although I haven't formulated it in those terms yet, I wanted to apply the rationale that I recently described in another post: user > ops > dev.

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

there's an amazing zen-flow sort of thing that happens when developers get to use their own tools on a daily basis. not testing it but actually wanting to use it because its useful to them. it's an amazingly accurate way of prioritizing bug fixes and features according to how they affect the UX, and a catalyst for ideas and experimentation.

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