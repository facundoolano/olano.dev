#!/usr/bin/env python3
import os
import sys


def migrate_dir(src):
    pass


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
