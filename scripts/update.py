# need python 3.7+

import json
import logging
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

from jinja2 import Template

log = logging.getLogger(__name__)
SRC_DIR = (Path(__file__).parent.parent / "src" / "manim_fontawesome").absolute()
URL_FORMAT = "https://github.com/FortAwesome/Font-Awesome/releases/download/{FONT_AWESOME_VERSION}/fontawesome-free-{FONT_AWESOME_VERSION}-desktop.zip"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
INIT_PY_JINJA_TEMPLATE_PATH = Path(__file__).parent / "__init__.py.jinjatemplate"
INIT_PYI_JINJA_TEMPLATE_PATH = Path(__file__).parent / "__init__.pyi.jinjatemplate"
FONTAWESOME_DIR = SRC_DIR / "font-awesome"


def download_file(url: str, filepath: Path):
    log.info("Downloading %s to %s", url, filepath)
    urllib.request.urlretrieve(url, filepath)


def move(src, dest):
    log.info("Moving %s to %s", src, dest)
    shutil.move(src, dest)


def get_latest_release_version():
    headers = {}
    if GITHUB_TOKEN:
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    request = urllib.request.Request(
        "https://api.github.com/repos/FortAwesome/Font-Awesome/releases",
        headers=headers,
    )
    with urllib.request.urlopen(request) as f:
        content = json.load(f)
    return content[0]["tag_name"]


def download_and_extract_font_awesome(version):
    if not SRC_DIR.exists():
        SRC_DIR.mkdir(parents=True)
    if FONTAWESOME_DIR.exists():
        shutil.rmtree(FONTAWESOME_DIR)
    FONTAWESOME_DIR.mkdir()
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        t_file = tmpdir / "temp.zip"
        download_file(URL_FORMAT.format(FONT_AWESOME_VERSION=version), t_file)
        log.info("Extracting %s to %s", t_file, tmpdir)
        with zipfile.ZipFile(t_file) as zip_file:
            zip_file.extractall(tmpdir)
        log.info("Copying files.")
        move(
            tmpdir / f"fontawesome-free-{version}-desktop" / "LICENSE.txt",
            FONTAWESOME_DIR,
        )
        move(tmpdir / f"fontawesome-free-{version}-desktop" / "svgs", FONTAWESOME_DIR)
    log.info("Download and extract Font Awesome v%s successfully", version)


def get_jinja_template(pth) -> Template:
    with open(pth) as f:
        return Template(f.read())


def convert_filename_to_function(var: str):
    var = var.removesuffix(".svg")
    var = var.replace("-", "_")
    is_start_int = True
    try:
        int(var[0])
    except ValueError:
        is_start_int = False
    if is_start_int:
        var = "_" + var

    return var


def main():
    version = get_latest_release_version()
    download_and_extract_font_awesome(version)
    svg_dir = FONTAWESOME_DIR / "svgs"
    template = get_jinja_template(INIT_PY_JINJA_TEMPLATE_PATH)

    @dataclass
    class Icon:
        name: str
        filename: str

    brand_icons = []
    for svg in (svg_dir / "brands").iterdir():
        module_name = convert_filename_to_function(svg.name)
        brand_icons.append(Icon(name=module_name, filename=svg.name))

    regular_icons = []
    for svg in (svg_dir / "regular").iterdir():
        module_name = convert_filename_to_function(svg.name)
        regular_icons.append(Icon(name=module_name, filename=svg.name))

    solid_icons = []
    for svg in (svg_dir / "solid").iterdir():
        module_name = convert_filename_to_function(svg.name)
        solid_icons.append(Icon(name=module_name, filename=svg.name))
    init_py = template.render(
        brand_icons=brand_icons,
        regular_icons=regular_icons,
        solid_icons=solid_icons,
        font_awesome_version=version,
    )
    with open(SRC_DIR / "__init__.py", "w", encoding="utf-8") as f:
        f.write(init_py)

    # for editor support
    template = get_jinja_template(INIT_PYI_JINJA_TEMPLATE_PATH)
    init_pyi = template.render(
        brand_icons=brand_icons,
        regular_icons=regular_icons,
        solid_icons=solid_icons,
        font_awesome_version=version,
    )
    with open(SRC_DIR / "__init__.pyi", "w", encoding="utf-8") as f:
        f.write(init_pyi)

    # Add a py.typed file. See PEP 484
    with open(SRC_DIR / "py.typed", "w") as f:
        f.write("")
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
