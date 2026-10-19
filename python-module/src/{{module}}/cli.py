"""CLI entry point for {{name}}."""

import argparse
import sys

from {{module}}.core import hello


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="{{name}}",
        description="{{description}}",
    )
    parser.add_argument("--name", default="world", help="Name to greet")
    args = parser.parse_args(argv)

    print(hello(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
