import subprocess
import sys
from pathlib import Path
import pytest

import manim_fontawesome

test_scene = """\
from manim import *
from manim_fontawesome import *
config.background_color = WHITE

class Test(Scene):
    def construct(self):
        self.add({name})
"""


@pytest.mark.parametrize(
    "test_input",
    [
        "brand.amazon",
        "solid.wifi",
        "regular.address_book",
    ],
)
def test_basic_animation(tmp_path, test_input):
    tmp_file = Path(tmp_path, "test.py")
    with open(tmp_file, "w") as f:
        f.write(test_scene.format(name=test_input))
    a = subprocess.run(
        [sys.executable, "-m", "manim", tmp_file, "Test", "-s"], cwd=tmp_path
    )
    assert a.returncode == 0


def test_font_awesome_version_define():
    assert manim_fontawesome.FONT_AWESOME_VERSION


@pytest.mark.parametrize(
    "inp,classa",
    [
        ("brands", manim_fontawesome._Brand),
        ("solid", manim_fontawesome._Solid),
        ("regular", manim_fontawesome._Regular),
    ],
)
def test_all_icons_exists(inp, classa):
    svg_dir = manim_fontawesome.svg_dir
    length = len([*(svg_dir / inp).iterdir()])
    assert length == len(classa)


def test_init_pyi_exists():
    assert (Path(manim_fontawesome.__file__).parent / "__init__.pyi").exists()
    assert (Path(manim_fontawesome.__file__).parent / "py.typed").exists()
