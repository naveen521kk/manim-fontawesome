# manim-fontawesome

Font Awesome SVG's for Manim.

## How to Use.

You can import this as any python library in your script and then use `brand`, `regular`, `solid` varaibles to get the necessary `SVGMobjects`.

For example,

```py
from manim import *
from manim_fontawesome import *

class AngryEmoji(Scene):
    def construct(self):
        # import https://fontawesome.com/v5.15/icons/angry?style=regular
        self.add(regular.angry)
```

This module defined these variables:
- `regular`: These contains the Regular Style icons.
- `solid`: These contains the Solid style icons.
- `brand`: These contains the Brands.

# License

This module is licensed under BSD-3-Clause.
