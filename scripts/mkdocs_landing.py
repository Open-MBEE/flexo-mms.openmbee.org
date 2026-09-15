"""Render docs/README.md with the landing page template, and check the templates' links.

Selecting the template here rather than in front matter keeps the page plain Markdown
on GitHub. The site-relative links the templates in overrides/ hold, which MkDocs cannot
validate, are checked against the built file set so a renamed page fails `--strict`.
"""

import logging
import re
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.landing")

LANDING = "README.md"
TEMPLATE = "home.html"

# `{{ 'services/layer1/'|url }}` — the site-relative targets a template links to.
URL_FILTER = re.compile(r"""\{\{\s*['"]([^'"]+)['"]\s*\|\s*url\s*\}\}""")


def _source_candidates(target: str) -> list[str]:
    """The docs/ paths that would publish at `target`, under use_directory_urls."""
    path = target.split("#", 1)[0].strip("/")
    if not path:
        return ["index.md", LANDING]
    return [f"{path}.md", f"{path}/index.md", f"{path}/{LANDING}"]


def on_files(files, config):
    overrides = Path(config["theme"].custom_dir or "")
    if not (overrides / TEMPLATE).is_file():
        log.warning("the landing page template %s is missing", overrides / TEMPLATE)
        return files

    published = {file.src_uri for file in files if file.inclusion.is_included()}
    for template in sorted(overrides.glob("**/*.html")):
        name = template.relative_to(overrides)
        for target in dict.fromkeys(URL_FILTER.findall(template.read_text())):
            if not any(candidate in published for candidate in _source_candidates(target)):
                log.warning("%s links to %r, which no page publishes", name, target)
    return files


def on_page_markdown(markdown: str, page, **_kwargs) -> str:
    if page.file.src_uri == LANDING:
        page.meta["template"] = TEMPLATE
        page.meta["hide"] = ["navigation", "toc"]
    return markdown
