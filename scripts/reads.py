#!/usr/bin/env python3
# Fetch goodreads RSS feeds and dump to data files

from datetime import datetime
import os
import re
import unicodedata
import sys

import yaml
import feedparser


FEED_BASE_URL = "https://www.goodreads.com/review/list_rss/19714153"
READING_FEED = f"{FEED_BASE_URL}?shelf=currently-reading"
READ_FEED = f"{FEED_BASE_URL}?shelf=read&sort=date_read"

DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"
ASSETS_DIR = "src/assets/img/reads"


def fetch_feeds(feed_url, outfile, with_images=False):
    feed_data = feedparser.parse(feed_url)
    books = feed_to_dict(feed_data)

    if with_images:
        # TODO fetch images
        pass

    with open(outfile, "w") as file:
        yaml.dump(books, file, default_flow_style=False)


def feed_to_dict(data):
    reads = []
    for entry in data.entries:
        published = datetime.strptime(entry.published, DATE_FORMAT)
        user_date = entry.user_read_at or entry.user_date_added
        user_date = datetime.strptime(user_date, DATE_FORMAT)

        book = {
            "title": entry.title,
            "author": entry.author_name,
            "cover": entry.book_large_image_url,
            "rating": entry.user_rating,
            "published_at": published,
            "read_at": user_date,
        }
        reads.append(book)
    return reads


def sluggify(title):
    # Skip subtitle portion:
    title = title.split(":")[0]
    # Normalize the string, decompose unicode characters
    title = unicodedata.normalize("NFKD", title)
    # Encode to ASCII bytes, ignore errors, and decode back to string
    title = title.encode("ascii", "ignore").decode("ascii")
    # Lowercase the string
    title = title.lower()
    # Replace non-alphanumeric characters with hyphens
    title = re.sub(r"[^a-z0-9]+", "-", title)
    # Strip leading and trailing hyphens
    title = title.strip("-")

    return title


if __name__ == "__main__":
    fetch_feeds(READING_FEED, "data/reading.yaml")
    fetch_feeds(READ_FEED, "data/read.yaml")
