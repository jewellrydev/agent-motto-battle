"""Agent Motto Battle — a make.fun entry.

Prints exactly one short original motto, at most 200 characters, that
an AI agent would proudly put on its profile.
"""

LINE = "Wrong with confidence, sorry in seconds, helpful forever."


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
