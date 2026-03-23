name = "Alexiy Buynitsky"

import os
from shutil import rmtree
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
import mistune, frontmatter

parser = argparse.ArgumentParser(description="Build the website")
parser.add_argument("--output", help="Output directory", default="dist")
parser.add_argument(
    "--no-clean", help="Don't clean the output directory", action="store_true"
)

args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))

env = Environment(
    loader=FileSystemLoader(f"{script_path}/templates"),
    autoescape=select_autoescape(["html"]),
)

if not args.no_clean:
    # delete everything inside the output directory
    for root, dirs, files in os.walk(args.output):
        for file in files:
            if file == "index.css":
                continue
            os.remove(os.path.join(root, file))

        for dir in dirs:
            rmtree(os.path.join(root, dir))


def write_output(content, *path):
    # make sure every directory in the path exists
    for i in range(len(path) - 1):
        if not os.path.exists(os.path.join(args.output, *path[: i + 1])):
            os.makedirs(os.path.join(args.output, *path[: i + 1]))

    with open(os.path.join(args.output, *path), "w") as f:
        f.write(content)


def load_bullet_list_markdown(file_path):
    items = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("- "):
                items.append(stripped[2:].strip())
    return items


def get_post(folder, file):
    obj = frontmatter.load(f"posts/{folder}/{file}")
    html = mistune.html(obj.content)

    obj.content = html
    obj["slug"] = file.replace(".md", "")
    obj["href"] = f"/{folder}/{obj['slug']}"

    if "order" not in obj:
        obj["order"] = 0

    return obj


def render_post(folder, post):
    template = env.get_template(f"posts/{folder}/page.html")
    return template.render(post=post, title=f"{name} | {post['title']}", name=name)


def render_post_list(folder, posts):
    template = env.get_template(f"posts/{folder}/list.html")
    return template.render(posts=posts)


custom_random_pages = [
    {
        "slug": "favorite_mtb",
        "title": "Mountain Biking",
        "template": "random/favorite_mtb.html",
    },
    {
        "slug": "favorite_hikes",
        "title": "Favorite Hikes",
        "template": "random/favorite_hikes.html",
    },
    {
        "slug": "favorite_books",
        "title": "Favorite Books",
        "template": "random/favorite_books.html",
    },
    {
        "slug": "happiness",
        "title": "Happiness",
        "template": "random/happiness.html",
    },
]


post_folders = [f for f in os.listdir("posts") if os.path.isdir(f"posts/{f}")]
lists = {}

for post_folder in post_folders:
    post_files = [f for f in os.listdir(f"posts/{post_folder}") if f.endswith(".md")]

    if post_folder == "random":
        custom_slugs = {page["slug"] for page in custom_random_pages}
        custom_slugs.add("coffee_shops")
        post_files = [f for f in post_files if f.replace(".md", "") not in custom_slugs]

    posts = [get_post(post_folder, f) for f in post_files]
    posts = sorted(posts, key=lambda x: x["order"])

    for post in posts:
        write_output(
            render_post(post_folder, post), post_folder, f"{post['slug']}.html"
        )

    lists[post_folder] = render_post_list(post_folder, posts)


for page in custom_random_pages:
    template = env.get_template(page["template"])
    write_output(
        template.render(title=f"{name} | {page['title']}", name=name),
        "random",
        f"{page['slug']}.html",
    )


index = env.get_template("index.html")
quotes = load_bullet_list_markdown("src/data/random_quotes.md")

write_output(
    index.render(lists=lists, quotes=quotes, name=name, title=name), "index.html"
)
