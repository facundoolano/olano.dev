#!/usr/bin/env python3
# Fetch goodreads RSS feeds and dump to data files

from datetime import datetime
import requests
import re
import unicodedata
from pathlib import Path

import yaml
import feedparser


FEED_BASE_URL = "https://www.goodreads.com/review/list_rss/19714153"
READING_FEED = f"{FEED_BASE_URL}?shelf=currently-reading"
READ_FEED = f"{FEED_BASE_URL}?shelf=read&sort=date_read"

DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"
ASSETS_DIR = "src/assets/img/reads"


def fetch_feeds(feed_url, outfile, with_images=False, pages=1):
    books = []
    for page in range(1, pages + 1):
        page_feed_url = f"{feed_url}&page={page}"
        feed_data = feedparser.parse(page_feed_url)
        books += feed_to_dict(feed_data)

    if with_images:
        # fetch images only if not already present
        for book in books:
            download_image(book["cover_url"], book["cover_file"])

    with open(outfile, "w") as file:
        yaml.dump(books, file, default_flow_style=False, allow_unicode=True)


def feed_to_dict(data):
    reads = []
    for entry in data.entries:
        published = datetime.strptime(entry.published, DATE_FORMAT).date()
        user_date = entry.user_read_at or entry.user_date_added
        user_date = datetime.strptime(user_date, DATE_FORMAT).date()

        title = remove_parenthesized_suffix(entry.title)

        cover_url = entry.book_large_image_url
        ext = cover_url.split(".")[-1]
        cover_file = f"{sluggify(entry.author_name)}-{sluggify(title)}.{ext}"

        book = {
            "title": title,
            "author": entry.author_name,
            "cover_url": cover_url,
            "cover_file": cover_file,
            "rating": int(entry.user_rating),
            "published_at": published,
            "read_at": user_date,
        }
        reads.append(book)
    return reads


def download_image(url, filename):
    file_path = Path(ASSETS_DIR, filename)
    if file_path.exists():
        return

    print("downloading", url)
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def remove_parenthesized_suffix(s):
    # This regex will match one or more groups of parentheses at the end of the string
    return re.sub(r"(?:\s*\([^)]*\))+$", "", s)


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
    fetch_feeds(READING_FEED, "data/reading.yaml", with_images=True)
    fetch_feeds(READ_FEED, "data/read.yaml", with_images=False, pages=2)
