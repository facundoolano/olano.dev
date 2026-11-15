#!/usr/bin/env python3
# Fetch public Goodreads widgets and merge books into the blog's YAML files.
# Dependencies: requests, beautifulsoup4, pyyaml (see `make venv`).

import ast
import re
import unicodedata
from datetime import date
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

WIDGET_URL = "https://www.goodreads.com/review/custom_widget/19714153"
ASSETS_DIR = Path("src/assets/img/reads")


def fetch_books(shelf):
    response = requests.get(
        WIDGET_URL,
        # Goodreads rejects requests' default python-requests User-Agent.
        headers={"User-Agent": "Mozilla/5.0"},
        params={
            "shelf": shelf,
            "sort": "date_read",
            "order": "d",
            "num_books": 100,  # The custom widget caps results at 100.
            # Goodreads caches widgets by ID, so each shelf needs its own.
            "widget_id": f"olano_{shelf}",
            "show_title": 1,
            "show_author": 1,
            "show_cover": 1,
            "show_rating": 1,
            "show_review": 0,
        },
        timeout=30,
    )
    response.raise_for_status()
    return parse_widget(response.text)


def parse_widget(javascript):
    # The response is HTML inside a quoted JS string. Decode it, don't execute it.
    match = re.search(r"var widget_code = ('(?:\\.|[^'\\])*')", javascript)
    if not match:
        raise ValueError("Goodreads did not return a widget")
    html = ast.literal_eval(match[1].replace(r"\/", "/"))
    soup = BeautifulSoup(html, "html.parser")
    if not soup.select_one('[class^="gr_custom_container_"]'):
        raise ValueError("Goodreads widget container is missing")

    books = []
    for item in soup.select('[class^="gr_custom_each_container_"]'):
        title_link = item.select_one('[class^="gr_custom_title_"] a')
        author_link = item.select_one('[class^="gr_custom_author_"] a')
        cover = item.select_one('[class^="gr_custom_book_container_"] img')
        stars = item.select('[class^="gr_custom_rating_"] img')
        if not title_link or not author_link or not cover or len(stars) != 5:
            raise ValueError("Incomplete book in Goodreads widget")
        review = re.search(r"/review/show/(\d+)", title_link["href"])
        if not review:
            raise ValueError("Goodreads review ID is missing")

        title = remove_parenthesized_suffix(title_link.get_text(strip=True))
        author = author_link.get_text(strip=True)
        # Drop Goodreads' thumbnail resize suffix to request the original cover.
        cover_url = re.sub(r"\._[^/]+_(?=\.)", "", cover["src"])
        ext = cover_url.rsplit(".", 1)[-1]
        books.append({
            "review_id": review[1],
            "title": title,
            "author": author,
            "cover_url": cover_url,
            "cover_file": f"{sluggify(author)}-{sluggify(title)}.{ext}",
            "rating": sum(
                star["src"].endswith("/gr_flat_red_star_active.png")
                for star in stars
            ),
        })
    return books


def book_key(book):
    # Fallback for existing entries that don't have a review ID yet.
    return (book["title"].casefold(), book["author"].casefold())


def merge_books(existing, fetched, *, keep_history):
    by_id = {str(book["review_id"]): book for book in existing if "review_id" in book}
    by_title = {book_key(book): book for book in existing}
    books = list(existing) if keep_history else []
    today = date.today()

    for book in fetched:
        old = by_id.get(book["review_id"])
        if old is None:
            candidate = by_title.get(book_key(book))
            if candidate is not None and "review_id" not in candidate:
                old = candidate
        if old is not None:
            # Preserve historical dates and local cover filenames.
            old.update({k: v for k, v in book.items() if k != "cover_file"})
            if not keep_history:
                books.append(old)
        else:
            new = {**book, "read_at": today}
            books.append(new)
            print(f"Adding {book['title']} ({today})")
            by_title[book_key(book)] = new
        by_id[book["review_id"]] = old if old is not None else new

    # Keep year groups contiguous and newest first for src/reads.html.
    return sorted(books, key=lambda book: str(book["read_at"]), reverse=True)


def load_books(path):
    with open(path) as file:
        return yaml.safe_load(file) or []


def save_books(path, books):
    # Replace only after a complete YAML file has been written.
    temporary = Path(f"{path}.tmp")
    with temporary.open("w") as file:
        yaml.safe_dump(books, file, default_flow_style=False, allow_unicode=True)
    temporary.replace(path)


def download_image(url, filename):
    file_path = ASSETS_DIR / filename
    if file_path.exists():
        return
    print("downloading", url)
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    file_path.write_bytes(response.content)


def remove_parenthesized_suffix(s):
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
    # Fetch and parse both shelves before changing either data file.
    reading = fetch_books("currently-reading")
    read = fetch_books("read")
    if not read:
        raise ValueError("Read shelf unexpectedly empty; leaving YAML files unchanged")

    reading = merge_books(load_books("data/reading.yaml"), reading, keep_history=False)
    read = merge_books(load_books("data/read.yaml"), read, keep_history=True)
    for book in reading:
        download_image(book["cover_url"], book["cover_file"])

    save_books("data/reading.yaml", reading)
    save_books("data/read.yaml", read)
