#!/usr/bin/env python3
import os
import re
import sys


def migrate_dir(src):
    posts = {}
    for filename in os.listdir(src):
        if re.match(r'^\d{4}-\d{2}-\d{2}', filename):
            dest = "-".join(filename.split("-")[3:])
            posts[filename] = dest
            print(filename, "->", dest)

    os.makedirs("blog", exist_ok=True)
    for filename, dst in posts.items():
        content = migrate_file(os.path.join(src, filename))
        dst_path = os.path.join("blog", dst)
        for filename, dst in posts.items():
            content = content.replace("file:../" + filename,
                                      "file:" + dst)

        with open(dst_path, "w") as file:
            file.write(content)
            print("wrote", dst_path)


def migrate_file(src):
    content = ""
    front_matter = ""
    with open(src) as src:
        line = next(src)
        while line:
            if line.startswith("#+BEGIN_EXPORT"):
                next(src)  # ---
                line = next(src)
                while line and line.strip() != "---":
                    front_matter += line
                    line = next(src)
                while line and not line.startswith("#+END_EXPORT"):
                    line = next(src)
                break
            else:
                content += line
                line = next(src)

        return "---\n" + front_matter + "---\n" + content + src.read()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: migrate.py src dest")
        exit(1)

    src = sys.argv[1]
    if os.path.isdir(src):
        migrate_dir(src)
    else:
        print(migrate_file(src))
