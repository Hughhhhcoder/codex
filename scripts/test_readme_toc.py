from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from readme_toc import generate_toc_lines


def test_generate_toc_lines_ignores_headings_inside_tilde_fences() -> None:
    content = """## Before
~~~markdown
## Not a heading
~~~
## After
"""

    assert generate_toc_lines(content) == [
        "- [Before](#before)",
        "- [After](#after)",
    ]


def test_generate_toc_lines_keeps_triple_backticks_inside_long_fences() -> None:
    content = """## Before
````markdown
## Not a heading
```
## Still not a heading
````
## After
"""

    assert generate_toc_lines(content) == [
        "- [Before](#before)",
        "- [After](#after)",
    ]


def test_generate_toc_lines_still_handles_regular_fences() -> None:
    content = """## Before
```markdown
## Not a heading
```
## After
"""

    assert generate_toc_lines(content) == [
        "- [Before](#before)",
        "- [After](#after)",
    ]
