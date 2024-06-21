#!/usr/bin/env python3

import os
from pathlib import Path

from jinja2 import (
    ChoiceLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    select_autoescape,
)

DEFAULT_TEMPLATES_PATH = os.path.join("templates")
DEFAULT_OUTPUT_PATH = os.path.join("out")


def main():
    loaders = []
    # loaders.append(PackageLoader("confgen.templates"))

    if os.path.exists(DEFAULT_TEMPLATES_PATH):
        loaders.append(FileSystemLoader(DEFAULT_TEMPLATES_PATH))

    env = Environment(loader=ChoiceLoader(loaders), autoescape=select_autoescape())

    Path(DEFAULT_OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    data = {"someVar": "someValue"}

    for template_name in env.list_templates():
        name, _ = os.path.splitext(template_name)
        template = env.get_template(template_name)

        rendered_content = template.render(data)

        with open(
            os.path.join(DEFAULT_OUTPUT_PATH, name), "w", encoding="utf-8"
        ) as out_file:
            out_file.write(rendered_content)


if __name__ == "__main__":
    main()
