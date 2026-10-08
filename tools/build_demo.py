"""Build the standalone demo from its editable HTML fragment using only Python."""

import argparse
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "__PROMPT_WORKSHOP_FRAGMENT__"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify index.html is current without changing files")
    args = parser.parse_args()
    fragment = (ROOT / "src" / "prompt-workshop.html").read_text(encoding="utf-8")
    template = (ROOT / "tools" / "standalone-template.html").read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise SystemExit("The standalone template must contain exactly one fragment marker.")
    document = template.replace(MARKER, escape(fragment))
    destination = ROOT / "index.html"
    if args.check:
        if not destination.exists() or destination.read_text(encoding="utf-8") != document:
            raise SystemExit("index.html is out of date. Run python tools/build_demo.py.")
        print("index.html matches the source.")
        return
    with destination.open("w", encoding="utf-8", newline="\n") as output:
        output.write(document)
    print("Built index.html")


if __name__ == "__main__":
    main()
